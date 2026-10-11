"""
autoeda/cli/missing.py
----------------------
Click command: `autoeda missing <file>`

Audits a dataset for missing (null/NaN) values. Reports per-column missing
count and percentage, and optionally renders a terminal density chart flagging
columns that exceed a configurable threshold.
"""

import click


@click.command("missing")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--threshold",
    "-t",
    default=0.0,
    show_default=True,
    type=click.FloatRange(min=0.0, max=100.0),
    help=(
        "Highlight columns whose missing percentage exceeds this value (0–100). "
        "Highlighted columns appear in red in the output table."
    ),
    metavar="PCT",
)
@click.option(
    "--plot/--no-plot",
    default=False,
    show_default=True,
    help="Render a terminal bar chart showing missing value density per column.",
)
@click.option(
    "--drop-complete",
    is_flag=True,
    default=False,
    help="Exclude columns that have zero missing values from the report.",
)
def missing(filepath: str, threshold: float, plot: bool, drop_complete: bool) -> None:
    """Audit missing (null/NaN) values across all columns in the dataset.

    Prints a table showing missing count and percentage for each column.
    Columns exceeding --threshold are highlighted for attention.

    \b
    Examples:
      autoeda missing data.csv
      autoeda missing data.csv --threshold 5.0 --plot
      autoeda missing data.csv --drop-complete
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Call autoeda.core.nulls.compute_missing(data) to compute per-column:
    #         - total missing count
    #         - missing percentage (missing / total_rows * 100)
    #         - a flag indicating whether the column exceeds threshold
    #       Return a MissingResult dataclass (to be defined in core/nulls.py).

    # TODO: If --drop-complete is set, filter out columns with 0 missing values
    #       from the MissingResult before rendering.

    # TODO: Call autoeda.renderers.table.render_missing_table(result, threshold)
    #       to print the report. Columns above threshold should be rendered in
    #       red using click.style() or equivalent ANSI coloring.

    # TODO: If --plot is set, call
    #       autoeda.renderers.charts.render_missing_bar_chart(result)
    #       to render a horizontal Unicode bar chart in the terminal showing
    #       the proportion of missing values per column.

    click.echo(f"[missing] Not yet implemented — target file: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
