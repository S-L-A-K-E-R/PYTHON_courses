# Advanced Python — Applied Python Lab

**Semester plan:** 20 hours remaining · 10 × 2-hour sessions  
**Audience:** Students with previous C/programming experience, already taking a separate machine-learning course  
**Environment:** Primarily Google Colab/Jupyter, including hands-on scientific computing with SciPy.  
**Approach:** About 20 minutes of explanation, 90 minutes of guided experimentation, and 10 minutes of review per session. The first session has a longer recap. 

<br>

## Learning outcomes

By the end of the semester, students should be able to write idiomatic Python, choose appropriate tools for working with data and images, understand the practical uses of basic OOP, use an HTTP API, apply introductory SciPy techniques, and build and explain a small reusable application or analysis notebook. This course **does not teach machine learning**, which is covered separately.

<br>

## Ten-session syllabus

| # | Subject | Concepts in the short course | Applied lab |
|---|---|---|---|
| 1 | **Python crash course** | Direct iteration (`for item in items`), conditions, collections, strings, functions, files, comprehensions, `enumerate`, `zip`, and mutability pitfalls | Short Python challenges; launch the two-part homework |
| 2 | **NumPy** | Arrays versus lists, dimensions, slicing, masks, vectorized operations | Explore and transform simulated sensor readings |
| 3 | **pandas and data cleaning** | CSV import, DataFrames, filtering, missing data, grouping | Clean a deliberately imperfect dataset and document the corrections |
| 4 | **Matplotlib and exploration** | Line/scatter/bar/histogram plots, labeling, simple descriptive statistics | Produce a small data-exploration notebook from the cleaned dataset |
| 5 | **Practical OOP** | Class/instance, `self`, `__init__`, attributes and methods; composition; brief `@dataclass` introduction | Build a `SensorSeries` class; compare it with functions + data |
| 6 | **Computer Vision I** | Images as arrays, pixels, RGB/BGR, crop/resize/rotate, OpenCV | Create an image-manipulation notebook using provided images |
| 7 | **Computer Vision II** | Grayscale, smoothing, thresholding, edges and contours | Count simple objects in synthetic images and explain failure cases |
| 8 | **JSON and APIs** | `json`, HTTP GET, `requests`, timeouts, status codes, expected schema | Retrieve data from an API or provided offline response; turn it into a table or plot |
| 9 | **SciPy introduction** | Scientific computing, interpolation, basic signal processing and useful numerical routines | Analyze simulated sensor data: interpolate missing readings and detect peaks |
| 10 | **Mini-project studio** | Integration, testing, documentation and presenting findings | Finish and demonstrate a chosen Data / Vision / API+SciPy project |

<br>

**Flexibility:** After Session 1, poll students on Data, Vision, APIs and scientific computing. Keep Sessions 2–4 as a practical common foundation unless their ML course already covers those exact skills. Session 9 introduces SciPy through a manageable notebook lab; its emphasis may shift between interpolation and signal processing to suit student interest. Session 10 may double as final project work rather than a formal presentation session.

<br>

## Session 1: one class, two homework releases

Use **45 minutes** for a Python-versus-C refresher and Pythonic idioms, **65 minutes** for compact coding challenges, and **10 minutes** to launch the homework. Give students a one-page syntax cheat sheet and short optional pre-reading rather than reteaching introductory algorithms.

<br>

### Homework: Log Explorer (one evolving project, 4–6 hours total)

**Part A — release after Session 1; target completion before Session 2.** Supply a list of structured, fictional events. Ask students to count INFO/WARNING/ERROR messages, filter by severity, summarize frequencies and identify the most frequent event. Focus on direct iteration, conditions, strings, lists and dictionaries. Include empty-input and tie-handling requirements.

**Part B — release after Session 2; final submission before Session 3.** Give the same events as a messy UTF-8 text file. Require `str.strip`, `split` (including a maximum split), several focused functions, file loading through `pathlib` or `with open`, clear malformed-line handling, a saved report and at least five meaningful assertions. Add an optional bonus for multi-file support or an analysis plot.

Use **one final submission** for the two-part homework. Provide sample inputs and a few self-checking tests to reduce correction time. Avoid using actual student data.

<br>

### Essential one-page cheat sheet

I can get some inspirations on the [cheatsheet](https://cheatsheets.zip/python) website.


- Iteration: `for item in items:`, `for i, item in enumerate(items):`, `for x, y in zip(xs, ys):`; use `range(n)` when indices or counts are needed.
- Decisions: `if` / `elif` / `else`, `in`, chained comparisons, `and` / `or` / `not`.
- Collections: list indexing/slicing, `append`, dictionary `.get`, sets, `sorted`, `sum`, `min`, `max`, comprehensions.
- Strings: `.strip()`, `.lower()`, `.split()`, `.join()`, `.replace()`, f-strings.
- Files: `Path(path).read_text(encoding="utf-8")`, `.splitlines()`, `with open(..., encoding="utf-8")`.
- Functions: `def`, parameters, `return`, type annotations where useful, `assert` for simple verification.
- Pitfalls: `=` versus `==`, `is None`, mutable aliasing, accidental notebook state, empty inputs and exceptions.

<br>

## OOP: one practical session, not an inheritance course

OOP is useful for reading and working with Python libraries and for programs that genuinely need state. It is **not** required for every Python project. Compare a `SensorSeries` class with a plain list and a few functions; explain when each is clearer. Teach `self`, instance state, methods and composition; mention inheritance only as a brief example or bonus. The deliverable is one small working class, not a large class hierarchy.

*(NOTE2SELF: I don't think I want to use a library to show them OOP? How about making ourselves the interface, and so on?)*

<br>

## Project options


Students choose one small project, 3 people together: **Data** (clean and visualize a dataset), **Vision** (an image-processing pipeline with a documented failure case), or **API + SciPy** (fetch/mock sensor data, then interpolate or analyze the measurements). Reuse lab work rather than beginning from zero. One clear notebook, a few assertions and a short live demo or written reflection are sufficient.

*(NOTE2SELF: not sure yet, in decision for this one. I might go with Vision only)*