"""
autoeda/cli/clean/drop.py
--------------------------
Click command: `autoeda clean drop <file>`

Drops rows or columns whose missing value percentage exceeds a threshold,
or drops rows matching a specific filter expression.
"""

import click


@click.command("drop")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--threshold",
    "-t",
    default=50.0,
    show_default=True,
    type=click.FloatRange(min=0.0, max=100.0),
    help=(
        "Drop columns whose missing percentage exceeds this value. "
        "Use --axis row to drop rows instead."
    ),
    metavar="PCT",
)
@click.option(
    "--axis",
    default="column",
    show_default=True,
    type=click.Choice(["row", "column"], case_sensitive=False),
    help="Whether to drop 'row' (drop rows above threshold) or 'column' (drop columns).",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Explicitly drop these comma-separated column names (ignores --threshold).",
    metavar="COL1,COL2,...",
)
@click.option(
    "--output",
    "-o",
    required=True,
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Path for the output (cleaned) file.",
    metavar="PATH",
)
def drop(
    filepath: str,
    threshold: float,
    axis: str,
    columns: str | None,
    output: str,
) -> None:
    """Drop rows or columns with too many missing values.

    If --columns is provided, those columns are dropped unconditionally.
    Otherwise, rows or columns are dropped based on the --threshold percentage.

    \b
    Examples:
      autoeda clean drop data.csv --threshold 50.0 -o cleaned.csv
      autoeda clean drop data.csv --axis row --threshold 80.0 -o cleaned.csv
      autoeda clean drop data.csv --columns "notes,temp_col" -o cleaned.csv
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: If --columns is provided, call
    #       autoeda.core.cleaning.drop_columns(data, columns_list)
    #       to remove the explicitly named columns.

    # TODO: Otherwise, if axis == "column", call
    #       autoeda.core.cleaning.drop_high_null_columns(data, threshold)
    #       to remove columns where missing_pct > threshold.

    # TODO: If axis == "row", call
    #       autoeda.core.cleaning.drop_high_null_rows(data, threshold)
    #       to remove rows where the proportion of null cells > threshold/100.

    # TODO: Call autoeda.io.writer.write_file(cleaned_data, output).

    # TODO: Print a summary: number of rows/columns dropped, output path.

    click.echo(f"[clean drop] Not yet implemented — source: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
