"""
autoeda/cli/timeseries.py
--------------------------
Click command: `autoeda time <file>`

Profiles temporal datasets and time-series variables:
  - Date span, inferred sampling cadence (hourly, daily, etc.)
  - Missing date gaps and irregular intervals
  - Timestamp ordering / monotonicity and duplicate timestamps
  - Autocorrelation Function (ACF) table and terminal chart
  - Seasonality distribution (day of week, hour of day)
"""

from __future__ import annotations

import click


@click.command("time")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--date-col",
    "-d",
    required=True,
    help="Name of the datetime / timestamp column.",
    metavar="COLUMN",
)
@click.option(
    "--target-col",
    "-y",
    default=None,
    help="Optional numerical target column to analyze autocorrelation (ACF) for.",
    metavar="COLUMN",
)
@click.option(
    "--lags",
    default=20,
    show_default=True,
    type=int,
    help="Maximum lags for Autocorrelation Function (ACF).",
)
def time_cmd(
    filepath: str,
    date_col: str,
    target_col: str | None,
    lags: int,
) -> None:
    """Analyze temporal datasets, detect gaps, cadence, and autocorrelation (ACF).

    \\b
    Examples:
      autoeda time sales.csv --date-col timestamp
      autoeda time stocks.csv --date-col date --target-col close --lags 30
    """
    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Execute autoeda.core.timeseries.profile_timeseries(...).
    # TODO: Print temporal overview table:
    #       - Start Date, End Date, Duration, Frequency, Monotonic? Gaps?
    # TODO: If gaps detected, display top temporal gaps table.
    # TODO: If target_col specified, print ACF table and ASCII bar chart.
    click.echo(
        f"[time] Profiling time series on '{filepath}' (date col: {date_col}) (TODO)"
    )
