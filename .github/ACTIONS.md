# ✅ GitHub Actions — Course Checks

Every update automatically checks the course files:

- 📓 **Notebook validity** — `.ipynb` files can be opened correctly.
- 🐍 **Python errors** — detects syntax errors and common coding mistakes.
- 🖼️ **Missing assets** — verifies repository images used by notebooks still exist.
- 🔀 **Git conflicts** — detects forgotten merge-conflict markers.
- 📄 **Python files** — checks regular `.py` files too.
- ⚠️ **Empty notebooks** — shown as a warning, but do not fail the checks.
- 🏷️ **Intentional error cells** — a code cell containing a comment line with `(#GA-IC)` is skipped by the Python-error check; the rest of the notebook is still checked.

> To ignore a deliberately invalid code cell, add the exact marker `(#GA-IC)` on a standalone Python comment line beginning with `#`.
>
> The marker may be anywhere in the cell — including at the very end after invalid code — because CI scans the entire cell before Ruff runs.
