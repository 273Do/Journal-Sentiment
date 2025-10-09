# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Journal Sentiment is a tool that analyzes emotional sentiment from iPhone's built-in Journal app data. The tool processes HTML journal entries stored in `AppleJournalEntries/Entries/` and performs sentiment analysis on the text data.

## Development Environment

- **Python Version**: 3.11
- **Package Manager**: pip with requirements.txt
- **Linter/Formatter**: Ruff (configured in ruff.toml)
- **Testing**: pytest
- **Git Hooks**: lefthook (pre-commit, pre-push, commit-msg)
- **Container**: Docker with docker-compose

## Essential Commands

### Running Tests
```bash
# Run all tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_main.py -v
```

### Linting and Formatting
```bash
# Format code
ruff format .

# Check formatting without making changes
ruff format . --check

# Run linter
ruff check .

# Run linter with auto-fix
ruff check . --fix
```

### Docker
```bash
# Build and start container
docker-compose up -d

# Access container shell
docker-compose exec app bash
```

### Git Workflow
- Commit messages must follow the pattern: `feat:|fix:|refactor:|chore:` (enforced by lefthook)
- Pre-commit hooks run formatting and linting on staged Python files
- Pre-push hooks run format check, lint check, and full test suite

## Code Quality Standards

### Ruff Configuration
- Line length: 88 characters (Black compatible)
- Target version: Python 3.11
- Ignored rules: T201 (print statements allowed), D103, D100 (docstring requirements relaxed)
- Quote style: double quotes
- Indent style: spaces (4 spaces)

## Project Architecture

### Data Pipeline (Planned)
Based on `fd.md`, the tool is designed to:
1. Process journal HTML entries from `AppleJournalEntries/Entries/`
2. Convert data to CSV format in a `result` directory
3. Allow users to set analysis periods via CLI
4. Perform 5-level sentiment analysis on journal text per day
5. Aggregate results by overall, monthly, and day-of-week statistics
6. Output results to terminal and table format

### Current Implementation Status
The codebase appears to be in early development with basic test setup. The `main.py` currently contains placeholder functions (`sum_even_numbers`, `show_exec_info`) used for testing the development environment setup.

## CI/CD

The GitHub Actions workflow (`.github/workflows/ci.yml`) runs on:
- Push/PR with changes to `*.py` files
- Executes: ruff format check, ruff lint, pytest

## Dependencies

Key packages (from requirements.txt):
- ruff: Linting and formatting
- pytest: Testing framework
- pandas: Data manipulation (for CSV processing)
- matplotlib: Visualization
- lefthook: Git hooks management