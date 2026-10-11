"""
autoeda/cli/dist.py
-------------------
Click command: `autoeda dist <file>`

Profiles distributions and runs statistical hypothesis tests for normality:
  - Normality tests: Shapiro-Wilk, Kolmogorov-Smirnov, D'Agostino-Pearson K^2
  - Skewness and excess kurtosis ratings
  - Terminal ASCII histogram and Q-Q plot visualization
"""

from __future__ import annotations

import click


_NORMALITY_TESTS = ("all", "shapiro", "ks", "dagostino")


@click.command("dist")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--test",
    "-t",
    default="all",
    show_default=True,
    type=click.Choice(_NORMALITY_TESTS, case_sensitive=False),
    help="Normality test to run: 'shapiro', 'ks' (Kolmogorov-Smirnov), 'dagostino', or 'all'.",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated column names to test. Defaults to all numeric columns.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--qq/--no-qq",
    default=False,
    help="Render an ASCII Quantile-Quantile (Q-Q) plot in the terminal.",
)
@click.option(
    "--alpha",
    default=0.05,
    show_default=True,
    type=float,
    help="Significance level alpha for hypothesis testing (typically 0.05 or 0.01).",
)
def dist(
    filepath: str,
    test: str,
    columns: str | None,
    qq: bool,
    alpha: float,
) -> None:
    """Assess feature distributions, skewness, and statistical normality tests.

    \\b
    Examples:
      autoeda dist data.csv
      autoeda dist data.csv --test shapiro --columns age,salary
      autoeda dist data.csv --qq --columns income
    """
    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Execute autoeda.core.distribution.profile_distributions(...).
    # TODO: Render summary table:
    #       - Column | Skewness | Kurtosis | Test | Statistic | p-value | Normal? (p > alpha)
    # TODO: If --qq is enabled, print ASCII Q-Q scatter plot for requested column(s).
    click.echo(
        f"[dist] Profiling distributions and normality tests on '{filepath}' (test: {test}) (TODO)"
    )
