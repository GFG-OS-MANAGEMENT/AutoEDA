"""
autoeda/cli/clean/rename.py
----------------------------
Click command: `autoeda clean rename <file>`

Renames one or multiple columns using explicit key=value pairs, a JSON/YAML mapping file,
or string transformations (lowercase, uppercase, snake_case, strip whitespace).
"""

from __future__ import annotations

import click


_CASE_TRANSFORMS = ("lower", "upper", "snake", "strip")


@click.command("rename")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--map",
    "-m",
    "mappings",
    multiple=True,
    help="Column rename pair in format 'OLD=NEW'. Can be specified multiple times.",
    metavar="OLD=NEW",
)
@click.option(
    "--case",
    type=click.Choice(_CASE_TRANSFORMS, case_sensitive=False),
    default=None,
    help="Apply bulk case transformation to all column names: lower, upper, snake, strip.",
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
def rename(
    filepath: str,
    mappings: tuple[str, ...],
    case: str | None,
    output: str | None,
    inplace: bool,
) -> None:
    """Rename columns explicitly or apply case transformations (snake_case, lower, etc.).

    \\b
    Examples:
      autoeda clean rename data.csv -m "Old Col=new_col" -m "Age=patient_age" -o cleaned.csv
      autoeda clean rename data.csv --case snake -o cleaned.csv
      autoeda clean rename data.csv --case lower --inplace
    """
    if not inplace and output is None:
        raise click.UsageError("Must specify either --output / -o or --inplace.")

    if not mappings and case is None:
        raise click.UsageError("Must provide at least one --map OLD=NEW or a --case transform.")

    target_path = filepath if inplace else output

    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Parse mappings: split "OLD=NEW" by "=", validate old columns exist.
    # TODO: If --case is set:
    #       - lower: col.lower()
    #       - upper: col.upper()
    #       - strip: col.strip()
    #       - snake: re.sub(r'[\s\-]+', '_', col).lower()
    # TODO: Apply explicit mappings after case transformations.
    # TODO: Check for resulting duplicate column names and raise error if detected.
    # TODO: Save updated dataset to target_path.
    click.echo(
        f"[clean rename] Renaming columns in {filepath} -> {target_path} (TODO)"
    )
