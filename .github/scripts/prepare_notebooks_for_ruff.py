#!/usr/bin/env python3
"""Prepare notebooks for Ruff by neutralizing explicitly ignored code cells.

This script runs only inside CI before Ruff. It edits the runner's temporary checkout,
never the committed notebook in the repository.
"""

from __future__ import annotations

import re
from pathlib import Path

import nbformat


ROOT = Path(__file__).resolve().parents[2]
IGNORE_MARKER = "(#GA-IC)"
IGNORE_COMMENT_RE = re.compile(r"^\s*#.*\(#GA-IC\)", re.MULTILINE)


def relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def should_ignore(source: str) -> bool:
    """Return True when any standalone comment line in the cell has the marker."""
    return bool(IGNORE_COMMENT_RE.search(source))


def neutralize(source: str) -> str:
    """Replace a tagged cell with comments while roughly preserving its line count."""
    lines = source.splitlines(keepends=True)

    if not lines:
        return f"# CI skipped cell marked {IGNORE_MARKER}\n"

    replacement: list[str] = []

    for index, line in enumerate(lines):
        if line.endswith("\r\n"):
            ending = "\r\n"
        elif line.endswith("\n"):
            ending = "\n"
        else:
            ending = ""

        if index == 0:
            replacement.append(f"# CI skipped cell marked {IGNORE_MARKER}{ending}")
        else:
            replacement.append(f"#{ending}")

    return "".join(replacement)


def main() -> int:
    notebooks = sorted(ROOT.rglob("*.ipynb"))
    skipped_cells = 0
    changed_notebooks = 0

    for path in notebooks:
        if path.stat().st_size == 0:
            continue

        notebook = nbformat.read(path, as_version=nbformat.NO_CONVERT)
        changed = False

        for cell_number, cell in enumerate(notebook.cells, start=1):
            if cell.cell_type != "code":
                continue

            source = cell.get("source", "")

            # Scan the complete source before changing anything. This intentionally allows
            # the marker to appear after broken Python code at the end of the cell.
            if not should_ignore(source):
                continue

            cell["source"] = neutralize(source)
            skipped_cells += 1
            changed = True
            print(
                f"Skipping Ruff checks for {relative(path)} "
                f"cell {cell_number}: {IGNORE_MARKER}"
            )

        if changed:
            nbformat.write(notebook, path)
            changed_notebooks += 1

    print(
        f"Prepared {len(notebooks)} notebook(s): "
        f"{skipped_cells} tagged cell(s) skipped across "
        f"{changed_notebooks} notebook(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
