# SYLLABUS

This syllabus presents the topics covered by these Python course materials.

The content is designed as a progressive learning path, starting from **complete programming fundamentals** and gradually introducing more advanced Python concepts and optional specialization modules.

> [!NOTE]
> Not every chapter has been completed yet:
>
> * `[x]` — Course material is available
> * `[ ]` — Course material is planned or currently being developed

---

# Learning Path

These course materials were designed primarily for engineering-school students, but the first chapters require **no previous programming experience**.

The curriculum is divided into several levels.

---

## Introduction to Programming & Algorithms

The first part introduces programming from the ground up using Python.

Topics include:

* Variables, values, types and operators
* Interactive programs and user input
* Conditions and control flow
* `for` and `while` loops
* Functions and program decomposition
* Strings and text manipulation
* Collections:

  * lists
  * tuples
  * dictionaries
  * sets
* Basic algorithms and problem solving

The objective is to become comfortable translating a simple problem into a working program.

---

## Python Essentials

Once the programming fundamentals are understood, the course focuses more specifically on **how Python works**.

Topics include:

* Names, references and objects
* Mutable and immutable objects
* Identity and aliasing
* Pythonic iteration:

  * `range()`
  * `enumerate()`
  * `zip()`
  * membership
  * `any()`
  * `all()`
* File handling with `pathlib`
* Context management with `with`
* Exceptions and error handling
* Useful built-in functions:

  * `sorted()`
  * `reversed()`
  * `min()` / `max()`
  * `sum()`
  * `map()`
  * and others
* Imports and modules

The objective is to move from simply **writing programs in Python** to understanding and using Python properly.

---

## Advanced Python

This part introduces techniques useful for larger and more structured Python projects.

Topics include:

* Comprehensions

  * lists
  * dictionaries
  * sets
* Unpacking
* Advanced collection patterns
* `dataclasses` as lightweight data structures
* Creating and importing your own modules
* Packages
* Project organization
* Dependency management

  * `pip`
  * virtual environments
  * `venv`
  * `pyproject.toml`
* Object-Oriented Programming
* Iterables and iterators
* Generators
* Decorators
* Context managers
* Type hints
* Python data-model / dunder protocols

The objective is to become capable of designing and organizing complete Python projects independently.

---

# Specialization Modules

Once the core Python curriculum is understood, independent modules can introduce different practical applications of Python.

These modules do **not necessarily need to be followed in order**.

## Data Science

* NumPy

  * numerical arrays
  * vectors and matrices
  * vectorized operations
* pandas

  * `Series`
  * `DataFrame`
  * importing datasets
  * filtering and transformations
* Data cleaning and data quality
* Matplotlib

  * data visualization
  * choosing appropriate representations
* Exploratory Data Analysis

---

## Scientific Python

Possible applications linked to engineering studies:

* NumPy for numerical computation
* SciPy
* Numerical integration
* Numerical differentiation
* Interpolation
* Optimization
* Solving equations
* Basic signal-processing applications

---

## Computer Vision

* Image representation
* Pixels, channels and color spaces
* NumPy image manipulation
* OpenCV
* Image transformations
* Filtering
* Feature and object detection fundamentals

---

## Graphical User Interfaces

* Event-driven programming
* Windows and widgets
* User interaction
* Connecting interfaces to existing Python programs
* Building simple desktop applications

Possible frameworks may include **PySide / Qt** or similar Python GUI libraries.

---

## APIs & Structured Data

* JSON
* HTTP fundamentals
* REST APIs
* Requests and responses
* `GET`, `POST`, and other HTTP methods
* Status codes
* Using external APIs from Python

---

## Testing

* Why software testing matters
* Unit testing
* Assertions
* `pytest`
* Test cases
* Edge cases
* Regression testing

---

## Performance & Profiling

* Measuring execution time
* Measuring memory usage
* Profiling Python programs
* Identifying bottlenecks
* Algorithmic optimization
* Comparing different implementations

---

## Asynchronous Programming

* Synchronous vs asynchronous execution
* `async`
* `await`
* Coroutines
* Event loops
* `asyncio`
* Typical asynchronous use cases

---

# Learning Outcome

Following the complete core curriculum should provide enough Python knowledge to work autonomously on **small to medium-sized projects**, understand unfamiliar Python code, use external libraries and documentation, and continue learning more specialized Python technologies independently.

The specialization modules can then be used to adapt the curriculum to different courses, engineering fields and student interests.
