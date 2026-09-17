Yes — and I think the direction you’re describing is much stronger than starting an “Advanced Python” course with NumPy/Pandas/FastAPI/asyncio and hoping students somehow become good Python programmers along the way. 😄

Because they already know **C + algorithms up to dynamic allocation**, you have a particularly nice opportunity: teach Python as a **different programming model**, not merely “C with fewer semicolons.”

## 1. The course philosophy I would use

I’d structure the beginning around:

> **“You already know how to program. Now we're going to learn how Python wants you to program.”**

So I would *not* spend three weeks teaching:

```python
print()
if
while
for
```

as though they had never programmed.

Instead:

```text
C concept
    ↓
Python equivalent
    ↓
Wait — Python behaves differently here!
    ↓
Why?
    ↓
Pythonic solution
```

And the things you've encountered in Advent of Code are **excellent teaching material** for precisely this.

Python's official documentation itself separates mutable objects such as lists/dictionaries from immutable objects such as strings/tuples, and describes variables essentially as names referring to objects rather than boxes containing values. ([Python documentation][1])

That should almost be the central theme of the first part of your course.

---

# 2. What coding environment would I use?

For *your* course, I would use a **hybrid setup**, but with one clear primary environment.

### My preferred stack

| Purpose                    | Tool                      |
| -------------------------- | ------------------------- |
| Main programming           | **VS Code**               |
| Python                     | **Python 3.14.x**         |
| Environment / dependencies | **uv**                    |
| Exercises                  | `.py` files + README      |
| Testing                    | **pytest**                |
| Version control            | Git + GitHub              |
| Interactive demonstrations | Jupyter / Colab           |
| Submission/autograding     | Classroom 50 or CodeGrade |
| Tiny browser experiments   | JupyterLite               |

VS Code's current Python tooling already integrates interpreters, environments, debugging, testing and Jupyter notebooks, which makes it a very good environment to grow from simple scripts into actual Python projects. ([Visual Studio Code][2])

And I'd personally prefer **VS Code over Colab as the default environment**.

Why?

Because this is *Advanced Python*, not *Data Science with Python*.

I want them eventually seeing:

```text
my_project/
├── src/
├── tests/
├── README.md
├── pyproject.toml
└── .venv/
```

rather than:

```text
AdvancedPythonTP7_final_FINAL_2.ipynb
```

😆

---

# 3. I would still keep Google Colab

Colab is still excellent for some lessons. It's hosted, requires effectively no setup, and Google explicitly positions it for education as well as ML/data science. ([Google Research][3])

But I'd use it for things like:

> “Run these six cells. Predict the result before executing.”

For example:

```python
a = [1, 2]
b = a
b.append(3)

print(a)
```

Then:

```python
a = "hello"
b = a
b += "!"

print(a)
print(b)
```

That kind of experiment works **wonderfully in notebooks**.

Then the real lab goes back to `.py`.

So:

**Notebook = laboratory bench.**
**`.py` project = actual programming.**

I like that distinction a lot pedagogically.

---

# 4. There's also JupyterLite now

This one might interest you.

**JupyterLite** runs Jupyter **entirely inside the browser**. There's no Python server behind it; Python kernels such as Pyodide execute client-side. ([jupyterlite.readthedocs.io][4])

That means you could theoretically host:

```text
ece-python.example.com
```

and students immediately get exercises without installing anything.

It's fantastic for:

* first-session exercises;
* demonstrations;
* little quizzes;
* manipulating lists/dicts/strings;
* algorithms;
* emergency “my Python installation died” situations.

But I wouldn't make it the main environment because not everything available in ordinary CPython/Jupyter works in JupyterLite. ([jupyterlite.readthedocs.io][4])

---

# 5. JupyterHub is interesting for your class size

If ECE ever gives you some server infrastructure, this is another possibility.

JupyterHub gives each user their own Jupyter environment, and the Jupyter project explicitly presents it as useful for classes. ([JupyterHub][5])

