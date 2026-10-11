"""
autoeda/cli/clean/encode.py
---------------------------
Click command: `autoeda clean encode <file>`

Encodes categorical features into numerical representations using One-Hot Encoding,
Label / Ordinal Encoding, Frequency / Count Encoding, or Binary Encoding.
"""

from __future__ import annotations

import click


_ENCODE_METHODS = ("onehot", "label", "frequency", "binary")


@click.command("encode")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--col",
    "-c",
    "columns",
    required=True,
    help="Comma-separated names of categorical columns to encode.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--method",
    "-m",
    default="onehot",
    show_default=True,
    type=click.Choice(_ENCODE_METHODS, case_sensitive=False),
    help=(
        "Encoding technique: "
        "'onehot' creates binary indicator columns for each category; "
        "'label' assigns integers 0..(K-1) alphabetically or by appearance; "
        "'frequency' replaces categories with their relative frequency or count; "
        "'binary' encodes integer labels into binary bits."
    ),
)
@click.option(
    "--drop-first",
    is_flag=True,
    default=False,
    help="Drop first category in one-hot encoding to avoid dummy variable trap (multicollinearity).",
)
@click.option(
    "--max-categories",
    type=int,
    default=20,
    show_default=True,
    help="Max unique categories to encode before grouping remaining into 'other'.",
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
def encode(
    filepath: str,
    columns: str,
    method: str,
    drop_first: bool,
    max_categories: int,
    output: str | None,
    inplace: bool,
) -> None:
    """Encode categorical columns into machine-learning ready numerical representations.

    \\b
    Examples:
      autoeda clean encode data.csv --col department --method onehot -o cleaned.csv
      autoeda clean encode data.csv --col education_level --method label -o cleaned.csv
      autoeda clean encode data.csv --col city --method frequency --max-categories 15 -o cleaned.csv
    """
    if not inplace and output is None:
        raise click.UsageError("Must specify either --output / -o or --inplace.")

    target_path = filepath if inplace else output

    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Parse target columns and validate existence in dataset.
    # TODO: Execute encoding strategy:
    #       - onehot: create col_<category> binary columns (drop first if requested)
    #       - label: build category -> int mapping dict and map values
    #       - frequency: calculate category counts / total_count and map values
    #       - binary: map category to integer, convert integer to bit columns
    # TODO: Handle unseen / missing categories gracefully (e.g. preserve NaN or assign -1).
    # TODO: Replace or expand columns in dataset schema.
    # TODO: Write updated dataset to target_path.
    click.echo(
        f"[clean encode] Encoding columns '{columns}' using method='{method}' in {filepath} -> {target_path} (TODO)"
    )
