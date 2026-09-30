# Copilot Repository Instructions

## General behavior

Keep changes simple, focused, and consistent with the existing repository.

Respect existing code, documentation, naming conventions, directory structure, and formatting.

Do not make unrelated refactors or cleanup unless explicitly requested.

When explaining or describing changes, use natural developer-friendly language rather than formal or generic wording.

---

## Commit messages

Commit messages should be clear, specific, and human.

### Summary

Write the summary in natural English using an active verb.

Prefer summaries that explain the meaningful change rather than mechanically listing modified files.

Good examples:

- Teach CI to skip intentionally broken notebook cells
- Tidy course links after the folder rename
- Make the crash-course exercises easier to follow
- Add the first SciPy exercises
- Simplify the README navigation
- Fix C23 compilation in CI
- Preserve both changes during the syllabus merge

Avoid generic summaries such as:

- Update files
- Make improvements
- Update README
- Fix issues
- Various changes
- Refactor code

Do not start summaries with "This commit".

Do not use Conventional Commit prefixes such as `feat:`, `fix:`, or `chore:` unless the repository already clearly follows that convention.

Keep the summary reasonably short, but clarity is more important than an arbitrary character limit.

### Description

For a very small change, omit the description entirely.

For a meaningful change, add a short description of what changed.

Prefer one short paragraph or a few concise sentences.

Explain:
- what changed;
- the useful consequence of the change;
- important implementation details when relevant.

Do not simply repeat the summary.

Do not enumerate every changed file unless those file names are important for understanding the change.

Never invent motivations, tests, bug fixes, or behavior that cannot be inferred from the actual diff.

### Tone

The tone should be:

- clear;
- natural;
- mildly conversational;
- confident but not exaggerated;
- professional without sounding corporate.

A small amount of personality is welcome when appropriate, but clarity comes first.

Avoid emojis, excessive enthusiasm, jokes, and marketing language in generated commit messages.