For **15–20 students**, that's completely reasonable.

The advantage is:

> “Everybody has exactly the environment I configured.”

The disadvantage:

> “Congratulations Simon, you're now also the system administrator.” 😂

Unless ECE IT maintains it, I'd probably avoid creating that extra job for yourself.

---

# 6. `uv` is something I seriously think you should consider teaching

This is one of the “newer Python ecosystem” tools I'd introduce.

Instead of immediately throwing:

```bash
python -m venv .venv
pip install ...
pip freeze > requirements.txt
```

at them, **uv** gives you Python version management, virtual environments, dependencies and lock files within one workflow. Current `uv` supports Windows, Linux and macOS and can automatically maintain a project-local `.venv`. ([Astral Docs][6])

A later project could therefore simply have:

```text
pyproject.toml
uv.lock
.python-version
```

and everybody gets the same environment.

That is genuinely useful modern Python knowledge rather than “advanced library of the week.”

I wouldn't introduce it on Session 1, though.

Maybe around **Session 6–7**, once external dependencies finally appear.

---

# 7. Homework management: one IMPORTANT 2026 change

I was originally about to recommend **GitHub Classroom** for you.

Don't.

GitHub Classroom was officially decommissioned on **August 28, 2026**. ([The GitHub Blog][7])

Rather hilariously, we're discussing your rentrée about **six days after its death**.

GitHub is instead pointing educators toward partner solutions including **Codio** and the Fifty Foundation's **Classroom 50**. ([GitHub][8])

### Classroom 50 looks particularly interesting for you

It was released this summer as a **free/open-source replacement for GitHub Classroom** and supports GitHub assignments, submissions and automated correctness tests. ([GitHub][9])

That matches your philosophy fairly well:

```text
Git repository
      ↓
student commits
      ↓
submission
      ↓
tests
      ↓
teacher review
```

### CodeGrade is another candidate

CodeGrade currently offers GitHub integration where pushes can become submissions and trigger automated tests. Its current free tier is advertised for classes of up to **50 students**, so your 15–20 students fit comfortably. ([codegrade.com][10])

I'd test **Classroom 50 first**, personally.

It's closer to the developer workflow you already use.

---

# 8. Now, the syllabus

Here's how I'd build it.

Rather than calling the first chapter:

> INTRODUCTION TO PYTHON

I'd call it something like:

# Part I — From C to Python

And deliberately exploit their existing knowledge.

---

## Module 0 — “You already know programming”

### Goal

Get them coding immediately and find out what they remember.

Topics:

* Python installation / interpreter;
* REPL;
* running `.py`;
* indentation;
* comments;
* variables;
* `print`;
* `input`;
* basic arithmetic;
* `if`;
* `while`;
* basic `for`.

But extremely quickly.

### Lab

Give them a tiny C program they've previously encountered.

For example:

```text
Ask for N numbers
Compute:
- minimum
- maximum
- average
```

Task:

> Rewrite it in Python **without learning any fancy Python yet**.

Let them naturally produce terrible C-shaped Python.

That's useful.

You *want*:

```python
for i in range(len(values)):
```

at this stage.

Because three lessons later you'll show them why they usually don't need it.

---

# Module 1 — Variables aren't C variables

This is where I'd really begin teaching Python.

## C intuition

```c
int x = 5;
```

Students mentally see:

```text
x
┌───┐
│ 5 │
└───┘
```

### Python mental model

Teach:

```python
x = 5
```

closer to:

```text
x ─────► object 5
```

Then:

```python
y = x
```

is another binding.

This becomes critical with:

```python
x = [1, 2]
y = x

y.append(3)
```

Python's own FAQ uses essentially this example: assignment does not copy the list; both names refer to the same mutable object. ([Python documentation][11])

### Concepts

* objects;
* names;
* references;
* identity;
* `id()`;
* `is`;
* `==`;
* aliasing;
* mutable vs immutable.

This is IMO **the perfect continuation after malloc/calloc**.

