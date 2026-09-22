# Tetrika Python Assignment

Python solutions for a technical assignment originally completed for Tetrika.

The repository contains three independent tasks covering runtime type validation, external API integration, and interval-processing algorithms.

## Tasks

### Task 1 — Strict Type Checking

Runtime type validation implemented as a `@strict` decorator.

The solution uses function introspection to bind positional and keyword arguments to their corresponding parameters and validates them against their type annotations at runtime.

**Topics:** decorators, type annotations, `inspect`, runtime validation.

[View task →](task1/README.md)

### Task 2 — Wikipedia Category Aggregation

Collects entries from the Russian Wikipedia category "Животные по алфавиту" using the MediaWiki API and stores the number of entries for each Russian letter in `beasts.csv`.

API pagination is handled through continuation tokens, while data aggregation and CSV output are separated into independent processing steps.

**Topics:** HTTP API, pagination, data aggregation, CSV processing, mocking.

[View task →](task2/README.md)

### Task 3 — Lesson Presence Overlap

Calculates the total time during which both a pupil and a tutor were present in an online lesson.

Presence intervals are normalized, clipped to the lesson boundaries, merged, and processed using a two-pointer algorithm.

**Topics:** interval processing, sorting, merging, two-pointer algorithm.

[View task →](task3/README.md)


## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/nikolaitolmachev/tetrika-python-assignment.git
cd tetrika-python-assignment

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Testing

Run the complete test suite from the repository root:

```bash
pytest
```

The test suite covers the assignment requirements as well as additional edge cases for type validation, API pagination, CSV output, and interval processing.

## Requirements

* Python 3.12+
* `requests`
* `pytest`

## Original Task Statements

The original task descriptions are preserved in Russian inside each task directory:

* [`task1/original_task.md`](task1/original_task.md)
* [`task2/original_task.md`](task2/original_task.md)
* [`task3/original_task.md`](task3/original_task.md)

## License

The source code in this repository is licensed under the [MIT License](LICENSE).

Original task statements are preserved for context and are not covered by this license.
