"""Extract a local PDF archive to page-preserving Markdown files."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pdfplumber
from pypdf import PdfReader


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def pdf_metadata(source: Path) -> tuple[int, dict[str, str]]:
    reader = PdfReader(str(source))
    metadata = reader.metadata or {}
    normalized = {
        key.lstrip("/"): str(value)
        for key, value in metadata.items()
        if value is not None
    }
    return len(reader.pages), normalized


def extract_pdf(source: Path, input_root: Path, output_root: Path) -> dict[str, object]:
    relative_source = source.relative_to(input_root)
    target = (output_root / relative_source).with_suffix(".md")
    target.parent.mkdir(parents=True, exist_ok=True)

    page_count, metadata = pdf_metadata(source)
    extracted_pages = 0
    blank_pages: list[int] = []
    errors: list[str] = []

    lines = [
        f"# {source.stem}",
        "",
        "## Origem",
        "",
        f"Arquivo PDF: `{relative_source.as_posix()}`",
        f"Páginas declaradas: {page_count}",
        "Método: extração da camada de texto com preservação aproximada do layout.",
    ]
    if metadata:
        lines.extend(["", "## Metadados do PDF", ""])
        for key, value in sorted(metadata.items()):
            lines.append(f"- {markdown_escape(key)}: {markdown_escape(value)}")

    lines.extend(["", "## Conteúdo por página", ""])

    try:
        with pdfplumber.open(source) as pdf:
            for number, page in enumerate(pdf.pages, start=1):
                lines.extend([f"### Página {number}", ""])
                try:
                    text = page.extract_text(layout=True) or ""
                except Exception as error:  # Continue with the remaining pages.
                    text = ""
                    errors.append(f"Página {number}: {type(error).__name__}: {error}")

                if text.strip():
                    lines.extend([text.rstrip(), ""])
                    extracted_pages += 1
                else:
                    lines.extend(["_Sem camada de texto extraível nesta página; requer conferência visual ou OCR._", ""])
                    blank_pages.append(number)
    except Exception as error:
        errors.append(f"Arquivo: {type(error).__name__}: {error}")

    target.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return {
        "source": relative_source.as_posix(),
        "markdown": target.relative_to(output_root).as_posix(),
        "pages": page_count,
        "pages_with_text": extracted_pages,
        "blank_pages": blank_pages,
        "errors": errors,
    }


def write_inventory(results: list[dict[str, object]], output_root: Path) -> None:
    failures = [item for item in results if item["errors"]]
    partials = [item for item in results if item["blank_pages"]]
    total_pages = sum(int(item["pages"]) for item in results)
    pages_with_text = sum(int(item["pages_with_text"]) for item in results)

    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "documents": len(results),
        "pages": total_pages,
        "pages_with_text": pages_with_text,
        "documents_with_blank_pages": len(partials),
        "documents_with_errors": len(failures),
        "items": results,
    }
    (output_root / "inventario_extracao.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Inventário de extração do acervo",
        "",
        f"- Documentos processados: {len(results)}",
        f"- Páginas declaradas: {total_pages}",
        f"- Páginas com texto extraído: {pages_with_text}",
        f"- Documentos com páginas sem texto: {len(partials)}",
        f"- Documentos com erros: {len(failures)}",
        "",
        "## Documentos",
        "",
        "| PDF de origem | Markdown | Páginas | Com texto | Páginas sem texto | Erros |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in results:
        lines.append(
            "| "
            f"`{item['source']}` | `{item['markdown']}` | {item['pages']} | "
            f"{item['pages_with_text']} | {len(item['blank_pages'])} | {len(item['errors'])} |"
        )
    lines.extend(
        [
            "",
            "Arquivos com páginas sem texto foram preservados com marcadores por página; "
            "esses casos exigem OCR ou revisão visual para captura adicional.",
        ]
    )
    (output_root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_root", type=Path)
    parser.add_argument("output_root", type=Path)
    args = parser.parse_args()

    input_root = args.input_root.resolve()
    output_root = args.output_root.resolve()
    if not input_root.is_dir():
        raise SystemExit(f"Diretório de entrada não encontrado: {input_root}")
    if output_root.exists():
        raise SystemExit(f"Diretório de saída já existe: {output_root}")

    pdfs = sorted(path for path in input_root.rglob("*") if path.is_file() and path.suffix.lower() == ".pdf")
    if not pdfs:
        raise SystemExit("Nenhum PDF encontrado.")

    output_root.mkdir(parents=True)
    results = [extract_pdf(pdf, input_root, output_root) for pdf in pdfs]
    write_inventory(results, output_root)
    print(f"Processados {len(results)} PDFs em {output_root}")


if __name__ == "__main__":
    main()