Instead of:

> “Here is Python syntax.”

you're saying:

> “Last semester we manually controlled memory. What happens when the language manages objects for us?”

Much more intellectually satisfying.

---

# Module 2 — Strings are NOT `char[]`

Your AoC observation goes directly here.

Python strings are immutable and Python doesn't actually have a separate `char` type; indexing a string gives another string of length 1. ([Python documentation][1])

So:

```python
word = "hello"
word[0] = "H"
```

❌

Instead:

```python
word = "H" + word[1:]
```

or appropriate string operations.

### Teach

* indexing;
* negative indexing;
* slicing;
* immutability;
* Unicode;
* `ord()`;
* `chr()`;
* `split`;
* `join`;
* `replace`;
* membership.

Your AoC password problem could inspire a great exercise here without literally using the AoC problem.

### Exercise

**Robot serial-number editor**

Input:

```text
RBT-X392-A
```

Students must:

* extract sections;
* validate characters;
* increment letters;
* rebuild strings.

It forces them to abandon `char[]` thinking.

---

# Module 3 — Python containers

This would be one of the biggest modules.

Introduce:

```python
list
tuple
dict
set
```

not just as syntax, but as **choosing the correct data structure**.

Python's built-in data structures already provide rich operations such as membership tests, comprehensions, dictionaries and set operations. ([Python documentation][12])

### C comparison

| C                            | Python                             |
| ---------------------------- | ---------------------------------- |
| array                        | `list` — but not really equivalent |
| struct-like tuple            | `tuple`                            |
| manually implemented lookup  | `dict`                             |
| manually searched uniqueness | `set`                              |

And make one important warning:

### A Python `list` is not simply a C dynamic array

Conceptually, for students, it's much more useful to think of it as:

> a dynamically sized sequence containing references to Python objects.

You can have:

```python
data = [42, "hello", [1, 2], None]
```

That's a huge conceptual difference.

---

# Module 4 — Pythonic conditions and iteration

This contains your:

```python
if x in [3, 4]:
```

observation.

And I'd go much further.

### Compare

C-shaped Python:

```python
for i in range(len(students)):
    print(students[i])
```

Python:

```python
for student in students:
    print(student)
```

Need index too?

```python
for index, student in enumerate(students):
```

Two collections?

```python
for name, grade in zip(names, grades):
```

Membership:

```python
if x in values:
```

Dictionary:

```python
if username in users:
```

String:

```python
if "ECE" in text:
```

Sets are particularly useful for membership testing. ([Python documentation][12])

### Also teach truthiness

```python
if students:
```

rather than:

```python
if len(students) > 0:
```

This is exactly the sort of thing that makes the course feel like **Python**, rather than programming fundamentals again.

---

# Module 5 — Functions: the pointer replacement lesson

This deserves serious attention.

And here's the correction to your current mental model.

Python does **not** pass parameters like C pointers, but this:

```python
def change(x):
    x = 42
```

and this:

```python
def change(values):
    values.append(42)
```

behave differently.

Why?

Because function arguments are **passed by assignment**.

Rebinding:

```python
x = 42
```

changes which object the **local name** references.

Mutating:

```python
values.append(42)
```

changes the actual shared object.

Python's FAQ explicitly describes this distinction and recommends returning multiple values rather than trying to emulate C-style output parameters. ([Python documentation][11])

This lesson could be fantastic.

### Exercise

Give them 10 snippets.

They must predict:

1. output;
2. whether the original object changes;
3. whether two variables reference the same object.

Then execute the code.

Something like:

```text
Prediction → Execution → Explanation
```

That's much better than just coding.

---

# Module 6 — Functions, but actually Python functions

Once the object model is understood:

* multiple return values;
* tuple unpacking;
* default arguments;
* keyword arguments;
* positional arguments;
* `*args`;
* `**kwargs`;
* scope;
* type annotations.

Also introduce the famous trap:

```python
def add_student(students=[]):
```

