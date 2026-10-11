# Repository Guidance

## Purpose and boundaries
- Keep this typed Playwright automation baseline reusable after cloning.
- Leave site-specific selectors, credentials, and workflow policy to instantiated projects.

## Development
- Put browser orchestration in `src/` and deterministic behavior tests in `tests/`.
- Keep browser setup and package rename instructions portable across machines.

## Validation
- Run `uv sync --frozen --group dev`, `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy`, `uv run pytest`, and `uv run pre-commit run --all-files`.
- Run `uv build` for packaging changes.

## Architecture constraints
- Isolate page-specific interactions from reusable browser setup.
- Do not encode a personal site or deployment environment into defaults.

## Safety
- Keep login secrets and captured real-page data out of tests and examples.

## Branching strategy

- This repository uses **trunk-based development**. Create short-lived change branches from current `main` and target PRs to `main`.
- Follow the [canonical branching and delivery policy](https://github.com/SpencerRWood/codex-config/blob/main/docs/branching-policy.md), available through the installed codex-config source path. Verify the strategy, release association, fetched base and PR target before implementation and record them in Story evidence. Story completion does not authorize publication or deployment; retain existing review, CI, security and rollback requirements.
- This classification applies to maintenance of the template repository. Replace it with the new repository's classification during project creation; applications must use release-branch integration before Story development begins.
