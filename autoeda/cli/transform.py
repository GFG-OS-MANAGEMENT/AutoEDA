"""
autoeda/cli/transform.py
-------------------------
Click command: `autoeda transform <file>`

Applies mathematical transformations (Log, Box-Cox, Yeo-Johnson, Sqrt, Discretization/Binning)
to continuous variables, outputting before/after skewness diagnostics and optionally exporting
the transformed dataset.
"""

from __future__ import annotations

import click


_TRANSFORM_METHODS = ("log", "boxcox", "yeojohnson", "sqrt", "reciprocal", "bin")


@click.command("transform")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--method",
    "-m",
    default="log",
    show_default=True,
    type=click.Choice(_TRANSFORM_METHODS, case_sensitive=False),
    help=(
        "Transformation method: "
        "'log' applies natural log (log1p); "
        "'boxcox' finds optimal power parameter lambda for positive values; "
        "'yeojohnson' supports positive and negative numbers; "
        "'sqrt' applies square-root; "
        "'reciprocal' applies 1 / x; "
        "'bin' discretizes continuous column into intervals."
    ),
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated column names to transform. Defaults to all numeric columns.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--lambda",
    "lmbda",
    type=float,
    default=None,
    help="Explicit lambda value for Box-Cox or Yeo-Johnson. If omitted, estimated automatically.",
    metavar="FLOAT",
)
@click.option(
    "--bins",
    "n_bins",
    type=int,
    default=5,
    show_default=True,
    help="Number of bins to generate when --method=bin.",
)
@click.option(
    "--output",
    "-o",
    required=False,
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Optional output path to save the transformed dataset.",
    metavar="PATH",
)
@click.option(
    "--inplace",
    is_flag=True,
    default=False,
    help="Overwrite the source dataset with transformed values.",
)
def transform(
    filepath: str,
    method: str,
    columns: str | None,
    lmbda: float | None,
    n_bins: int,
    output: str | None,
    inplace: bool,
) -> None:
    """Transform continuous features to stabilize variance and normalize skew.

    \\b
    Examples:
      autoeda transform data.csv --method log --columns salary,revenue
      autoeda transform data.csv --method boxcox -o transformed.csv
      autoeda transform data.csv --method bin --bins 10 --columns age -o binned.csv
    """
    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Call autoeda.core.transformation.transform_dataset(...).
    # TODO: Render skewness & kurtosis impact comparison table:
    #       - Column | Method | Before Skew | After Skew | Skew Reduced? | Optimal Param
    # TODO: If --output or --inplace is specified, export the transformed dataset.
    click.echo(
        f"[transform] Transforming '{filepath}' using method='{method}' (TODO)"
    )
