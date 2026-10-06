"""Caminhos únicos dos semanários; documentação administrativa fica na raiz."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SEMANARIOS_ROOT = REPO_ROOT / "docs" / "semanarios"
MD_ROOT = SEMANARIOS_ROOT / "md"
DOCX_ROOT = SEMANARIOS_ROOT / "docx"


def docx_path(markdown_path: Path) -> Path:
    return (DOCX_ROOT / markdown_path.resolve().relative_to(MD_ROOT)).with_suffix(".docx")


def semanarios(segmento: str | None = None) -> list[Path]:
    return sorted((MD_ROOT / segmento if segmento else MD_ROOT).rglob("semanario*.md"))