Mutable default arguments are evaluated once when the function is defined, so the same object may be reused across calls. Python's documentation explicitly warns about this. ([Python documentation][11])

That's a fantastic exam question, incidentally. 😈

---

# Module 7 — Comprehensions and transformation

Now take their rigid C loops and let them loosen up.

Start:

```python
squares = []

for x in values:
    squares.append(x * x)
```

Then:

```python
squares = [x * x for x in values]
```

The official tutorial describes comprehensions precisely as a concise way of constructing sequences from transformations and conditions. ([Python documentation][12])

But I'd emphasize:

> **Readable comprehension > clever comprehension.**

Do not create students who write:

```python
[x for x in y if x if all(z for z in ...)]
```

and then feel powerful. 😭

---

# Module 8 — Dictionaries and sets as algorithmic weapons

Here the Algorithm course can really reconnect.

Problems like:

* frequencies;
* duplicate detection;
* caching;
* graph adjacency;
* lookup tables;
* grouping;
* uniqueness.

Example challenge:

```text
Paris -> Lyon
Paris -> Lille
Lyon -> Nantes
...
```

Build a graph:

```python
dict[str, list[str]]
```

Suddenly they're using algorithm knowledge, but with much more expressive structures.

AoC has probably already shown you how absurdly useful dictionaries become.

---

# Module 9 — Files, `pathlib`, exceptions and `with`

This is another place I'd avoid old-school Python teaching.

Don't start them with:

```python
file = open(...)
...
file.close()
```

Teach:

```python
with ...
```

as resource management.

Then:

* text files;
* `Path`;
* encoding;
* CSV/JSON later;
* exceptions;
* `try / except / else / finally`;
* raising errors.

This is a nice transition from:

```c
if (file == NULL)
```

toward exception-based error handling.

---

# Module 10 — Building actual Python programs

Now:

* modules;
* imports;
* `__name__`;
* packages;
* project structure;
* `pyproject.toml`;
* virtual environments;
* `uv`.

This is where I'd transition away from:

```text
exercise.py
```

toward:

```text
weather_analyzer/
├── src/
│   └── weather_analyzer/
├── tests/
├── pyproject.toml
└── README.md
```

Current `uv` project workflows can manage the project environment, dependencies and lockfile from this structure. ([Astral Docs][13])

---

# Module 11 — Testing and debugging

I would definitely teach **pytest**.

Not because it's “advanced Python,” but because students should start treating functions as things that must have contracts.

Pytest gives you simple:

```python
assert ...
```

based tests, automatic test discovery and later fixtures/parameterization. ([pytest][14])

Start extremely simply.

A homework could ship with:

```text
tests/
    test_basic.py
```

Students run:

```bash
pytest
```

You can progressively introduce hidden tests in submissions.

That's also useful against:

> “Works on my machine 🙂”

---

# Module 12 — Iterables, generators and lazy evaluation

**Now** we're entering what I'd personally call genuinely Advanced Python.

Teach:

```python
iter()
next()
yield
generator expressions
range
enumerate
zip
```

and the distinction between:

```text
container
iterable
iterator
generator
```

This is a very nice point for students with C knowledge because it begins exposing **how Python protocols work**.

---

# Then: Advanced Python proper

Only after that foundation would I choose from:

```text
dataclasses
decorators
context managers
dunder methods
typing
collections
itertools
functools
generators
OOP in Python
protocols
asyncio
concurrency
multiprocessing
```

And I definitely **wouldn't try to teach all of them** just because the title says Advanced Python.

I'd rather have a student who genuinely understands:

```python
x = y
```

than one who can blindly write:

```python
@functools.cache
```

without knowing what object they're caching.

---

# 9. Your C → Python syllabus bridge

I think this table could almost become an actual slide in your first lecture:

