# PYTHON COURSES — MASTER TODO

**Based on:** `syllabus_2.0(1).md` (23 September 2026)  
**Purpose:** an editable production checklist for Google Colab COURSE and EXERCISES notebooks.  
**Scope:** every topic in the source syllabus, plus clearly marked teaching suggestions and three recurring exercise threads.  
**Status:** all boxes intentionally start unchecked; tick them as you create and review the materials.  
**Suggested priority:** `CORE` = introductory curriculum, Python Essentials, and Advanced Python. `OPTIONAL` = independent specialization modules; choose an order to suit the class. `EXTRA` = an addition suggested here, not required by the source syllabus.

> **Working rule:** a topic is not complete simply because it appears in a slide or Markdown cell. Aim for one explanation, one runnable example, one short exercise, one nontrivial application, and at least one common pitfall or edge case. The syllabus describes a learning path, **not a fixed calendar**; adjust notebook sizes to your available teaching time.

---

## 0. Production workflow — repeat for each chapter

### COURSE notebook
- [ ] Specify **3–6 measurable learning outcomes** at the beginning.
- [ ] State prerequisites and link the previous COURSE notebook if applicable.
- [ ] Introduce the problem that motivates the new concept before showing syntax.
- [ ] Include short, annotated, runnable Python examples; keep output visible where useful.
- [ ] Contrast a frequent mistake with its corrected form; avoid intentional failures in cells that are supposed to run all at once.
- [ ] Include a **Try it yourself** cell every few concepts (predict → run → explain).
- [ ] Add an end-of-chapter reference/cheat sheet and a brief recap.
- [ ] Point to the companion EXERCISES notebook and specify which knowledge it practices.
- [ ] If the chapter includes Colab-specific behavior, distinguish it from ordinary `.py` execution.
- [ ] Run **Runtime → Restart session and run all** or an equivalent clean-kernel check; verify outputs and imports.

### EXERCISES notebook
- [ ] Include **2–4 short standalone problems**, each focused on one idea.
- [ ] Include **1 debugging/prediction problem**, with a realistic erroneous snippet.
- [ ] Include **1 small synthesis exercise** combining the chapter with older knowledge.
- [ ] Include **1 incremental project milestone** where appropriate (see recurring threads below).
- [ ] Provide clear input/output examples and constraints; do not accidentally give away the algorithm.
- [ ] Add at least one meaningful edge case and a few optional `assert` checks where they are helpful.
- [ ] Mark extensions explicitly as **Bonus**, so beginners have a reachable finish line.
- [ ] Keep a teacher-only correction/reference notebook or equivalent solution notes.
- [ ] Verify that students can complete exercises without hidden state from the COURSE notebook.

### Three recurring project threads — proposed teaching design (`EXTRA`)

| Thread | Initial problem | Intermediate milestones | Advanced / specialization outcomes |
|---|---|---|---|
| **Campus Toolkit** | Calculate a fictional student's average | Grade lists, course dictionaries, functions, input validation, load/save | Data model, CLI package, tests, optional GUI |
| **Sensor Lab** | Process simulated measurements | Loops, statistics, threshold alerts, CSV files | NumPy, pandas, plots, interpolation, signal processing |
| **Log Explorer** | Count characters and keywords | Parse textual events, aggregate dates and severity, handle malformed rows | JSON/API client, generators, tests, performance, async |

*Use fictional student data and generated sensor/log data. Do not depend on access to real student records, paid APIs, or a Colab session retaining files permanently.*

---

# PART I — INTRODUCTION TO PROGRAMMING & ALGORITHMS [CORE]

**Exit target:** the learner can translate a simple problem into a functioning, readable program, using functions and an appropriate collection where necessary.

## F01 — First Python programs, values and variables

**COURSE**
- [ ] Show how a Python expression is evaluated in a REPL versus executed in a notebook code cell.
- [ ] Explain `print()`, basic string literals, comments and readable formatting.
- [ ] Explain values and variables through assignment (`=`), reassignment and descriptive names.
- [ ] Introduce `int`, `float`, `str`, `bool` and `None` at a beginner-appropriate level.
- [ ] Show `type()`, simple conversions (`int()`, `float()`, `str()`) and conversion errors.
- [ ] Introduce arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`) and operator precedence.
- [ ] Introduce `input()` and clarify that its return value is always a string.
- [ ] Show f-strings for formatting interactive output.
- [ ] Demonstrate the difference between a notebook's displayed final expression and `print()` output.

**EXERCISES**
- [ ] Standalone: personal greeting and age-next-year calculator.
- [ ] Standalone: convert seconds to hours, minutes and seconds using `//` and `%`.
- [ ] Standalone: rectangle dimensions → perimeter and area; handle numerical conversion.
- [ ] Debug: fix `input()` values concatenating instead of adding; identify `=` versus `==` later.
- [ ] **Campus Toolkit 1:** read three fictional grades and display their arithmetic mean; no loops yet.
- [ ] **Sensor Lab 1:** convert a temperature between Celsius and Fahrenheit; display a formatted result.
- [ ] Bonus: simple unit converter with two or three conversions.

## F02 — Comparisons, conditions and control flow

