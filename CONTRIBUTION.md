# Contributing to AutoEDA 🤝

First off, thank you for considering contributing to **AutoEDA**! 🎉

AutoEDA is an open-source project dedicated to making Exploratory Data Analysis fast, accessible, and code-free straight from the terminal. The project is built in **Python** using the **[Click](https://click.palletsprojects.com/)** library for robust, composable command-line interactions.

Community contributions—whether they are bug fixes, new Click subcommands, documentation improvements, or architecture refinements—are the heartbeat of this project.

Please take a moment to review this document before submitting your contribution.

---

## 📜 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [How Can I Contribute?](#-how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features & Enhancements](#suggesting-features--enhancements)
  - [Improving Documentation](#improving-documentation)
  - [Writing Code](#writing-code)
- [Development Setup](#-development-setup)
- [Project Architecture](#-project-architecture)
- [Building CLI Commands with Click](#-building-cli-commands-with-click)
- [Development Workflow](#-development-workflow)
  - [Branching Strategy](#branching-strategy)
  - [Code Quality & Linting](#code-quality--linting)
  - [Testing Click Commands with CliRunner](#testing-click-commands-with-clirunner)
  - [Commit Conventions](#commit-conventions)
- [Submitting a Pull Request (PR)](#-submitting-a-pull-request-pr)
- [Recognition & Community](#-recognition--community)

---

## 🕊 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to **harpreet.02007@gmail.com**.

---

## 🌟 How Can I Contribute?

### Reporting Bugs

If you find a bug or unexpected behavior:
1. **Search existing issues** on GitHub to ensure the bug hasn't already been reported.
2. If it's a new issue, open a new **Bug Report** with:
   - A clear and descriptive title.
   - Operating system and terminal type (e.g., Windows PowerShell, Ubuntu Bash, macOS zsh).
   - Python version and Click version (`click --version`).
   - Steps to reproduce the problem.
   - Minimal sample dataset or row snippet (ensure no private/sensitive data is shared).
   - Expected behavior vs. actual behavior (including stack traces or error outputs).

### Suggesting Features & Enhancements

Have an idea for a new Click subcommand, visualization style, or file format?
1. Open a **Feature Request** issue on GitHub.
2. Clearly explain:
   - What problem does this solve?
   - Proposed Click syntax (e.g., `autoeda <command> [OPTIONS] [ARGUMENTS]`).
   - Any proposed computation algorithms or libraries.

### Improving Documentation

Documentation is just as vital as code! You can help by:
- Fixing typos or improving clarity in `README.md` or Click command `--help` docstrings.
- Writing guides, tutorials, or real-world dataset walkthroughs.
- Adding docstrings and type annotations to existing Python functions.

### Writing Code

Look for open issues labeled:
- `good first issue` – Great for newcomers to the project.
- `help wanted` – Tasks where the community needs extra hands.
- `bug` – Confirmed issues needing resolution.

---

## 💻 Development Setup

### 1. Prerequisites
- **Python**: version 3.8 or higher
- **Git**
- Package manager: `pip` and virtual environment manager (`venv`)

### 2. Fork and Clone
```bash
# 1. Fork the repo on GitHub (click the "Fork" button on the repo page)

# 2. Clone your fork locally
git clone https://github.com/<YOUR-USERNAME>/AutoEDA.git
cd AutoEDA

# 3. Add the upstream remote
git remote add upstream https://github.com/GFG-OS-MANAGEMENT/AutoEDA.git
```

### 3. Set Up Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate it:
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (Command Prompt):
.\venv\Scripts\activate.bat
# Linux / macOS:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Install in editable mode with development & testing packages (including click, pytest, black, ruff)
pip install -e ".[dev]"
```

Verify your local installation:
```bash
python -m autoeda --help
# or
autoeda --help
```

---

## 🏛 Project Architecture

AutoEDA uses **Click** command groups to organize CLI features into clean, modular subcommands:

```text
AutoEDA/
├── autoeda/
│   ├── __init__.py
│   ├── cli/                     # Click CLI layer
│   │   ├── __init__.py
│   │   ├── main.py              # Root @click.group() and entrypoint
│   │   ├── overview.py          # `autoeda overview` Click command
│   │   ├── stats.py             # `autoeda stats` Click command
│   │   ├── missing.py           # `autoeda missing` Click command
│   │   ├── correlate.py         # `autoeda correlate` Click command
│   │   ├── outliers.py          # `autoeda outliers` Click command
│   │   └── report.py            # `autoeda report` Click command
│   ├── core/                    # Pure Python numerical & statistical engines
│   │   ├── summary.py           # Descriptive statistics
│   │   ├── nulls.py             # Missingness detection
│   │   ├── correlation.py       # Pearson, Spearman matrices
│   │   └── outliers.py          # IQR & Z-Score anomaly detectors
│   ├── io/                      # Multi-format data ingestors (CSV, Parquet, JSON, etc.)
│   ├── renderers/               # Terminal tables, sparklines & ANSI formatters
│   └── reports/                 # HTML / Markdown export templates
├── tests/                       # Unit tests & Click CliRunner integration tests
│   ├── test_cli_overview.py
│   ├── test_cli_stats.py
│   └── test_core_stats.py
├── LICENSE                      # Apache 2.0 License
├── README.md                    # Project overview and documentation
├── CODE_OF_CONDUCT.md           # Community guidelines
├── CONTRIBUTING.md              # Pointer file for GitHub Community Profile
└── CONTRIBUTION.md              # Contributor handbook
```

---

## ⚡ Building CLI Commands with Click

All AutoEDA CLI functionality is implemented using **[Click](https://click.palletsprojects.com/)**. Keep these best practices in mind when adding or updating commands:

### 1. Register Commands Under the Main Group
In `autoeda/cli/main.py`:
```python
import click

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(package_name="autoeda")
def cli():
    """AutoEDA: Terminal-native Exploratory Data Analysis tool."""
    pass
```

### 2. Implement Commands in `autoeda/cli/<command_name>.py`
Use Click decorators cleanly:
```python
import click
from autoeda.cli.main import cli
from autoeda.core.summary import compute_stats

@cli.command("stats")
@click.argument("filepath", type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option(
    "--columns", "-c",
    help="Comma-separated list of column names to analyze.",
    default=None,
)
@click.option(
    "--hist/--no-hist",
    default=False,
    help="Display terminal histogram for numerical distributions.",
)
def stats(filepath: str, columns: str, hist: bool):
    """Compute summary statistics for numerical and categorical columns."""
    click.echo(f"Analyzing {filepath}...")
    # Call core engine and render results
```

### 3. Click Guidelines
- **Use `click.Path`** for file paths with `exists=True, readable=True` to let Click validate paths before code execution.
- **Provide clear `help=` strings** on all arguments and options.
- **Use `click.echo()` or `click.secho()`** instead of plain `print()` to respect terminal encodings and colors.
- **Handle errors cleanly**: Use `raise click.ClickException("Clear error message")` or `raise click.BadParameter("...")` instead of unhandled Python crashes.

---

## 🔄 Development Workflow

### Branching Strategy
Never commit directly to `main`. Create a descriptive feature branch:

```bash
# Ensure your local main is up to date
git checkout main
git pull upstream main

# Create a new feature or fix branch
git checkout -b feat/add-outlier-detection
# or
git checkout -b fix/click-filepath-validation
```

Branch naming convention:
- `feat/<feature-name>` for new features or CLI commands
- `fix/<bug-name>` for bug fixes
- `docs/<doc-change>` for documentation updates
- `refactor/<module>` for refactoring code without behavioral changes
- `test/<test-name>` for adding or updating tests

### Code Quality & Linting
We follow standard Python style conventions (**PEP 8**). Before committing, format and lint your code:

```bash
# Format code using black
black autoeda tests

# Sort imports
isort autoeda tests

# Run linter
ruff check autoeda tests

# Type check
mypy autoeda
```

### Testing Click Commands with CliRunner
Click provides an isolated test runner called `CliRunner` which tests CLI commands end-to-end without spawning a subprocess:

```python
# tests/test_cli_stats.py
from click.testing import CliRunner
from autoeda.cli.main import cli

def test_stats_command_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["stats", "--help"])
    assert result.exit_code == 0
    assert "Compute summary statistics" in result.output

def test_stats_command_execution(tmp_path):
    # Create a small dummy CSV file for testing
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("age,salary\n25,50000\n30,60000\n35,70000\n")

    runner = CliRunner()
    result = runner.invoke(cli, ["stats", str(csv_file)])
    assert result.exit_code == 0
    assert "salary" in result.output
```

Run tests with pytest:
```bash
pytest
```

### Commit Conventions
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

Format:
```text
<type>(<scope>): <short description>
```

Examples:
- `feat(cli): add histogram visualization flag to click stats command`
- `fix(cli): validate file existence using click.Path`
- `docs(readme): add click framework badge and tech stack section`
- `test(cli): add CliRunner test cases for missing command`
- `refactor(core): decouple summary computation from click rendering`

---

## 🚀 Submitting a Pull Request (PR)

Once your code is tested, formatted, and committed:

1. **Push your branch to your fork:**
   ```bash
   git push origin <your-branch-name>
   ```

2. **Open a Pull Request:**
   - Go to your fork on GitHub and click **Compare & pull request**.
   - Make sure your PR targets `base: main` on `GFG-OS-MANAGEMENT/AutoEDA`.

3. **Fill out the PR Template:**
   - Describe what changes were made and why.
   - Mention the Click command(s) added or modified.
   - Link related issue(s) using keywords (e.g., `Closes #12`).
   - Include terminal output snippets or tests demonstrating the functionality.

4. **PR Checklist:**
   - [ ] My code adheres to PEP 8, formatted with `black` and checked with `ruff`.
   - [ ] Click commands provide descriptive docstrings and `--help` text.
   - [ ] I have added unit tests using `pytest` and `click.testing.CliRunner`.
   - [ ] All tests pass locally (`pytest`).
   - [ ] Documentation has been updated (`README.md` or command reference).
   - [ ] No merge conflicts with `main`.

5. **Code Review:**
   - Project maintainers will review your PR. Be prepared to answer questions, discuss design choices, or make requested adjustments.
   - Once approved, your PR will be squashed and merged into `main`!

---

## 🏆 Recognition & Community

Every contribution counts! All contributors who have code, documentation, or design merged into AutoEDA will be recognized in the repository and release notes.

If you have questions or need guidance, feel free to open a GitHub Discussion or reach out to the maintainers.

Happy coding and thank you for helping build **AutoEDA**! 🚀