| Students know from C       | New Python question                         |
| -------------------------- | ------------------------------------------- |
| Variables store values     | What does a Python name actually reference? |
| `char` / `char[]`          | Why does Python have immutable `str`?       |
| Arrays                     | When should I use list, tuple, set or dict? |
| Pointers                   | What are references and aliases?            |
| `malloc/calloc/free`       | Who manages Python objects?                 |
| Array indexes              | Why iterate over values instead?            |
| Functions + pointer output | Why return multiple values?                 |
| Structs                    | Tuple, dict, dataclass or class?            |
| Error return codes         | Exceptions                                  |
| Header/source files        | Modules and packages                        |
| Manual loops               | Comprehensions/built-ins                    |
| Fixed types                | Dynamic typing + type hints                 |
| Memory address reasoning   | Identity / mutability / lifecycle           |

That's basically your **course backbone**.

---

# 10. A lab format I'd strongly encourage

Rather than each lab being:

> Exercise 1
> Exercise 2
> Exercise 3
> Exercise 4

I'd give each lab a conceptual progression.

For example:

## LAB — Mutability

### Part A — Predict

```python
a = [1, 2]
b = a
b.append(3)
```

What happens?

---

### Part B — Experiment

Use:

```python
id(a)
id(b)
a is b
```

---

### Part C — Break it

Students deliberately create an aliasing bug.

---

### Part D — Repair it

Find two possible solutions.

---

### Part E — Apply

Implement a small inventory system.

That means they're not just practicing syntax.

They're building a **mental model**.

---

# 11. I also love a “C-shaped Python → Pythonic Python” exercise

You could regularly give them something like:

```python
result = []

for i in range(0, len(numbers)):
    if numbers[i] % 2 == 0:
        result.append(numbers[i] * numbers[i])
```

Don't ask:

> “Make this shorter.”

Ask:

> **“Make this more idiomatic without reducing readability.”**

That's a much better lesson.

It teaches that Pythonic doesn't mean code golf.

You could even have three stages:

```text
Working Python
      ↓
Readable Python
      ↓
Idiomatic Python
```

That could become a recurring theme throughout the semester.

---

# 12. Homework strategy for 15–20 students

With this class size, I'd take advantage of the fact that you can still actually inspect student work.

Rather than 2–3 huge assignments:

### I'd do frequent small homework

Something like:

```text
HW-01   30–45 min
HW-02   45–60 min
HW-03   60 min
HW-04   60–90 min
...
```

Each one targets **one language concept**.

For example:

| HW | Core concept      |
| -- | ----------------- |
| 01 | strings + slicing |
| 02 | mutability        |
| 03 | functions         |
| 04 | dict/set          |
| 05 | comprehensions    |
| 06 | files             |
| 07 | exceptions        |
| 08 | modules           |
| 09 | pytest            |
| 10 | generators        |

And eventually combine them.

---

# 13. For monitoring their actual work

I wouldn't make automated tests equal the entire grade.

I'd use three dimensions:

```text
Correctness
    +
Code quality
    +
Understanding
```

For instance:

**60% tests**

Does it actually work?

**25% quality**

Names, decomposition, readable Python, sensible structures.

**15% understanding**

A tiny written question:

> Why did you use a dictionary here rather than a list?

or:

> Would modifying this list inside the function affect the caller? Explain.

That last part becomes particularly valuable now that AI can produce perfectly plausible Python code.

And occasionally:

> “Explain this function to me.”

for 2 minutes during the lab.

With only 15–20 students, you can realistically do that.

---

# 14. One additional anti-copying idea I think fits your teaching style

Give students **tests but not implementations**.

For example:

```text
Your program must make these 8 tests succeed.
```

Then perhaps 4 additional tests remain hidden.

This changes the task from:

> “Produce this output.”

to:

> “Implement this behavior.”

Pytest is very well suited to this style because tests can start with plain `assert` statements and later grow into parameterized tests and fixtures. ([pytest][14])

And students gradually learn professional testing at the same time.

---

# 15. If I were building your first ~6 sessions right now

I'd probably do:

