# python-project

A Python 3.14 project managed with [uv](https://docs.astral.sh/uv/).

## Prerequisites

- **Python 3.14+** — required by the project
- **uv** — package and project manager

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or via Homebrew on macOS:

```bash
brew install uv
```

## Setup

Clone the repo and install dependencies:

```bash
git clone <repo-url>
cd python-project
uv sync
```

`uv sync` creates a virtual environment and installs all dependencies (including dev dependencies) automatically.

## Usage

Run the entry point:

```bash
uv run python-project
```

## Development

Run all tests:

```bash
uv run pytest
```

Run a single test file:

```bash
uv run pytest tests/test_main.py
```

Add a dependency:

```bash
uv add <package>
```

Add a dev dependency:

```bash
uv add --dev <package>
```
