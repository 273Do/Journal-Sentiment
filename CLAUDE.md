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
pytest tests/usecase/test_html_to_df.py -v
pytest tests/usecase/test_read_html.py -v

# Run single test function
pytest tests/usecase/test_read_html.py::test_read_html_pattern1 -v
```

**Note**: Tests require `pandas` and `pytest` to be installed. If running locally without these dependencies, use Docker:
```bash
docker-compose up -d
docker-compose exec app pytest -v
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

### Code Organization
```
src/
├── schema/data_format/
│   └── entry_type.py          # TypedDict definitions for journal entries
└── usecase/data_format/
    ├── read_html.py           # HTML parser for Apple Journal entries
    ├── html_to_df.py          # Converts HTML files to pandas DataFrame
    └── date_format.py         # Date string parsing utilities
```

### Data Flow
1. **Input**: HTML files from `AppleJournalEntries/Entries/` (configured via `.env`)
2. **Processing**:
   - `read_html()`: Parses individual HTML files using custom HTMLParser
   - `html_to_df()`: Aggregates multiple entries into pandas DataFrame
3. **Output**: CSV file saved to `results/` directory (configured via `.env`)

### HTML Parsing Strategy
The parser (`read_html.py`) handles two different Apple Journal HTML patterns:
- **Pattern 1**: `<div class='title'>` (title) + `<span class="s2">` (body)
- **Pattern 2**: `<span class="s2">` (title) + `<span class="s3">` (body)

The `JournalHTMLParser` class automatically detects which pattern is used by checking for the presence of `<div class='title'>`.

### Type System
- `EntryType`: Complete entry with date, title, and body
- `ParserEntryType`: Subset returned by HTML parser (title and body only)
- Date extraction happens at two levels:
  - From HTML content: `<div class="pageHeader">YYYY年MM月DD日</div>`
  - From filename: `YYYY-MM-DD_タイトル.html`

### Running the Main Pipeline
```bash
# Execute the data formatting pipeline
./main.sh
# Or directly:
python3 setup.py
```

The `main.sh` script:
1. Validates environment variables (`ENTRY_PATH`, `OUTPUT_PATH`)
2. Checks that the entry directory exists
3. Creates output directory if needed
4. Runs `setup.py` to convert HTML → CSV

### Environment Configuration
Create a `.env` file with:
```bash
ENTRY_PATH=AppleJournalEntries/Entries  # Path to HTML journal entries
OUTPUT_PATH=results                      # CSV output directory
```

### Future Implementation (from fd.md)
The following features are planned but not yet implemented:
- CLI for setting analysis periods
- 5-level sentiment analysis on journal text
- Aggregation by overall, monthly, and day-of-week statistics
- Visualization with matplotlib
- Terminal output of sentiment distribution and statistics

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