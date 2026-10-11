"""
tests/test_cli_eda_suite.py
----------------------------
Integration tests for newly added EDA and data cleaning CLI commands:
  - autoeda pca
  - autoeda normalize
  - autoeda transform
  - autoeda dist
  - autoeda vif
  - autoeda time
  - autoeda clean (cast, rename, clip, encode, fill, drop, dedup)
"""

import pytest
from click.testing import CliRunner

from autoeda.cli.main import cli


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()


# ---------------------------------------------------------------------------
# CLI Help Screen Tests (these pass immediately without core logic)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "command_args",
    [
        ["pca", "--help"],
        ["normalize", "--help"],
        ["transform", "--help"],
        ["dist", "--help"],
        ["vif", "--help"],
        ["time", "--help"],
        ["clean", "--help"],
        ["clean", "cast", "--help"],
        ["clean", "rename", "--help"],
        ["clean", "clip", "--help"],
        ["clean", "encode", "--help"],
        ["clean", "fill", "--help"],
        ["clean", "drop", "--help"],
        ["clean", "dedup", "--help"],
    ],
)
def test_eda_commands_help_exit_zero(runner: CliRunner, command_args: list[str]) -> None:
    """Verify that every new EDA subcommand responds to --help with exit code 0."""
    result = runner.invoke(cli, command_args)
    assert result.exit_code == 0, f"Command failed: {command_args}\n{result.output}"
    assert "Usage:" in result.output


# ---------------------------------------------------------------------------
# Execution / Feature Tests (skipped pending contributor implementation)
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Contributors must implement autoeda.core.pca before unskipping.")
def test_pca_execution(runner: CliRunner, sample_csv_file: str) -> None:
    result = runner.invoke(cli, ["pca", sample_csv_file, "--n-components", "2"])
    assert result.exit_code == 0
    assert "PC1" in result.output


@pytest.mark.skip(reason="Contributors must implement autoeda.core.normalization before unskipping.")
def test_normalize_execution(runner: CliRunner, sample_csv_file: str, tmp_path) -> None:
    out_file = str(tmp_path / "normalized.csv")
    result = runner.invoke(cli, ["normalize", sample_csv_file, "--method", "standard", "-o", out_file])
    assert result.exit_code == 0


@pytest.mark.skip(reason="Contributors must implement autoeda.core.transformation before unskipping.")
def test_transform_execution(runner: CliRunner, sample_csv_file: str) -> None:
    result = runner.invoke(cli, ["transform", sample_csv_file, "--method", "log"])
    assert result.exit_code == 0


@pytest.mark.skip(reason="Contributors must implement autoeda.core.distribution before unskipping.")
def test_dist_execution(runner: CliRunner, sample_csv_file: str) -> None:
    result = runner.invoke(cli, ["dist", sample_csv_file, "--test", "shapiro"])
    assert result.exit_code == 0


@pytest.mark.skip(reason="Contributors must implement autoeda.core.collinearity before unskipping.")
def test_vif_execution(runner: CliRunner, sample_csv_file: str) -> None:
    result = runner.invoke(cli, ["vif", sample_csv_file, "--threshold", "10.0"])
    assert result.exit_code == 0
