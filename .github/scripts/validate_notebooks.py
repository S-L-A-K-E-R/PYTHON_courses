#!/usr/bin/env python3
"""Structural quality checks for the Python course notebooks.

Python-specific errors are checked separately with Ruff in the GitHub Actions workflow.
This script focuses on notebook integrity and repository-specific course checks.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import nbformat
from nbformat.validator import NotebookValidationError


ROOT = Path(__file__).resolve().parents[2]

MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
HTML_IMAGE_RE = re.compile(r"<img\b[^>]*\bsrc=['\"]([^'\"]+)['\"]", re.IGNORECASE)
CONFLICT_RE = re.compile(r"^(?:<<<<<<< .+|>>>>>>> .+)$", re.MULTILINE)

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
    if path.stat().st_size == 0:
        # Keep unfinished/placeholder notebooks visible without blocking the workflow.
        # This is intentionally a warning: it should remind us to complete the file later,
        # while still allowing course development to continue.
        warnings.append((path, "Notebook is empty (0 bytes) and should be completed later."))
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


def write_summary(notebooks: list[Path]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return

    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("## Course notebook structural checks\n\n")
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