```text
ADVANCED PYTHON
│
├── 01 — From C to Python
│       syntax refresh
│       first Python program
│       C-shaped Python
│
├── 02 — Objects, Names & Memory
│       references
│       identity
│       mutability
│       aliasing
│
├── 03 — Strings & Sequences
│       immutable strings
│       slicing
│       indexing
│       membership
│
├── 04 — Containers
│       list
│       tuple
│       dict
│       set
│
├── 05 — Iterating the Python Way
│       for
│       range
│       enumerate
│       zip
│       membership
│       truthiness
│
└── 06 — Functions & Data Flow
        arguments
        mutation
        return values
        unpacking
        defaults
        scope
```

Only **after those six** would I start:

```text
comprehensions
files
exceptions
dataclasses
modules
testing
generators
...
```

And I think that slow ramp you're imagining is exactly right.

The students aren't beginners.

But they **are beginners in Python's object model**.

That's an important distinction.

---

## And your three Advent of Code observations?

I'd turn all three directly into course material:

**“Strings can't be modified.”**
→ lesson on immutable objects and sequence operations. Python formally defines `str` as an immutable sequence. ([Python documentation][1])

**“Function parameters don't behave like pointers.”**
→ lesson on name binding, aliases, mutation and return values. Python arguments are passed by assignment; mutable objects can still be changed through a parameter. ([Python documentation][11])

**`if x in [3, 4]`**
→ lesson on Python protocols, membership, collections and readable intent. `in` applies far beyond lists—to strings, tuples, dictionaries, sets and other containers/iterables. ([Python documentation][12])

Those aren't little syntax curiosities.

They're almost **three perfect entry points into what makes Python Python**.

And I think your AoC relearning is going to be unusually useful for designing this course, because you're currently experiencing exactly the *“wait, why does Python do that?”* moments your students are going to have.

[1]: https://docs.python.org/3/reference/datamodel.html?highlight=co_consts&utm_source=chatgpt.com "3. Data model — Python 3.14.6 documentation"
[2]: https://code.visualstudio.com/docs/languages/python?utm_source=chatgpt.com "Python in Visual Studio Code"
[3]: https://research.google.com/colaboratory/faq.html?hl=fr&utm_source=chatgpt.com "Google Colab"
[4]: https://jupyterlite.readthedocs.io/en/stable/?utm_source=chatgpt.com "JupyterLite — JupyterLite 0.8.3 documentation"
[5]: https://jupyterhub.readthedocs.io/en/latest/explanation/singleuser.html?utm_source=chatgpt.com "The JupyterHub single-user server — JupyterHub documentation"
[6]: https://docs.astral.sh/uv/?utm_source=chatgpt.com "uv"
[7]: https://github.blog/changelog/2026-08-27-github-classroom-deprecated/?utm_source=chatgpt.com "GitHub Classroom deprecated - GitHub Changelog"
[8]: https://github.com/orgs/community/discussions/196615?utm_source=chatgpt.com "📣 Important announcement for Educators: GitHub Classroom functionality will be transitioning to partners · community · Discussion #196615 · GitHub"
[9]: https://github.com/orgs/community/discussions/200700?utm_source=chatgpt.com "Introducing Classroom 50, an open-source alternative to GitHub Classroom · community · Discussion #200700 · GitHub"
[10]: https://www.codegrade.com/solutions/github-integration?utm_source=chatgpt.com "GitHub Integration for CS Courses | CodeGrade"
[11]: https://docs.python.org/3/faq/programming.html?highlight=unboundlocalerror&utm_source=chatgpt.com "Programming FAQ — Python 3.14.6 documentation"
[12]: https://docs.python.org/3/tutorial/datastructures.html?highlight=list+remove&utm_source=chatgpt.com "5. Data Structures — Python 3.14.6 documentation"
[13]: https://docs.astral.sh/uv/guides/projects/?utm_source=chatgpt.com "Working on projects | uv"
[14]: https://docs.pytest.org/en/latest/getting-started.html?utm_source=chatgpt.com "Get Started - pytest documentation"
