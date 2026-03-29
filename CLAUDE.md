# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Python 3.14 project managed with `uv`.

## Structure

- `src/python_project/` — application source code
- `tests/` — pytest test files mirroring the src layout

## Code Style

- Always use type hints on all function parameters, return types, and non-obvious variables.

## Testing

- Add or update tests in `tests/` for every code change.
- Run `uv run pytest` after changes — all tests must pass before the task is done.

## Commands

```bash
# Run the entry point
uv run python-project

# Run all tests
uv run pytest

# Run a single test file
uv run pytest tests/test_main.py

# Add a dependency
uv add <package>

# Add a dev dependency
uv add --dev <package>
```
