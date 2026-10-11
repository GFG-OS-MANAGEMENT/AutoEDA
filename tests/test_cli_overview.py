"""
tests/test_cli_overview.py
---------------------------
CLI integration tests for `autoeda overview` using Click's CliRunner.

All tests invoke the CLI as a black-box, asserting on exit codes and
output strings. They do NOT test internal logic (that belongs in test_core_*).
"""

import pytest
from click.testing import CliRunner

from autoeda.cli.main import cli


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@pytest.fixture()
def runner() -> CliRunner:
    """Return a Click CliRunner with colour output disabled for clean assertions."""
    return CliRunner()


# ---------------------------------------------------------------------------
# --help tests
# ---------------------------------------------------------------------------

def test_overview_help(runner: CliRunner) -> None:
    """The `overview --help` flag should exit 0 and describe the command."""
    result = runner.invoke(cli, ["overview", "--help"])
    assert result.exit_code == 0
    assert "overview" in result.output.lower()
    # TODO: Assert that --head and --tail options appear in help output.


# ---------------------------------------------------------------------------
# Basic invocation tests (to be enabled once implemented)
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Not yet implemented — remove skip when overview command is ready.")
def test_overview_basic(runner: CliRunner, sample_csv: str) -> None:
    """Running `overview` on a valid CSV should exit 0 and print column names."""
    result = runner.invoke(cli, ["overview", sample_csv])
    assert result.exit_code == 0
    assert "id" in result.output
    assert "salary" in result.output
    # TODO: Assert memory usage line is present.
    # TODO: Assert row count is displayed.


@pytest.mark.skip(reason="Not yet implemented — remove skip when overview command is ready.")
def test_overview_missing_file(runner: CliRunner) -> None:
    """Providing a non-existent file path should exit non-zero."""
    result = runner.invoke(cli, ["overview", "/nonexistent/path/data.csv"])
    assert result.exit_code != 0
    # TODO: Assert that a helpful error message is printed.


@pytest.mark.skip(reason="Not yet implemented — remove skip when overview command is ready.")
def test_overview_no_preview(runner: CliRunner, sample_csv: str) -> None:
    """The --no-preview flag should suppress the row preview table."""
    result = runner.invoke(cli, ["overview", sample_csv, "--no-preview"])
    assert result.exit_code == 0
    # TODO: Assert that the row preview table is absent from output.


@pytest.mark.skip(reason="Not yet implemented — remove skip when overview command is ready.")
def test_overview_custom_head(runner: CliRunner, sample_csv: str) -> None:
    """The --head option should control how many rows appear in the preview."""
    result = runner.invoke(cli, ["overview", sample_csv, "--head", "2"])
    assert result.exit_code == 0
    # TODO: Assert exactly 2 data rows appear in the preview section.
