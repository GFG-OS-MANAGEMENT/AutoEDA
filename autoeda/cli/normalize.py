"""
autoeda/cli/normalize.py
-------------------------
Click command: `autoeda normalize <file>`

Scales numerical features using Min-Max, Z-score Standardization, Robust (IQR),
or Max-Abs normalization, outputting comparison summary tables and optionally
exporting the scaled dataset.
"""

from __future__ import annotations

import click


_SCALING_METHODS = ("minmax", "standard", "robust", "maxabs")


@click.command("normalize")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--method",
    "-m",
    default="standard",
    show_default=True,
    type=click.Choice(_SCALING_METHODS, case_sensitive=False),
    help=(
        "Normalization / scaling technique: "
        "'standard' standardizes to mean=0, std=1 (Z-score); "
        "'minmax' rescales values to [lower, upper] range; "
        "'robust' scales via median and IQR (outlier resilient); "
        "'maxabs' scales to [-1, 1] by dividing by max absolute value."
    ),
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated column names to normalize. Defaults to all numeric columns.",
    metavar="COL1,COL2,...",
)
@click.option(
    "--range",
    "feature_range",
    default="0.0,1.0",
    show_default=True,
    help="Target lower and upper bounds for --method=minmax, formatted as 'LOWER,UPPER'.",
    metavar="MIN,MAX",
)
@click.option(
    "--output",
    "-o",
    required=False,
    type=click.Path(dir_okay=False, writable=True, resolve_path=True),
    help="Optional output path to export the normalized dataset (CSV, Parquet, JSON).",
    metavar="PATH",
)
@click.option(
    "--inplace",
    is_flag=True,
    default=False,
    help="Overwrite the source dataset with normalized values. Use with caution.",
)
def normalize(
    filepath: str,
    method: str,
    columns: str | None,
    feature_range: str,
    output: str | None,
    inplace: bool,
) -> None:
    """Normalize and scale numerical features for machine learning and EDA.

    \\b
    Examples:
      autoeda normalize data.csv --method standard
      autoeda normalize data.csv --method minmax --range "-1.0,1.0" -o scaled.csv
      autoeda normalize data.csv --columns age,income --method robust -o robust.csv
    """
    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Parse feature_range string "0.0,1.0" into tuple (float, float).
    # TODO: Call autoeda.core.normalization.normalize_dataset(...) with parsed options.
    # TODO: Render before vs after comparison table in terminal:
    #       - Column | Method | Orig Mean +/- Std | Orig [Min, Max] | Scaled [Min, Max]
    # TODO: If --output or --inplace is specified, export the scaled dataset.
    click.echo(
        f"[normalize] Normalizing '{filepath}' using method='{method}' (range: {feature_range}) (TODO)"
    )
