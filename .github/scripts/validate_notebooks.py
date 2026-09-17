#!/usr/bin/env python3
"""Quality checks for the Python course notebooks.

The checker deliberately validates notebooks without executing them: course material can
contain exercises with intentional runtime errors that students are expected to fix.
"""

from __future__ import annotations

import ast
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import nbformat
from IPython.core.inputtransformer2 import TransformerManager
from nbformat.validator import NotebookValidationError


ROOT = Path(__file__).resolve().parents[2]
ALLOWED_EMPTY_NOTEBOOKS = {
    Path("COURSES/002_Getting-Started/AP_LAB_002.ipynb"),
}

MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*\bsrc=['\"]([^'\"]+)['\"]", re.IGNORECASE)
CONFLICT_RE = re.compile(r"^(?:<<<<<<< .+|>>>>>>> .+)$", re.MULTILINE)

transformer = TransformerManager()
failures: list[tuple[Path, str]] = []
warnings: list[tuple[Path, str]] = []


def relative(path: Path) -> Path:
    return path.resolve().relative_to(ROOT.resolve())


def annotation(level: str, path: Path, message: str) -> None:
    clean = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::{level} file={relative(path).as_posix()}::{clean}")


def extract_image_targets(markdown: str) -> set[str]:
    return set(MARKDOWN_IMAGE_RE.findall(markdown)) | set(HTML_IMAGE_RE.findall(markdown))


def local_image_path(notebook: Path, target: str) -> Path | None:
    target = target.strip().strip("<>")
    parsed = urlsplit(target)

    if parsed.scheme in {"http", "https"}:
        if parsed.netloc != "raw.githubusercontent.com":
            return None

        parts = unquote(parsed.path).lstrip("/").split("/")
        if parts[:2] != ["S-L-A-K-E-R", "PYTHON_courses"]:
            return None

        tail = parts[2:]
        if tail[:3] == ["refs", "heads", "main"]:
            tail = tail[3:]
        elif tail[:1] == ["main"]:
            tail = tail[1:]
        else:
            # A raw link to another ref cannot reliably be checked against this checkout.
            return None

        return ROOT.joinpath(*tail)

    if parsed.scheme or target.startswith("#"):
        return None

    path_part = unquote(parsed.path)
    if not path_part:
        return None

    if path_part.startswith("/"):
        return ROOT / path_part.lstrip("/")

    return notebook.parent / path_part


def check_images(notebook: Path, markdown: str, cell_number: int) -> None:
    for target in extract_image_targets(markdown):
        candidate = local_image_path(notebook, target)
        if candidate is None:
            continue

        try:
            resolved = candidate.resolve()
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            failures.append(
                (notebook, f"Cell {cell_number}: image path escapes the repository: {target}")
            )
            continue

        if not resolved.is_file():
            failures.append(
                (notebook, f"Cell {cell_number}: referenced repository image does not exist: {target}")
            )


def check_notebook(path: Path) -> None:
    rel = relative(path)

    if path.stat().st_size == 0:
        if rel in ALLOWED_EMPTY_NOTEBOOKS:
            warnings.append((path, "Empty notebook placeholder is currently allowed."))
        else:
            failures.append((path, "Notebook is empty (0 bytes)."))
        return

    try:
        notebook = nbformat.read(path, as_version=nbformat.NO_CONVERT)
        nbformat.validate(notebook)
    except (NotebookValidationError, ValueError, OSError) as exc:
        failures.append((path, f"Invalid notebook structure/JSON: {exc}"))
        return

    language = notebook.metadata.get("language_info", {}).get("name")
    if language and language.lower() != "python":
        warnings.append((path, f"Notebook language is '{language}', not Python."))

    for index, cell in enumerate(notebook.cells, start=1):
        source = cell.get("source", "")

        if CONFLICT_RE.search(source):
            failures.append((path, f"Cell {index}: unresolved Git merge-conflict marker."))

        if cell.cell_type == "markdown":
            check_images(path, source, index)
            continue

        if cell.cell_type != "code" or not source.strip():
            continue

        try:
            transformed = transformer.transform_cell(source)
            ast.parse(transformed, filename=f"{rel.as_posix()}:cell-{index}")
        except (SyntaxError, IndentationError) as exc:
            location = f"line {exc.lineno}" if exc.lineno else "unknown line"
            failures.append(
                (path, f"Cell {index}: Python/IPython syntax error at {location}: {exc.msg}")
            )
        except Exception as exc:  # Defensive: malformed IPython syntax should still fail clearly.
            failures.append((path, f"Cell {index}: could not parse code cell: {exc}"))


def write_summary(notebooks: list[Path]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## Course notebook quality check\n\n")
        summary.write(f"- Notebooks discovered: **{len(notebooks)}**\n")
        summary.write(f"- Errors: **{len(failures)}**\n")
        summary.write(f"- Warnings: **{len(warnings)}**\n")

        if warnings:
            summary.write("\n### Warnings\n")
            for path, message in warnings:
                summary.write(f"- `{relative(path).as_posix()}`: {message}\n")


def main() -> int:
    notebooks = sorted(ROOT.rglob("*.ipynb"))

    if not notebooks:
        print("No notebooks found.")
        return 0

    for notebook in notebooks:
        check_notebook(notebook)

    for path, message in warnings:
        annotation("warning", path, message)

    for path, message in failures:
        annotation("error", path, message)

    write_summary(notebooks)

    print(
        f"Checked {len(notebooks)} notebook(s): "
        f"{len(failures)} error(s), {len(warnings)} warning(s)."
    )

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
