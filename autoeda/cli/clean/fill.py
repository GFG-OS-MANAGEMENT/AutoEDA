"""
autoeda/cli/clean/fill.py
--------------------------
Click command: `autoeda clean fill <file>`

Fills missing (null/NaN) values in numerical or categorical columns using a
configurable imputation strategy, then writes the cleaned dataset to a new file.
"""

import click


_FILL_STRATEGIES = ("mean", "median", "mode", "constant", "ffill", "bfill")


@click.command("fill")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--strategy",
    "-s",
    default="mean",
    show_default=True,
    type=click.Choice(_FILL_STRATEGIES, case_sensitive=False),
    help=(
        "Imputation strategy: "
        "'mean'/'median'/'mode' use column statistics; "
        "'constant' requires --value; "
        "'ffill'/'bfill' propagate adjacent values."
    ),
)
@click.option(
    "--value",
    default=None,
    help="Constant value to use when --strategy=constant.",
    metavar="VALUE",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated column names to fill. Defaults to all columns with missing values.",
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
@click.option(
    "--inplace",
    is_flag=True,
    default=False,
    help="Overwrite the source file instead of writing to --output. Use with caution.",
)
def fill(
    filepath: str,
    strategy: str,
    value: str | None,
    columns: str | None,
    output: str,
    inplace: bool,
) -> None:
    """Fill missing values using a chosen imputation strategy.

    Reads the dataset, fills null values in the target columns using the
    specified strategy, and writes the result to the output path.

    \b
    Examples:
      autoeda clean fill data.csv --strategy mean -o cleaned.csv
      autoeda clean fill data.csv --strategy constant --value 0 -o cleaned.csv
      autoeda clean fill data.csv --strategy mode --columns department -o cleaned.csv
    """
    # TODO: Validate --strategy=constant requires --value; raise click.BadParameter if not.

    # TODO: If --inplace is set, override output with filepath and warn the user.

    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Parse --columns: split by comma, validate each column exists.
    #       If None, target all columns that have at least one missing value.

    # TODO: Call autoeda.core.cleaning.fill_missing(data, columns, strategy, value)
    #       to perform the imputation. Return a new DataResult (never mutate in place).
    #       Implement the following strategies in core/cleaning.py:
    #         "mean"     → replace NaN with column mean (numerical only)
    #         "median"   → replace NaN with column median (numerical only)
    #         "mode"     → replace NaN with most frequent value (any dtype)
    #         "constant" → replace NaN with the provided constant value
    #         "ffill"    → forward-fill: carry the previous non-null value forward
    #         "bfill"    → backward-fill: carry the next non-null value backward

    # TODO: Call autoeda.io.writer.write_file(cleaned_data, output) to persist the result.
    #       The writer should detect the output format from the file extension.

    # TODO: Print a success summary: columns filled, total cells changed, output path.

    click.echo(f"[clean fill] Not yet implemented — source: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
