# template-web-automation

A minimal, typed Playwright web automation template with `uv`, Ruff, mypy, pytest, pre-commit, GitHub Actions, and semantic-release wired together.

## Intended Use

Use this template for browser-based workflow automation using Playwright. The repository infrastructure is ready
for local development and release automation; the package modules are intentionally thin
placeholders for project-specific implementation.

## Project Layout

```text
src/template_web_automation/
  __init__.py
  py.typed
  browser.py
  config.py
  exceptions.py
  actions/
    __init__.py
    common.py
  models/
    __init__.py
  pages/
    __init__.py
    example_page.py
  workflows/
    __init__.py
    example_workflow.py
tests/
  unit/
    test_template_integrity.py
  integration/
```

Keep reusable Python code under `src/template_web_automation/` and tests under `tests/`.
The `py.typed` marker declares the package as typed.

## Local Setup

Install dependencies into the local environment:

```sh
uv sync --frozen --group dev
```

Install pre-commit hooks:

```sh
uv run pre-commit install
```

Run all baseline checks locally:

```sh
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
uv build
uv run pre-commit run --all-files
```

Use Ruff to apply safe fixes:

```sh
uv run ruff check --fix .
uv run ruff format .
```

## Linting, Formatting, And Typing

Ruff and mypy follow the same conventions as the Python library template:
Python 3.14, `src/` layout, strict mypy, 88-character line length, Ruff import
sorting, and normal `assert` statements allowed in tests.

## Tests

The initial tests verify template integrity without pretending application
behavior exists. Add focused unit and integration tests alongside each real
implementation as the copied project grows.

## Build And Release

The package builds with Hatchling through `uv build`. The release workflow
validates mypy, pytest, and pre-commit before python-semantic-release runs with
conventional commits and tags like `v0.0.1`. Ruff linting and formatting run
through pre-commit.

## Copy And Rename

After copying this template, replace these names everywhere:

- project name: `template-web-automation`
- package name: `template_web_automation`


Then update package metadata in `pyproject.toml`, refresh `uv.lock` with
`uv lock`, run `uv sync --frozen --group dev`, and run the baseline checks.