**COURSE**
- [ ] Introduce comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`) and Boolean results.
- [ ] Introduce `and`, `or`, `not`; illustrate precedence with parentheses.
- [ ] Explain indentation and the `if` / `elif` / `else` structure.
- [ ] Compare independent `if` statements with a mutually exclusive branch chain.
- [ ] Introduce truthiness of common values (`0`, `""`, empty collections) without overcomplicating it.
- [ ] Demonstrate chained comparisons (`0 <= score <= 20`) as a Python-specific convenience.
- [ ] Explain how to choose test cases for each branch, including equality boundaries.

**EXERCISES**
- [ ] Standalone: classify a number as positive, negative or zero.
- [ ] Standalone: ticket price determined by age and a discount flag.
- [ ] Standalone: determine whether a proposed triangle is valid, then classify it.
- [ ] Debug: explain why `if x == 1 or 2:` is incorrect; repair it.
- [ ] **Campus Toolkit 2:** reject grades outside an agreed range; display pass/fail with a configurable threshold.
- [ ] **Sensor Lab 2:** categorize a measurement as normal, warning or critical.
- [ ] Bonus: truth-table or nested-condition challenge.

## F03 — Repetition: `for`, `while` and nested loops

**COURSE**
- [ ] Explain `for` over strings and `range()`; show the exclusive upper bound.
- [ ] Show `range(start, stop, step)` and forward/backward iteration.
- [ ] Explain `while` loops, loop guards and stopping conditions.
- [ ] Introduce counters, running totals, sentinels and accumulation patterns.
- [ ] Show `break` and `continue`, including when they harm clarity.
- [ ] Demonstrate a nested loop with a small table/grid.
- [ ] Discuss infinite loops, off-by-one mistakes and choosing `for` versus `while`.

**EXERCISES**
- [ ] Standalone: multiplication table or countdown.
- [ ] Standalone: sum even numbers in a range; compare `for` and `while` solutions.
- [ ] Standalone: number-guessing game with repeated attempts.
- [ ] Debug: repair an infinite loop and two different off-by-one errors.
- [ ] **Campus Toolkit 3:** collect an unknown number of grades until a sentinel, then compute the average safely.
- [ ] **Sensor Lab 3:** generate or enter several measurements; calculate running minimum, maximum and average.
- [ ] Bonus: draw a simple ASCII shape with nested loops.

## F04 — Functions and program decomposition

**COURSE**
- [ ] Explain `def`, calling a function, parameters and arguments.
- [ ] Contrast `return` with `print()` and explain what a function returns without an explicit `return`.
- [ ] Introduce positional and keyword arguments, then simple default parameters.
- [ ] Explain local variables and a beginner-friendly view of scope.
- [ ] Split a larger problem into several small, single-purpose functions.
- [ ] Explain docstrings, meaningful names and a basic function contract (inputs, output, assumptions).
- [ ] Show simple `assert` calls for verifying pure functions; reserve systematic testing for its specialization module.

**EXERCISES**
- [ ] Standalone: `is_even(n)`, `clamp(value, low, high)` and `convert_temperature(...)`.
- [ ] Standalone: rewrite repeated code into reusable functions.
- [ ] Debug: fix a function that prints instead of returning; fix a local-variable mistake.
- [ ] **Campus Toolkit 4:** split grade input, validation, average calculation and reporting into functions.
- [ ] **Sensor Lab 4:** implement `mean_measurement(...)` for a gradually more flexible input format.
- [ ] Bonus: add doctest-style examples to two function docstrings.

## F05 — Strings and text manipulation

**COURSE**
- [ ] Explain characters, indexing, negative indices and slices.
- [ ] Explain string immutability and safe creation of a modified string.
- [ ] Iterate through a string and compare substrings using membership (`in`).
- [ ] Demonstrate useful methods: `.strip()`, `.lower()`, `.upper()`, `.split()`, `.join()`, `.replace()`, `.find()` and `.count()`.
- [ ] Explain basic formatting with f-strings and format specifiers.
- [ ] Distinguish text length, whitespace, case-sensitive matching and empty strings.
- [ ] Briefly introduce Unicode and `ord()` / `chr()` as an optional bridge from C/ASCII.

**EXERCISES**
- [ ] Standalone: count vowels and digits in a sentence.
- [ ] Standalone: palindrome check with a clearly stated normalization rule.
- [ ] Standalone: parse a simple `name:score` string.
- [ ] Debug: explain why `text[0] = "X"` fails; fix a case-sensitive comparison.
- [ ] **Log Explorer 1:** read example log messages stored in strings and count `ERROR`, `WARNING` and `INFO` occurrences.
- [ ] **Campus Toolkit 5:** standardize fictitious student names and produce formatted summaries.
- [ ] Bonus: implement a Caesar cipher or a simple word-frequency counter without external libraries.

## F06 — Lists and sequences

**COURSE**
- [ ] Explain list creation, indexing, negative indexing, slicing and nested lists.
- [ ] Compare modifying a list with creating a new one; introduce `.append()`, `.extend()`, `.insert()`, `.pop()` and `.remove()`.
- [ ] Demonstrate iteration through a list and `len()`.
- [ ] Explain list membership, concatenation and copying at an introductory level.
- [ ] Demonstrate in-place `.sort()` versus `sorted()` briefly, to revisit later.
- [ ] Discuss empty lists, invalid indices and mutation while iterating.

**EXERCISES**
- [ ] Standalone: find min/max and mean in a numeric list, including an empty-list policy.
- [ ] Standalone: remove duplicates while keeping the original order (simple approach).
- [ ] Standalone: rotate a list or find its second-largest distinct value.
- [ ] Debug: investigate an out-of-range index and an accidental modification of the original list.
- [ ] **Campus Toolkit 6:** store all grades in a list and compute per-student summaries.
- [ ] **Sensor Lab 5:** flag anomalous values and extract a subset of measurements.
- [ ] Bonus: represent a tic-tac-toe board as a nested list.

## F07 — Tuples, dictionaries and sets

**COURSE**
- [ ] Explain tuple creation, packing, indexing and when immutability is useful.
- [ ] Explain dictionary keys and values; create, access, update and remove entries.
- [ ] Demonstrate `.get()`, `.items()`, `.keys()` and `.values()`.
- [ ] Explain sets, uniqueness and basic union/intersection/difference.
- [ ] Compare when to choose a list, tuple, dictionary or set; include membership behavior.
- [ ] Explain key errors, missing keys and the requirement that dictionary keys and set items be hashable.

**EXERCISES**
- [ ] Standalone: count word frequencies with a dictionary.
- [ ] Standalone: compare two class rosters with sets (only fictitious names).
- [ ] Standalone: represent coordinates with tuples and calculate simple distances.
- [ ] Debug: fix dictionary access to a missing key and a mistaken set/list operation.
- [ ] **Campus Toolkit 7:** group grades by course using a dictionary of lists.
- [ ] **Log Explorer 2:** aggregate counts by severity and find unique event categories.
- [ ] Bonus: implement a small inventory using nested dictionaries.

## F08 — Basic algorithms and problem solving

**COURSE**
- [ ] Show a repeatable process: specify input/output → work through examples → pseudocode → code → test.
- [ ] Implement counting, accumulation, filtering and linear search patterns.
- [ ] Explain tracking a best-so-far candidate and the danger of initializing it to zero.
- [ ] Compare an iterative solution with a direct built-in solution after both are understood.
- [ ] Introduce a simple sorting algorithm conceptually (e.g., selection sort) and contrast with built-in sorting.
- [ ] Introduce simple complexity intuition (one pass vs nested passes), without making asymptotic analysis a prerequisite.
- [ ] Discuss boundary cases: empty input, duplicates, invalid data, ties and large inputs.

**EXERCISES**
- [ ] Standalone: locate the first matching item and return a useful not-found result.
- [ ] Standalone: most frequent element with a deterministic tie rule.
- [ ] Standalone: implement a basic sorting algorithm and compare against `sorted()`.
- [ ] Debug: identify an algorithm that mishandles negative numbers or duplicates.
- [ ] **Sensor Lab 6:** identify the longest consecutive run of measurements above a threshold.
- [ ] **Log Explorer 3:** find the most frequent error message and group events by severity.
- [ ] Bonus: algorithm challenge with a short pseudocode explanation and test table.

## F09 — Introductory integration milestone (`EXTRA`)

**COURSE / WORKSHOP**
- [ ] Show students how to turn a problem statement into small functions and simple data structures.
- [ ] Demonstrate a clean notebook structure: title, specification, constants, functions, demo and tests.

**EXERCISES / SUBMISSION**
- [ ] Let students select **Campus Toolkit**, **Sensor Lab** or **Log Explorer** as a mini-project.
- [ ] Require at least one condition, one loop, two functions and one collection.
- [ ] Require three normal test cases and two edge cases.
- [ ] Ask for one short paragraph explaining an implementation decision.
- [ ] Bonus: a simple interactive menu, with no file handling yet.

---

# PART II — PYTHON ESSENTIALS [CORE]

**Exit target:** the learner understands Python's object model at a practical level, iterates idiomatically, and builds robust scripts that work with files and modules.

## E01 — Names, references, objects, mutability and aliasing

**COURSE**
- [ ] Distinguish assigning a name from copying an object; use small diagrams.
- [ ] Explain immutable objects (e.g., numbers, strings, tuples) and mutable objects (e.g., lists, dictionaries, sets).
- [ ] Contrast equality (`==`) and identity (`is`); show the appropriate idiom `is None`.
- [ ] Demonstrate aliasing through `b = a` for a mutable list.
- [ ] Compare a shallow copy (`list.copy()` / slice) with a nested structure; mention `copy.deepcopy()` when justified.
- [ ] Explain function arguments as object references and why mutation can be visible to callers.
- [ ] Show the mutable default-argument pitfall and a `None`-sentinel solution.

**EXERCISES**
- [ ] Predict → run: trace variables and identities through a short sequence of assignments.
- [ ] Debug: repair an unexpectedly modified list and a mutable default-argument function.
- [ ] **Campus Toolkit 8:** clone a fictional student's course records before running a what-if grade scenario.
- [ ] Bonus: contrast copying a nested list with copying each nested list independently.

## E02 — Pythonic iteration and logical collection operations

**COURSE**
- [ ] Revisit `range()` and explain when direct iteration is clearer than indexing.
- [ ] Introduce `enumerate()` for index-value pairs and `zip()` for parallel sequences.
- [ ] Compare list/dictionary/set membership with explicit search loops.
- [ ] Explain `any()` and `all()`, including behavior on empty iterables.
- [ ] Show unpacking in `for` loops (`for name, grade in ...`).
- [ ] Discuss when `zip()` silently stops at the shortest iterable and why length mismatches may matter.

**EXERCISES**
- [ ] Standalone: number a list of items with `enumerate()`.
- [ ] Standalone: combine matching timestamps and sensor values using `zip()`.
- [ ] Standalone: check whether at least one / every student satisfies a condition using `any()` / `all()`.
- [ ] Debug: fix an index-based loop that can be simplified or has an off-by-one error.
- [ ] **Sensor Lab 7:** combine timestamp and measurement sequences into pairs and report flagged rows.

## E03 — Useful built-ins and expressive transformations

**COURSE**
- [ ] Explain `sorted()` versus `.sort()`, the `key=` argument and `reverse=True`.
- [ ] Explain `reversed()` and its difference from a newly reversed list.
- [ ] Practice `min()`, `max()` and `sum()`; discuss empty input and optional `key=` / `default=` where applicable.
- [ ] Introduce `map()` and compare it with a clear loop and, later, a comprehension.
- [ ] Review relevant general-purpose built-ins: `len()`, `abs()`, `round()`, `divmod()` and `filter()` as appropriate (`EXTRA` examples).
- [ ] Show how to read built-in documentation and discover function signatures.

**EXERCISES**
- [ ] Standalone: sort fictional students by grade, then by (grade, name) to establish a tie rule.
- [ ] Standalone: calculate total, min/max and reversed order for a dataset.
- [ ] Refactor: compare `map()` with a plain loop for converting numeric strings.
- [ ] Debug: explain why assigning the result of `.sort()` loses a list reference.
- [ ] **Campus Toolkit 9:** produce a ranked *fictional grade report* with consistent sorting and tie behavior.

## E04 — Files, `pathlib` and `with`

**COURSE**
- [ ] Show relative versus absolute paths and the working directory in Colab versus local Python.
- [ ] Introduce `pathlib.Path`, path joins, `.exists()`, `.is_file()`, `.mkdir()` and `.glob()`.
- [ ] Demonstrate `read_text()` / `write_text()` with explicit UTF-8 encoding.
- [ ] Introduce `open(..., encoding="utf-8")` and the `with` statement.
- [ ] Explain file modes (`r`, `w`, `a`) and why overwriting requires care.
- [ ] Read a text file line by line; handle trailing newlines and empty files.
- [ ] Explain where Colab files live, how to upload/download sample files, and that runtime storage is temporary.

**EXERCISES**
- [ ] Standalone: write a daily note to a file, then reload it.
- [ ] Standalone: find `.txt` files in a sample folder using `Path.glob()`.
- [ ] Debug: repair incorrect relative paths and a file that accidentally gets overwritten.
- [ ] **Campus Toolkit 10:** save and load a gradebook in a simple text/CSV-like format, clearly documenting its schema.
- [ ] **Log Explorer 4:** read real sample log *files* rather than hardcoded strings; count events per file.
- [ ] Bonus: `with` several files open and merge daily log extracts.

## E05 — Exceptions and error handling

**COURSE**
- [ ] Explain the difference between syntax errors, exceptions and incorrect program results.
- [ ] Demonstrate `try` / `except` with narrow, specific exception types.
- [ ] Introduce `else`, `finally` and deliberate `raise` for invalid inputs.
- [ ] Explain how to interpret a traceback and preserve useful diagnostic information.
- [ ] Discuss validation versus exception handling; avoid a bare `except:` that hides bugs.
- [ ] Explain how cleanup interacts with the `with` statement.

**EXERCISES**
- [ ] Standalone: safely parse an integer with a user-friendly retry policy.
- [ ] Standalone: distinguish missing files from malformed file contents.
- [ ] Debug: narrow an overly broad handler that incorrectly suppresses an error.
- [ ] **Campus Toolkit 11:** handle invalid grades, missing files and malformed saved records.
- [ ] **Log Explorer 5:** process good log rows while recording (not silently discarding) malformed rows.
- [ ] Bonus: define one small custom exception for an application-specific error.

## E06 — Imports, standard-library modules and script structure

**COURSE**
- [ ] Explain `import module` versus `from module import name`; avoid `import *`.
- [ ] Demonstrate useful standard-library examples (`math`, `random`, `statistics`, `datetime`) where relevant.
- [ ] Explain the module search path at a practical level.
- [ ] Introduce `if __name__ == "__main__":` and its role when a file is both executed and imported.
- [ ] Create a small separate `.py` module from Colab using `%%writefile`, then import it.
- [ ] Distinguish notebook cell execution order from ordinary module execution.

**EXERCISES**
- [ ] Standalone: use `math` and `statistics` to verify earlier manual calculations.
- [ ] Standalone: implement a reusable utility module and import its functions into another file.
- [ ] Debug: fix a shadowed standard-library module name or a function executed at import time.
- [ ] **Sensor Lab 8:** generate reproducible sample measurements with a fixed random seed (`EXTRA` for demonstration).

## E07 — Essentials integration milestone (`EXTRA`)
- [ ] Refactor the introductory mini-project into functions and at least one importable `.py` module.
- [ ] Add file persistence through `pathlib` and a `with` block where appropriate.
- [ ] Make invalid user input and missing files fail gracefully.
- [ ] Remove accidental aliases and replace manual index loops where idiomatic iteration is clearer.
- [ ] Provide a clean-kernel demonstration with a supplied sample-data folder.

---

# PART III — ADVANCED PYTHON [CORE]

**Exit target:** the learner can independently structure a small or medium Python project, understand common Python protocols and manage project dependencies.

## A01 — Comprehensions and unpacking

**COURSE**
- [ ] Explain list comprehensions: expression, iterable and optional filter.
- [ ] Explain dictionary and set comprehensions and appropriate use cases.
- [ ] Contrast comprehensions with explicit loops for readability.
- [ ] Explain tuple/list unpacking, starred unpacking (`first, *middle, last`) and argument unpacking (`*args`, `**kwargs`).
- [ ] Show unpacking in assignment, return values and parallel iteration.
- [ ] Discuss nested comprehensions, evaluation order and why deeply nested expressions are often harder to maintain.

**EXERCISES**
- [ ] Standalone: transform and filter a list of measurements in one comprehension.
- [ ] Standalone: build a word-length dictionary and a set of normalized words.
- [ ] Standalone: split a coordinate record into named variables using unpacking.
- [ ] Refactor: convert a verbose loop into a readable comprehension and justify one case kept as a loop.
- [ ] **Sensor Lab 9:** build a dictionary of timestamps → categorized measurements.

## A02 — Advanced collection patterns and `dataclasses`

**COURSE**
- [ ] Revisit nested dictionaries, dictionaries of lists and sets of unique identifiers.
- [ ] Show grouping and counting patterns; introduce `collections.Counter` and `defaultdict` as practical extensions (`EXTRA`).
- [ ] Introduce `@dataclass`, field annotations, autogenerated `__init__` and `__repr__`.
- [ ] Explain the role of `default_factory` for mutable fields.
- [ ] Compare a tuple, a dictionary, a dataclass and a full class for a record-like object.
- [ ] Explain how to convert simple dataclasses to serializable dictionaries as preparation for JSON.

**EXERCISES**
- [ ] Standalone: group fictional records by course or category.
- [ ] Standalone: create `Measurement` and `StudentRecord` dataclasses.
- [ ] Debug: fix shared mutable state caused by an incorrect field default.
- [ ] **Campus Toolkit 12:** migrate nested grade dictionaries to clear record structures.
- [ ] **Log Explorer 6:** represent parsed log entries as dataclasses with severity and timestamp fields.

## A03 — Modules, packages, project layout and dependencies

**COURSE**
- [ ] Create multiple `.py` modules and explain where import statements belong.
- [ ] Build a package directory and explain `__init__.py` at an introductory level.
- [ ] Separate business logic, user interface/CLI, data access and tests.
- [ ] Explain absolute versus relative imports and import errors.
- [ ] Demonstrate `pip` installation, upgrades and how to inspect installed packages.
- [ ] Explain virtual environments and create/activate/deactivate a `venv` **in a local-terminal companion guide**, rather than pretending Colab is a normal long-lived local environment.
- [ ] Introduce `pyproject.toml` and distinguish project metadata, dependencies and tool configuration.
- [ ] Show how to reproduce a project's environment and document basic startup steps.
- [ ] Explain Colab-specific `!pip install` and when runtime restart may be needed; clarify that notebook installs may be ephemeral.

**EXERCISES**
- [ ] Standalone: split an existing notebook solution into two imported modules.
- [ ] Standalone: create a tiny package with an executable entry point or `main.py`.
- [ ] Debug: resolve an import error and a missing dependency.
- [ ] **Campus Toolkit 13:** create `models.py`, `calculations.py`, `storage.py` and `main.py`.
- [ ] Bonus: document local setup in a README and add a small `pyproject.toml`.

## A04 — Object-Oriented Programming

**COURSE**
- [ ] Explain classes, instances, attributes, methods and `self`.
- [ ] Introduce `__init__`, instance state and basic method contracts.
- [ ] Distinguish instance attributes from class attributes.
- [ ] Show encapsulation by defining a clear public API and validating invariants.
- [ ] Teach composition before introducing simple inheritance and method overriding.
- [ ] Briefly explain polymorphism through different classes with the same public method.
- [ ] Compare an OOP solution with a function + dataclass solution to avoid using classes without a reason.

**EXERCISES**
- [ ] Standalone: build a `BankAccount`-style toy class with validation, or another non-financial stateful object.
- [ ] Standalone: design a `Sensor` instance that stores measurements and calculates summaries.
- [ ] Debug: fix a missing `self`, incorrect attribute access and shared class-level mutable state.
- [ ] **Campus Toolkit 14:** introduce `Course` and `Gradebook` objects; preserve file compatibility.
- [ ] Bonus: introduce a common report interface for console and file outputs.

## A05 — Iterables, iterators and generators

**COURSE**
- [ ] Explain `iter()` and `next()` and the iterable versus iterator distinction.
- [ ] Introduce `StopIteration` and the iterator protocol.
- [ ] Build a small custom iterable/iterator with `__iter__()` and `__next__()`.
- [ ] Explain `yield` and generator functions.
- [ ] Compare eager lists with lazy generators, especially for large files.
- [ ] Demonstrate generator expressions and one-shot exhaustion.

**EXERCISES**
- [ ] Standalone: create a countdown iterator.
- [ ] Standalone: write a generator that yields validated measurements from a text stream.
- [ ] Debug: explain why a generator produces no values the second time it is consumed.
- [ ] **Log Explorer 7:** stream log entries from files rather than loading all lines into memory.
- [ ] Bonus: combine generators in a small processing pipeline.

## A06 — Decorators and context managers

**COURSE**
- [ ] Explain functions as objects and a function nested inside another function.
- [ ] Introduce closures and the `@decorator` syntax with a simple wrapper.
- [ ] Explain `functools.wraps` and why wrapper metadata matters.
- [ ] Demonstrate a simple parameterized decorator as a bonus (`EXTRA`).
- [ ] Revisit `with` and explain the context-manager protocol (`__enter__`, `__exit__`).
- [ ] Introduce `contextlib.contextmanager` for a generator-based context manager.
- [ ] Compare decorators, context managers and ordinary helper functions: choose the simplest suitable tool.

**EXERCISES**
- [ ] Standalone: make a decorator that logs calls without changing return values.
- [ ] Standalone: write a context manager that prints or records acquisition/release messages.
- [ ] Debug: fix a decorator that drops `*args` / `**kwargs` or forgets to return its result.
- [ ] **Sensor Lab 10:** instrument processing functions with an optional timing decorator.
- [ ] Bonus: context manager for opening a group of related files safely.

## A07 — Type hints and the Python data model

**COURSE**
- [ ] Introduce parameter, return and variable annotations, including `list[int]`, `dict[str, float]` and `T | None` in a modern Python version.
- [ ] Explain that type hints are not automatically runtime validation.
- [ ] Introduce `typing` constructs only as needed (`Iterable`, `Iterator`, `Callable`, `Protocol` as an optional extension).
- [ ] Review useful dunder protocols: `__repr__`, `__str__`, `__len__`, `__iter__`, `__eq__` and, when appropriate, `__getitem__`.
- [ ] Connect `__enter__` / `__exit__` to the earlier context-manager lesson.
- [ ] Explain that operator or collection protocol overloading should preserve unsurprising behavior.
- [ ] Show a simple static type-checking demonstration as an optional local-workflow extension (`EXTRA`).

**EXERCISES**
- [ ] Standalone: annotate an existing utility module and identify an intentional annotation mismatch.
- [ ] Standalone: implement readable string representations for a custom record.
- [ ] Standalone: make a tiny custom collection usable with `len()` and iteration.
- [ ] Debug: fix an incorrectly designed `__eq__` or `__repr__` method.
- [ ] **Campus Toolkit 15:** add annotations and selected data-model methods to its public types.

## A08 — Advanced core capstone (`EXTRA`)
- [ ] Select one recurring project and package it as an independently runnable application.
- [ ] Organize it into modules/packages with a short README and reproducible dependencies.
- [ ] Include at least one dataclass or deliberately justified full class.
- [ ] Apply either a generator, a decorator or a custom context manager where it genuinely simplifies the design.
- [ ] Use type hints on the public functions and handle foreseeable file/input errors.
- [ ] Include a clean demonstration notebook that imports the project rather than reimplementing it in cells.
- [ ] Include a short design review: why these collections and abstractions, and what would change for a larger dataset?

---

# PART IV — INDEPENDENT SPECIALIZATION MODULES [OPTIONAL]

**Important:** the source syllabus describes these as independent modules that **do not have to be followed in sequence**. The mini-projects below are proposed connections, not additional compulsory syllabus chapters.

## S01 — Data Science: NumPy

**COURSE**
- [ ] Explain why homogeneous NumPy arrays differ from ordinary Python lists.
- [ ] Construct 1D and 2D arrays; inspect `shape`, `dtype` and dimensionality.
- [ ] Perform array indexing, slicing and Boolean masking.
- [ ] Demonstrate vectors, matrices and axis-aware reductions.
- [ ] Explain vectorized operations and basic broadcasting with visual examples.
- [ ] Compare a vectorized solution with a pure-Python loop on a modest dataset.

**EXERCISES**
- [ ] Standalone: convert and normalize an array of temperatures.
- [ ] Standalone: select columns/rows from a small matrix and compute summaries along each axis.
- [ ] Debug: identify a shape mismatch and unintended broadcasting.
- [ ] **Sensor Lab DS1:** load simulated readings into NumPy arrays and apply threshold masks.

## S02 — Data Science: pandas and importing datasets

**COURSE**
- [ ] Introduce `Series` and `DataFrame`, indexes, columns and basic dtypes.
- [ ] Import a supplied CSV dataset and inspect schema, dimensions and first rows.
- [ ] Demonstrate column selection, row filtering, Boolean masks and `.loc` / `.iloc`.
- [ ] Demonstrate transformations, derived columns, sorting and grouping/aggregation.
- [ ] Explain the difference between modifying a DataFrame and returning a transformed copy.

**EXERCISES**
- [ ] Standalone: filter a fictional course-results dataset by a specified condition.
- [ ] Standalone: group sensor measurements by date and compute daily summaries.
- [ ] Debug: correct a Boolean filter with missing parentheses or an index mismatch.
- [ ] **Sensor Lab DS2:** turn raw measurements into a tidy, documented DataFrame.

## S03 — Data Science: cleaning and quality

**COURSE**
- [ ] Identify missing values, duplicate rows, inconsistent labels and implausible numeric ranges.
- [ ] Explain type conversion and the difference between zero, an empty string and a missing value.
- [ ] Introduce explicit missing-data policies (drop, replace or retain with justification).
- [ ] Demonstrate duplicate handling, text normalization and basic outlier inspection.
- [ ] Track transformations and check their effects with simple validation assertions.

**EXERCISES**
- [ ] Standalone: clean a deliberately messy CSV file and report what changed.
- [ ] Standalone: detect invalid timestamps and inconsistent units.
- [ ] Debug: identify a silent data-quality error that distorts an average.
- [ ] **Sensor Lab DS3:** prepare a trustworthy sensor dataset and a one-page quality report.

## S04 — Data Science: Matplotlib and choosing representations

**COURSE**
- [ ] Create line, scatter, bar and histogram charts with Matplotlib.
- [ ] Explain which chart fits a time series, a distribution or a category comparison.
- [ ] Add useful titles, axis labels, legends and units.
- [ ] Discuss visual pitfalls: misleading axes, overplotting, missing data and inappropriate categorical scales.
- [ ] Export and display figures in Colab.

**EXERCISES**
- [ ] Standalone: choose the most suitable plot for three different small datasets and explain why.
- [ ] Debug: repair a misleading or unreadable chart.
- [ ] **Sensor Lab DS4:** generate a compact monitoring dashboard of readings over time, distributions and anomalies.

## S05 — Data Science: Exploratory Data Analysis

**COURSE**
- [ ] Define exploratory questions before computing statistics.
- [ ] Combine descriptive statistics, grouping, distributions and relationships between columns.
- [ ] Distinguish correlation from causation and identify sample/data limitations.
- [ ] Present a reproducible notebook narrative: question → cleaning → exploration → findings → limitations.

**EXERCISES**
- [ ] Standalone: investigate a small unknown dataset and propose three testable questions.
- [ ] **Sensor Lab DS5:** complete an end-to-end EDA notebook with five labeled findings and at least two limitations.
- [ ] Bonus: contrast outcomes before and after cleaning the same dataset.

## SC01 — Scientific Python: numerical computation with NumPy and SciPy

**COURSE**
- [ ] Review NumPy vectors/matrices and numerical precision concerns.
- [ ] Introduce the structure and documentation of SciPy and when it adds to NumPy.
- [ ] Explain floating-point approximation, tolerances and validation against a known result.

**EXERCISES**
- [ ] Standalone: compute a simple engineering formula on a vector of sample inputs.
- [ ] **Sensor Lab SC1:** represent calibrated sensor measurements and document units/tolerances.

## SC02 — Numerical integration and differentiation

**COURSE**
- [ ] Explain the idea behind numerical integration with an area approximation.
- [ ] Demonstrate a relevant SciPy integration routine and interpret its output.
- [ ] Introduce finite-difference derivatives and their sensitivity to the chosen step size.
- [ ] Compare a numerical estimate with an analytically known result.

**EXERCISES**
- [ ] Standalone: estimate distance traveled from sampled velocity values.
- [ ] Standalone: approximate the derivative of a known function and investigate step size.
- [ ] **Sensor Lab SC2:** estimate accumulated exposure or a rate of change from measurements.

## SC03 — Interpolation, optimization and solving equations

**COURSE**
- [ ] Explain interpolation between measured points and the limits of extrapolation.
- [ ] Demonstrate a basic interpolation method with SciPy.
- [ ] Introduce numerical root-finding and why initial conditions/bounds matter.
- [ ] Introduce optimization through an objective function and basic constraints.
- [ ] Teach result checking: units, bounds, solver success and sensitivity.

**EXERCISES**
- [ ] Standalone: interpolate gaps in a small measurement series.
- [ ] Standalone: numerically solve a simple physical equation with a known solution.
- [ ] Standalone: optimize a simple cost or efficiency function under stated constraints.
- [ ] **Sensor Lab SC3:** calibrate sensor parameters by minimizing error against reference readings.

## SC04 — Basic signal processing

**COURSE**
- [ ] Explain sampling rate, signal versus noise and basic visualization.
- [ ] Demonstrate moving averages and a simple SciPy filtering or peak-detection application.
- [ ] Discuss boundary effects, latency and the risk of losing meaningful signal features.

**EXERCISES**
- [ ] Standalone: recover a periodic pattern from a noisy simulated signal.
- [ ] **Sensor Lab SC4:** identify anomalous peaks and compare raw versus filtered sensor traces.

## CV01 — Computer Vision: images, pixels and color spaces

**COURSE**
- [ ] Explain how an image is represented as a height × width × channel array.
- [ ] Introduce grayscale versus RGB/BGR and basic color-channel interpretation.
- [ ] Inspect individual pixels and small image regions with NumPy.
- [ ] Display images correctly in Colab and explain OpenCV's BGR convention.

**EXERCISES**
- [ ] Standalone: inspect pixel values and compute a simple color statistic.
- [ ] Debug: correct a color-space mistake that makes a displayed image look wrong.
- [ ] Mini-project **Image Lab 1:** generate a simple synthetic image and annotate shapes and colors.

## CV02 — NumPy image manipulation and OpenCV

**COURSE**
- [ ] Load, display and save images with OpenCV (using supplied permissively licensed/synthetic inputs).
- [ ] Crop, resize, rotate and flip image arrays.
- [ ] Explain coordinate order, image bounds and interpolation at a practical level.

**EXERCISES**
- [ ] Standalone: build a small image contact sheet from cropped regions.
- [ ] Mini-project **Image Lab 2:** implement a repeatable image-preparation pipeline.

## CV03 — Image transformations and filtering

**COURSE**
- [ ] Demonstrate grayscale conversion, thresholding and simple contrast adjustments.
- [ ] Introduce blur, smoothing and edge-enhancing filters.
- [ ] Compare results on a noisy synthetic image and explain trade-offs.

**EXERCISES**
- [ ] Standalone: find a threshold that separates dark objects from a bright background.
- [ ] Mini-project **Image Lab 3:** detect and count simple synthetic shapes after preprocessing.

## CV04 — Feature and object detection fundamentals

**COURSE**
- [ ] Introduce contours, corners or another classical feature concept.
- [ ] Demonstrate a simple OpenCV feature/object detection pipeline and its failure modes.
- [ ] Distinguish image processing, classical feature detection and learned models without promising ML coverage that is absent from the source syllabus.

**EXERCISES**
- [ ] Standalone: detect simple shapes or corners in a controlled sample image.
- [ ] Mini-project **Image Lab 4:** evaluate the pipeline against at least three deliberately difficult images.

## GUI01 — Event-driven programming, windows and widgets

**Environment note:** this is a **local-desktop practical**, not a native Colab GUI project. Colab can host explanatory material and pure logic, but a PySide/Qt event loop and window should run on students' computers.

**COURSE**
- [ ] Contrast sequential programs with event-driven applications.
- [ ] Introduce windows, labels, buttons, text fields and simple layouts in PySide/Qt (or an equivalent library).
- [ ] Explain event loops, signals and slots/callbacks.
- [ ] Demonstrate input validation and basic UI feedback.

**EXERCISES**
- [ ] Standalone: build a small local unit-conversion window.
- [ ] Debug: fix a widget whose callback is never connected or whose value is converted incorrectly.

## GUI02 — Connect a GUI to an existing Python program

**COURSE**
- [ ] Explain separation between UI code and tested/reusable application logic.
- [ ] Connect buttons and input controls to existing functions.
- [ ] Display success and error messages without crashing the window.

**EXERCISES**
- [ ] **Campus Toolkit GUI1:** wrap the gradebook in a simple desktop interface.
- [ ] Bonus: show a small Matplotlib chart inside an appropriate Qt widget.

## GUI03 — Simple desktop application integration

- [ ] Add file open/save operations and confirm overwrite behavior.
- [ ] Handle empty input and unavailable files.
- [ ] Package the deliverable with a local setup guide and screenshots in the Colab handout.
- [ ] Bonus: choose an alternative GUI framework and briefly justify the trade-offs.

## API01 — JSON and HTTP fundamentals

**COURSE**
- [ ] Explain structured data and map Python lists/dictionaries to JSON arrays/objects.
- [ ] Demonstrate `json.loads()`, `json.dumps()` and reading/writing JSON files.
- [ ] Explain HTTP requests, responses, URLs, headers and payloads.
- [ ] Explain REST as an API design style without presenting it as a strict protocol.
- [ ] Introduce `GET`, `POST`, and the purposes of common additional methods (`PUT`, `PATCH`, `DELETE`).
- [ ] Cover common status-code groups and representative codes (200, 201, 400, 401, 404, 429, 500).

**EXERCISES**
- [ ] Standalone: convert a fictional gradebook or sensor record to JSON and back.
- [ ] Standalone: inspect three mock HTTP responses and choose appropriate handling.
- [ ] Debug: fix a JSON serialization error or an incorrect assumption about a response body.

## API02 — Using external APIs from Python

**COURSE**
- [ ] Make a `GET` request using a Python HTTP library such as `requests`.
- [ ] Explain status validation, timeouts, expected JSON structure and API errors.
- [ ] Demonstrate a `POST` request against a safe test/mock endpoint; discuss idempotency at a practical level as a bonus.
- [ ] Explain pagination, rate limits and avoiding hardcoded API secrets (`EXTRA` operational concerns).
- [ ] Provide deterministic local/mock responses for students with unreliable internet access.

**EXERCISES**
- [ ] Standalone: retrieve a small public dataset and extract relevant fields.
- [ ] Debug: handle non-JSON responses, timeouts and unexpected status codes.
- [ ] **Sensor Lab API1:** retrieve measurements from an endpoint or supplied mock JSON responses.

## API03 — API integration challenge

- [ ] Build a mini client that supports at least one `GET` and one safe mock `POST` operation.
- [ ] Parse structured responses into a dataclass or documented dictionary shape.
- [ ] Handle at least three failure cases and demonstrate a graceful fallback to a local sample file.
- [ ] Bonus: paginate through several mock result pages.

## T01 — Why testing matters, assertions and test cases

**COURSE**
- [ ] Explain the difference between running an example and verifying an expected result.
- [ ] Introduce assertion statements and the idea of an independent expected value.
- [ ] Define normal cases, boundary cases, invalid inputs and regression cases.
- [ ] Explain test isolation and deterministic test data.
- [ ] Introduce the arrange → act → assert structure.

**EXERCISES**
- [ ] Standalone: write at least five test cases for `mean_measurement()` or another existing function.
- [ ] Debug: identify a test that passes without meaningfully checking its result.

## T02 — Unit testing with `pytest`

**COURSE**
- [ ] Introduce `pytest` test file/function naming and the command to run tests.
- [ ] Demonstrate parametrized tests, exception assertions and fixtures where appropriate.
- [ ] Show how to isolate file operations using a temporary directory.
- [ ] Explain clean test runs in Colab versus a local terminal/CI environment.

**EXERCISES**
- [ ] Standalone: turn earlier inline assertions into a small `pytest` suite.
- [ ] Standalone: test malformed input and a missing-file exception.
- [ ] **Campus Toolkit T1:** cover the grading and storage modules with representative tests.

## T03 — Edge cases and regression testing

**COURSE**
- [ ] Demonstrate how a reported bug becomes a regression test.
- [ ] Explain what test coverage can and cannot demonstrate; introduce basic coverage measurement as an optional extension (`EXTRA`).
- [ ] Briefly connect the tests to an automated repository workflow (`EXTRA`, since the source syllabus specifies regression testing but not CI).

**EXERCISES**
- [ ] Intentionally introduce a bug in a working module, reproduce it, fix it, and retain the test.
- [ ] **Log Explorer T1:** test empty logs, malformed lines, duplicate entries and Unicode messages.

## P01 — Execution time and memory measurement

**COURSE**
- [ ] Explain why single-run timings can be misleading.
- [ ] Demonstrate `time.perf_counter()` and `timeit` with repeatable examples.
- [ ] Introduce `tracemalloc` or another suitable way to inspect Python memory allocation.
- [ ] Explain the impact of input size, warm-up and the measurement environment.

**EXERCISES**
- [ ] Standalone: measure two implementations of a simple data-transformation task.
- [ ] **Log Explorer P1:** compare reading an entire file with a line-by-line approach.

## P02 — Profiling and bottlenecks

**COURSE**
- [ ] Use `cProfile` or an equivalent profiler to locate costly functions.
- [ ] Show how to interpret call counts and cumulative time.
- [ ] Distinguish a measured bottleneck from an intuitively suspicious section.

**EXERCISES**
- [ ] Standalone: profile deliberately slow sample code and identify the dominant cost.
- [ ] **Sensor Lab P1:** profile the data-cleaning pipeline and record a baseline.

## P03 — Algorithmic optimization and comparison

**COURSE**
- [ ] Revisit asymptotic complexity for one-pass, nested-loop and dictionary-based operations.
- [ ] Compare changes to algorithms with lower-level Python refactoring and vectorization.
- [ ] Explain performance/readability/memory trade-offs and verify result equivalence after optimization.

**EXERCISES**
- [ ] Standalone: improve a repeated membership search using a set when appropriate.
- [ ] **Log Explorer P2:** propose, implement and measure one optimization; show timing and memory before/after.
- [ ] Bonus: compare a pure-Python numerical loop against NumPy vectorization on suitably sized data.

## AS01 — Synchronous versus asynchronous execution

**COURSE**
- [ ] Explain blocking versus non-blocking waits through a timeline of independent tasks.
- [ ] Explain typical async use cases (e.g., multiple network requests) and when CPU-heavy work does *not* automatically become faster.
- [ ] Introduce coroutines, `async def`, `await` and event loops.
- [ ] Clarify Colab/Jupyter's existing event-loop behavior versus `asyncio.run()` in a standalone script.

**EXERCISES**
- [ ] Standalone: compare three simulated blocking sleeps with concurrent async sleeps.
- [ ] Debug: explain a coroutine that was created but never awaited.

## AS02 — `asyncio` and coordinating coroutines

**COURSE**
- [ ] Demonstrate scheduling multiple coroutines with `asyncio.gather()` or current equivalent patterns.
- [ ] Explain task results, exception propagation, cancellation and timeout basics.
- [ ] Show an appropriate concurrency limit for external API use (`EXTRA` operational practice).

**EXERCISES**
- [ ] Standalone: asynchronously request multiple *mock* data sources with controlled delays.
- [ ] Debug: repair a blocking operation mistakenly used inside an async coroutine.

## AS03 — Asynchronous mini-project

- [ ] **Sensor Lab AS1 / Log Explorer AS1:** fetch or simulate multiple independent data feeds concurrently.
- [ ] Compare wall-clock times against a sequential baseline without claiming CPU parallelism.
- [ ] Handle one failed feed and one timeout while retaining successful results.
- [ ] Bonus: connect the asynchronous client to the earlier JSON/API module.

---

# PART V — COMPREHENSIVE COVERAGE & RELEASE CHECKS

## Syllabus crosswalk

Use the following as a **final audit** of every source-syllabus topic. The chapter IDs above show where to find the work. `EXTRA` milestones and suggestions are not implied by the syllabus.

### Introduction to Programming & Algorithms
- [ ] Variables, values, types and operators — **F01**
- [ ] Interactive programs and user input — **F01, F02, F03**
- [ ] Conditions and control flow — **F02**
- [ ] `for` and `while` loops — **F03**
- [ ] Functions and program decomposition — **F04**
- [ ] Strings and text manipulation — **F05**
- [ ] Lists — **F06**
- [ ] Tuples — **F07**
- [ ] Dictionaries — **F07**
- [ ] Sets — **F07**
- [ ] Basic algorithms and problem solving — **F08**

### Python Essentials
- [ ] Names, references and objects — **E01**
- [ ] Mutable and immutable objects — **E01**
- [ ] Identity and aliasing — **E01**
- [ ] `range()` — **F03, E02**
- [ ] `enumerate()` — **E02**
- [ ] `zip()` — **E02**
- [ ] Membership — **F05–F07, E02**
- [ ] `any()` — **E02**
- [ ] `all()` — **E02**
- [ ] `pathlib` — **E04**
- [ ] `with` — **E04**
- [ ] Exceptions and error handling — **E05**
- [ ] `sorted()` — **E03**
- [ ] `reversed()` — **E03**
- [ ] `min()` / `max()` — **E03**
- [ ] `sum()` — **E03**
- [ ] `map()` and other useful built-ins — **E03**
- [ ] Imports and modules — **E06**

### Advanced Python
- [ ] List comprehensions — **A01**
- [ ] Dictionary comprehensions — **A01**
- [ ] Set comprehensions — **A01**
- [ ] Unpacking — **A01**
- [ ] Advanced collection patterns — **A02**
- [ ] `dataclasses` — **A02**
- [ ] Creating/importing own modules — **A03**
- [ ] Packages — **A03**
- [ ] Project organization — **A03, A08**
- [ ] `pip` — **A03**
- [ ] Virtual environments / `venv` — **A03**, local guide
- [ ] `pyproject.toml` — **A03**
- [ ] Object-Oriented Programming — **A04**
- [ ] Iterables and iterators — **A05**
- [ ] Generators — **A05**
- [ ] Decorators — **A06**
- [ ] Context managers — **A06**
- [ ] Type hints — **A07**
- [ ] Python data model / dunder protocols — **A07**

### Data Science
- [ ] NumPy numerical arrays, vectors/matrices, vectorized operations — **S01**
- [ ] pandas Series/DataFrame, dataset import, filtering/transformations — **S02**
- [ ] Data cleaning and data quality — **S03**
- [ ] Matplotlib, visualization and appropriate chart choices — **S04**
- [ ] Exploratory Data Analysis — **S05**

### Scientific Python
- [ ] NumPy numerical computation and SciPy — **SC01**
- [ ] Numerical integration — **SC02**
- [ ] Numerical differentiation — **SC02**
- [ ] Interpolation — **SC03**
- [ ] Optimization — **SC03**
- [ ] Solving equations — **SC03**
- [ ] Basic signal-processing applications — **SC04**

### Computer Vision
- [ ] Image representation — **CV01**
- [ ] Pixels, channels and color spaces — **CV01**
- [ ] NumPy image manipulation — **CV01–CV02**
- [ ] OpenCV — **CV02–CV04**
- [ ] Image transformations — **CV02–CV03**
- [ ] Filtering — **CV03**
- [ ] Feature and object detection fundamentals — **CV04**

### Graphical User Interfaces
- [ ] Event-driven programming — **GUI01**
- [ ] Windows and widgets — **GUI01**
- [ ] User interaction — **GUI01–GUI02**
- [ ] Connecting interfaces to existing Python programs — **GUI02**
- [ ] Building simple desktop applications — **GUI03**

### APIs & Structured Data
- [ ] JSON — **API01**
- [ ] HTTP fundamentals — **API01**
- [ ] REST APIs — **API01**
- [ ] Requests and responses — **API01–API02**
- [ ] `GET`, `POST` and other HTTP methods — **API01–API02**
- [ ] Status codes — **API01**
- [ ] Using external APIs from Python — **API02–API03**

### Testing
- [ ] Why software testing matters — **T01**
- [ ] Unit testing — **T01–T02**
- [ ] Assertions — **T01**
- [ ] `pytest` — **T02**
- [ ] Test cases — **T01–T02**
- [ ] Edge cases — **T01, T03**
- [ ] Regression testing — **T03**

### Performance & Profiling
- [ ] Measuring execution time — **P01**
- [ ] Measuring memory usage — **P01**
- [ ] Profiling Python programs — **P02**
- [ ] Identifying bottlenecks — **P02**
- [ ] Algorithmic optimization — **P03**
- [ ] Comparing different implementations — **P01, P03**

### Asynchronous Programming
- [ ] Synchronous versus asynchronous execution — **AS01**
- [ ] `async` — **AS01**
- [ ] `await` — **AS01**
- [ ] Coroutines — **AS01**
- [ ] Event loops — **AS01**
- [ ] `asyncio` — **AS02**
- [ ] Typical asynchronous use cases — **AS01–AS03**

## Whole-course release checklist
- [ ] Every source-syllabus item above is linked to at least one **COURSE** explanation and one runnable example.
- [ ] Every source-syllabus item has practice: a short task, a synthesis task or a milestone appropriate to its complexity.
- [ ] Each core section ends with an integration exercise that reuses concepts from earlier chapters.
- [ ] Beginner prerequisites remain explicit; bonuses do not become hidden mandatory dependencies.
- [ ] Sample data, file paths, URLs and images work in a fresh Colab runtime; non-Colab lessons have local instructions.
- [ ] Notebook cells execute top to bottom in a clean session unless they are clearly labeled as independent/error-demonstration examples.
- [ ] Teacher correction notebooks are separate from student notebooks.
- [ ] The syllabus and repository README match the material that has actually been published.

---

## When you have only 30–60 minutes to work (`EXTRA` workflow)

- [ ] Pick **one unchecked COURSE concept** and write its explanation plus one minimal runnable example.
- [ ] Add a deliberately tricky input and explain why the first implementation needs improvement.
- [ ] Write **one standalone exercise** and **one continuation milestone** for the same concept.
- [ ] Add example inputs/outputs, one edge case and a correction note.
- [ ] Run the cells in a fresh session, commit the chapter and tick its checklist boxes.

**Practical order:** finish the core fundamentals first; finish Python Essentials next; use Testing in parallel as an *optional practice habit*, while still keeping its full dedicated specialization module; then build Advanced Python and choose whichever specializations match the class.
