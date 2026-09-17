# ✅ GitHub Actions — Course Checks

Every update automatically checks the course files:

- 📓 **Notebook validity** — `.ipynb` files can be opened correctly.
- 🐍 **Python errors** — detects syntax errors and common coding mistakes.
- 🖼️ **Missing assets** — verifies repository images used by notebooks still exist.
- 🔀 **Git conflicts** — detects forgotten merge-conflict markers.
- 📄 **Python files** — checks regular `.py` files too.
- ⚠️ **Empty notebooks** — shown as a warning, but do not fail the checks.

> **Exception:** `AP_LAB_001.ipynb` contains intentional errors for students to fix,  
> so its Python code is not checked.
