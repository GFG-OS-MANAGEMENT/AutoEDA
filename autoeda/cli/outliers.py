"""
autoeda/cli/outliers.py
-----------------------
Click command: `autoeda outliers <file>`

Detects anomalous values in numerical columns using either Tukey's IQR method
or the Z-score method. Prints a report of flagged rows per column.
"""

import click


_OUTLIER_METHODS = ("iqr", "zscore")


@click.command("outliers")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--method",
    "-m",
    default="iqr",
    show_default=True,
    type=click.Choice(_OUTLIER_METHODS, case_sensitive=False),
    help=(
        "Detection method: 'iqr' (Tukey's Interquartile Range, default) or "
        "'zscore' (standard Z-score threshold)."
    ),
)
@click.option(
    "--col",
    "column",
    default=None,
    help="Restrict detection to a single named column. Defaults to all numerical columns.",
    metavar="COLUMN",
)
@click.option(
    "--iqr-factor",
    default=1.5,
    show_default=True,
    type=float,
    help="Multiplier applied to IQR to define the whisker bounds (IQR method only).",
)
@click.option(
    "--z-threshold",
    default=3.0,
    show_default=True,
    type=float,
    help="Absolute Z-score above which a value is flagged as an outlier (zscore method only).",
)
def outliers(
    filepath: str,
    method: str,
    column: str | None,
    iqr_factor: float,
    z_threshold: float,
) -> None:
    """Detect outliers in numerical columns using IQR or Z-score method.

    Prints a summary of flagged rows, the affected column, and the outlier value.

    \b
    Examples:
      autoeda outliers data.csv
      autoeda outliers data.csv --method zscore --z-threshold 2.5
      autoeda outliers data.csv --col salary --method iqr --iqr-factor 2.0
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Determine target columns: if --col is provided validate it exists
    #       and is numerical; otherwise default to all numerical columns.

    # TODO: Based on --method, call the appropriate detector:
    #
    #   if method == "iqr":
    #       result = autoeda.core.outliers.detect_iqr(data, columns, factor=iqr_factor)
    #
    #   elif method == "zscore":
    #       result = autoeda.core.outliers.detect_zscore(data, columns, threshold=z_threshold)
    #
    #   Each detector returns an OutlierResult dataclass (to be defined in
    #   core/outliers.py) with per-column outlier row indices and values.

    # TODO: Call autoeda.renderers.table.render_outlier_report(result) to
    #       print a formatted table of flagged values sorted by column.
    #       Show: column name, row index, outlier value, and the bound that was violated.

    # TODO: Print a final summary line: total flagged rows across all columns.

    click.echo(f"[outliers] Not yet implemented — target file: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
