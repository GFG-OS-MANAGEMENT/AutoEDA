"""
autoeda/cli/clean/__init__.py
------------------------------
`autoeda clean` — Click sub-group for data cleaning & transformation commands.

All clean commands READ a source file, apply a transformation, and WRITE the
result to an output file. The source file is NEVER modified in place unless
--inplace is explicitly passed.
"""

import click

from autoeda.cli.clean import fill, drop, dedup, cast, rename, clip, encode


@click.group("clean")
def clean() -> None:
    """Data cleaning and transformation commands.

    Each subcommand reads a dataset, applies a transformation, and writes the
    result to a new file. The original file is never overwritten unless you
    explicitly pass --inplace.

    \b
    Examples:
      autoeda clean fill   data.csv --strategy mean -o cleaned.csv
      autoeda clean drop   data.csv --threshold 50.0 -o cleaned.csv
      autoeda clean dedup  data.csv -o cleaned.csv
      autoeda clean cast   data.csv --col age --to integer -o cleaned.csv
      autoeda clean encode data.csv --col department --method onehot -o cleaned.csv
    """
    pass


# Register all cleaning subcommands under the clean group
clean.add_command(fill.fill)
clean.add_command(drop.drop)
clean.add_command(dedup.dedup)
clean.add_command(cast.cast)
clean.add_command(rename.rename)
clean.add_command(clip.clip)
clean.add_command(encode.encode)
