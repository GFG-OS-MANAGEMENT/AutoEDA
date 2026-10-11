"""
autoeda/cli/main.py
-------------------
Root Click group and CLI entrypoint.

The `cli` object here is the top-level Click group that every subcommand
(overview, stats, missing, correlate, outliers, cat, report) is registered on.
It is referenced by the `autoeda` console_script entry-point in pyproject.toml.
"""

import click

from autoeda.cli import (
    cat,
    correlate,
    dist,
    missing,
    normalize,
    outliers,
    overview,
    pca,
    report,
    stats,
    timeseries,
    transform,
    vif,
)
from autoeda.cli.clean import clean


# TODO: Add global Click options that apply to every subcommand, such as:
#   --no-color / --color    Force or disable ANSI color output
#   --output-format         Default output format (table, json, csv)
#   --verbose / -v          Increase logging verbosity
#   --quiet / -q            Suppress all non-essential output

@click.group(
    context_settings={"help_option_names": ["-h", "--help"], "max_content_width": 100}
)
@click.version_option(package_name="autoeda")
def cli() -> None:
    """AutoEDA: Terminal-native Exploratory Data Analysis.

    Run any subcommand with --help for full usage details.

    \b
    Examples:
      autoeda overview  data.csv
      autoeda stats     data.csv --columns age,salary
      autoeda pca       data.csv --n-components 2
      autoeda normalize data.csv --method standard -o scaled.csv
      autoeda transform data.csv --method log -o log_transformed.csv
      autoeda dist      data.csv --test shapiro
      autoeda vif       data.csv --threshold 5.0
      autoeda time      data.csv --date-col timestamp
      autoeda clean     fill data.csv --strategy mean -o cleaned.csv
      autoeda report    data.csv --format html -o report.html
    """
    # TODO: Initialise any global state here (e.g., color theme, log level).
    pass


# Register subcommands
cli.add_command(overview.overview)
cli.add_command(stats.stats)
cli.add_command(missing.missing)
cli.add_command(correlate.correlate)
cli.add_command(outliers.outliers)
cli.add_command(cat.cat)
cli.add_command(normalize.normalize)
cli.add_command(transform.transform)
cli.add_command(pca.pca)
cli.add_command(dist.dist)
cli.add_command(vif.vif)
cli.add_command(timeseries.time_cmd)
cli.add_command(clean)
cli.add_command(report.report)


if __name__ == "__main__":
    cli()
