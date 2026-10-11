"""
tests/test_cli_stats.py
------------------------
CLI integration tests for `autoeda stats` using Click's CliRunner.
"""

import pytest
from click.testing import CliRunner

from autoeda.cli.main import cli


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


def test_stats_help(runner: CliRunner) -> None:
    """The `stats --help` flag should exit 0 and describe the command."""
    result = runner.invoke(cli, ["stats", "--help"])
    assert result.exit_code == 0
    assert "stats" in result.output.lower()
    # TODO: Assert --columns and --hist options appear in help text.


@pytest.mark.skip(reason="Not yet implemented — remove skip when stats command is ready.")
def test_stats_all_columns(runner: CliRunner, sample_csv: str) -> None:
    """Running stats on a valid CSV (all columns) should exit 0."""
    result = runner.invoke(cli, ["stats", sample_csv])
    assert result.exit_code == 0
    # TODO: Assert numerical column stats (mean, std, min, max) are present.
    # TODO: Assert categorical column stats are present.


@pytest.mark.skip(reason="Not yet implemented — remove skip when stats command is ready.")
def test_stats_specific_columns(runner: CliRunner, sample_csv: str) -> None:
    """The --columns flag should restrict output to the named columns."""
    result = runner.invoke(cli, ["stats", sample_csv, "--columns", "age,salary"])
    assert result.exit_code == 0
    assert "age" in result.output
    assert "salary" in result.output
    # TODO: Assert columns not listed (e.g. "name") do NOT appear.


@pytest.mark.skip(reason="Not yet implemented — remove skip when stats command is ready.")
def test_stats_invalid_column(runner: CliRunner, sample_csv: str) -> None:
    """Providing a non-existent column name should exit non-zero with an error."""
    result = runner.invoke(cli, ["stats", sample_csv, "--columns", "nonexistent"])
    assert result.exit_code != 0
    # TODO: Assert a descriptive error message is shown.


@pytest.mark.skip(reason="Not yet implemented — remove skip when stats command is ready.")
def test_stats_with_hist(runner: CliRunner, sample_csv: str) -> None:
    """The --hist flag should produce histogram output for numerical columns."""
    result = runner.invoke(cli, ["stats", sample_csv, "--hist"])
    assert result.exit_code == 0
    # TODO: Assert histogram block characters (▏▎▍▌▋▊▉█) appear in output.
