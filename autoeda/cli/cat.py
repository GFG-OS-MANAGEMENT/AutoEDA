"""
autoeda/cli/cat.py
------------------
Click command: `autoeda cat <file>`

Profiles categorical (string) columns in a dataset. Reports value frequencies,
unique value counts, and top-N most/least common values.
"""

import click


@click.command("cat")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--top",
    "-n",
    default=10,
    show_default=True,
    type=click.IntRange(min=1),
    help="Number of top (most frequent) values to show per column.",
)
@click.option(
    "--cardinality/--no-cardinality",
    default=True,
    show_default=True,
    help="Show the total unique value count (cardinality) for each column.",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated list of categorical columns to analyse. Defaults to all string columns.",
    metavar="COL1,COL2,...",
)
def cat(filepath: str, top: int, cardinality: bool, columns: str | None) -> None:
    """Profile categorical columns: frequency tables and cardinality metrics.

    Prints per-column frequency distribution tables and unique value counts
    for all string/object-type columns in the dataset.

    \b
    Examples:
      autoeda cat data.csv
      autoeda cat data.csv --top 5 --columns department,country
      autoeda cat data.csv --no-cardinality
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Determine target columns: if --columns is provided, validate each
    #       exists and is of categorical/string type. Otherwise default to all
    #       object/string dtype columns.

    # TODO: Call autoeda.core.summary.compute_categorical_stats(data, columns, top_n=top)
    #       to compute per-column:
    #         - total distinct (unique) value count
    #         - top-N most frequent values with their counts and percentages
    #       Return a CategoricalResult dataclass (to be defined in core/summary.py).

    # TODO: Call autoeda.renderers.table.render_categorical_table(result, cardinality)
    #       to print a frequency distribution table per column.
    #       If cardinality=False, omit the unique count row.

    click.echo(f"[cat] Not yet implemented — target file: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
