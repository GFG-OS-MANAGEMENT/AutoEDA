"""
autoeda/cli/clean/cast.py
--------------------------
Click command: `autoeda clean cast <file>`

Casts one or more columns to specified data types (integer, float, string,
boolean, datetime), handling parsing errors and invalid values gracefully.
"""

from __future__ import annotations

import click


_SUPPORTED_DTYPES = ("integer", "float", "string", "boolean", "datetime")
_ERROR_STRATEGIES = ("raise", "coerce", "ignore")


@click.command("cast")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--col",
    "-c",
    "column",
    required=True,
    help="Name of the column to type-cast.",
    metavar="COLUMN",
)
@click.option(
    "--to",
    "target_dtype",
    required=True,
    type=click.Choice(_SUPPORTED_DTYPES, case_sensitive=False),
    help="Target data type to cast to.",
)
@click.option(
    "--errors",
    default="coerce",
    show_default=True,
    type=click.Choice(_ERROR_STRATEGIES, case_sensitive=False),
    help=(
        "How to handle parsing errors: "
        "'coerce' sets unparseable values to None/null; "
        "'raise' fails execution on first invalid value; "
        "'ignore' retains original value."
    ),
)
@click.option(
    "--date-format",
    default=None,
    help="Optional strftime format string (e.g. '%Y-%m-%d') when casting to datetime.",
    metavar="FORMAT",
)
@click.option(
    "--output",
    "-o",
    required=False,
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Path for the output (cleaned) file. Required unless --inplace is passed.",
    metavar="PATH",
)
@click.option(
    "--inplace",
    is_flag=True,
    default=False,
    help="Overwrite the source file instead of writing to --output.",
)
def cast(
    filepath: str,
    column: str,
    target_dtype: str,
    errors: str,
    date_format: str | None,
    output: str | None,
    inplace: bool,
) -> None:
    """Type-cast a column to integer, float, string, boolean, or datetime.

    \\b
    Examples:
      autoeda clean cast data.csv --col age --to integer -o cleaned.csv
      autoeda clean cast data.csv --col price --to float --errors coerce -o cleaned.csv
      autoeda clean cast data.csv --col signup_date --to datetime --date-format "%Y-%m-%d" -o cleaned.csv
    """
    if not inplace and output is None:
        raise click.UsageError("Must specify either --output / -o or --inplace.")

    target_path = filepath if inplace else output

    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Validate that `column` exists in data.columns.
    # TODO: Execute type casting logic:
    #       - integer: parse via int(float(val)), handle float strings like "12.0"
    #       - float: parse via float(val)
    #       - string: str(val) if val is not None else None
    #       - boolean: truthy string parsing ("true", "1", "yes", "t") vs ("false", "0", "no", "f")
    #       - datetime: datetime.strptime() if date_format else dateutil.parser
    # TODO: Handle errors:
    #       - coerce: set failed conversions to None
    #       - raise: raise ValueError with row index and bad value
    #       - ignore: keep raw value unchanged
    # TODO: Write output using appropriate autoeda exporter.
    click.echo(
        f"[clean cast] Casting column '{column}' to {target_dtype} in {filepath} -> {target_path} (TODO)"
    )
