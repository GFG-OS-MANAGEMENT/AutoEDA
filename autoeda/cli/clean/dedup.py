"""
autoeda/cli/clean/dedup.py
---------------------------
Click command: `autoeda clean dedup <file>`

Identifies and removes duplicate rows from a dataset. Supports keeping the
first, last, or no occurrence of each duplicate group.
"""

import click


@click.command("dedup")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--keep",
    default="first",
    show_default=True,
    type=click.Choice(["first", "last", "none"], case_sensitive=False),
    help=(
        "Which occurrence to keep: 'first' (keep first), 'last' (keep last), "
        "'none' (drop all duplicates)."
    ),
)
@click.option(
    "--subset",
    default=None,
    help="Comma-separated column names to consider when identifying duplicates. Defaults to all columns.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--output",
    "-o",
    required=True,
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Path for the output (deduplicated) file.",
    metavar="PATH",
)
def dedup(
    filepath: str,
    keep: str,
    subset: str | None,
    output: str,
) -> None:
    """Remove duplicate rows from the dataset.

    \b
    Examples:
      autoeda clean dedup data.csv -o cleaned.csv
      autoeda clean dedup data.csv --keep last -o cleaned.csv
      autoeda clean dedup data.csv --subset "name,email" -o cleaned.csv
      autoeda clean dedup data.csv --keep none -o cleaned.csv
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Parse --subset: split by comma, validate each column name exists.
    #       If None, use all columns for duplicate comparison.

    # TODO: Call autoeda.core.cleaning.remove_duplicates(data, subset, keep)
    #       to identify and remove duplicate rows.
    #       - "first"  → mark all duplicates except first occurrence for removal
    #       - "last"   → mark all duplicates except last occurrence for removal
    #       - "none"   → mark all occurrences of any duplicate group for removal

    # TODO: Call autoeda.io.writer.write_file(cleaned_data, output).

    # TODO: Print a summary: total rows before, duplicate rows removed, rows after.

    click.echo(f"[clean dedup] Not yet implemented — source: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
