"""
autoeda/cli/stats.py
--------------------
Click command: `autoeda stats <file>`

Computes descriptive statistics for numerical and categorical columns including
mean, median, mode, std, variance, skewness, kurtosis, IQR, and percentiles.
"""

import click


@click.command("stats")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated list of column names to analyse. Defaults to all columns.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--hist/--no-hist",
    default=False,
    show_default=True,
    help="Display a terminal ASCII histogram for each numerical column.",
)
@click.option(
    "--percentiles",
    default="25,50,75",
    show_default=True,
    help="Comma-separated percentile values to compute (e.g. 10,25,50,75,90).",
    metavar="P1,P2,...",
)
def stats(filepath: str, columns: str | None, hist: bool, percentiles: str) -> None:
    """Compute summary statistics for numerical and categorical columns.

    Outputs per-column metrics: count, mean, median, mode, std, variance,
    min, max, specified percentiles, skewness, kurtosis, and IQR.

    \b
    Examples:
      autoeda stats data.csv
      autoeda stats data.csv --columns age,salary --hist
      autoeda stats data.csv --percentiles 10,25,50,75,90
    """
    # TODO: Parse --columns option: split by comma, strip whitespace, validate
    #       that all provided names actually exist in the loaded dataset.

    # TODO: Parse --percentiles option: convert to a list of floats,
    #       validate that each is in the range [0, 100].

    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Filter columns from the dataset based on the --columns option.
    #       If None, include all numerical and categorical columns.

    # TODO: Call autoeda.core.summary.compute_stats(data, columns, percentiles)
    #       to compute descriptive statistics for the selected columns.
    #       Return a StatsResult dataclass (to be defined in core/summary.py).

    # TODO: Call autoeda.renderers.table.render_stats_table(result) to print
    #       a formatted table of statistics in the terminal.

    # TODO: If --hist is set, for each numerical column call
    #       autoeda.renderers.charts.render_histogram(column_data)
    #       to print an ASCII histogram below each column's stats row.

    click.echo(f"[stats] Not yet implemented — target file: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
