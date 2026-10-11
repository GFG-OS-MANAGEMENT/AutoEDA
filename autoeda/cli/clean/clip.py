"""
autoeda/cli/clean/clip.py
-------------------------
Click command: `autoeda clean clip <file>`

Caps / winsorizes numerical outliers to upper and lower bounds based on
IQR fences (Tukey's fences), Z-scores, or fixed percentiles / static thresholds.
"""

from __future__ import annotations

import click


_CLIP_METHODS = ("iqr", "zscore", "percentile", "fixed")


@click.command("clip")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--method",
    "-m",
    default="iqr",
    show_default=True,
    type=click.Choice(_CLIP_METHODS, case_sensitive=False),
    help=(
        "Clipping method: "
        "'iqr' caps values outside Q1 - k*IQR and Q3 + k*IQR; "
        "'zscore' caps values outside mean +/- k*std; "
        "'percentile' caps at lower/upper percentiles (e.g. 1st and 99th); "
        "'fixed' clips between explicit --lower and --upper values."
    ),
)
@click.option(
    "--k",
    default=1.5,
    show_default=True,
    type=float,
    help="Multiplier for IQR (typically 1.5 or 3.0) or Z-score threshold (typically 2.0 or 3.0).",
)
@click.option(
    "--lower",
    type=float,
    default=None,
    help="Explicit lower bound (for fixed method) or lower percentile (e.g. 1.0 for 1st percentile).",
)
@click.option(
    "--upper",
    type=float,
    default=None,
    help="Explicit upper bound (for fixed method) or upper percentile (e.g. 99.0 for 99th percentile).",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated column names to clip. Defaults to all numeric columns.",
    metavar="COL1,COL2,...",
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
def clip(
    filepath: str,
    method: str,
    k: float,
    lower: float | None,
    upper: float | None,
    columns: str | None,
    output: str | None,
    inplace: bool,
) -> None:
    """Clip / winsorize extreme values to prevent outlier distortion.

    \\b
    Examples:
      autoeda clean clip data.csv --method iqr --k 1.5 -o cleaned.csv
      autoeda clean clip data.csv --method percentile --lower 1.0 --upper 99.0 -o cleaned.csv
      autoeda clean clip data.csv --columns salary,age --method fixed --lower 0 --upper 200000 -o cleaned.csv
    """
    if not inplace and output is None:
        raise click.UsageError("Must specify either --output / -o or --inplace.")

    target_path = filepath if inplace else output

    # TODO: Load dataset using autoeda.io.loader.load_file(filepath).
    # TODO: Determine target columns (defaulting to numeric columns if not specified).
    # TODO: Compute clipping boundaries per column:
    #       - IQR: lower_bound = Q1 - k * IQR, upper_bound = Q3 + k * IQR
    #       - Z-score: lower_bound = mean - k * std, upper_bound = mean + k * std
    #       - Percentile: lower_bound = percentile(p_lower), upper_bound = percentile(p_upper)
    #       - Fixed: lower_bound = lower, upper_bound = upper
    # TODO: Apply clipping: for each val, val = max(lower_bound, min(upper_bound, val)).
    # TODO: Report count of clipped values per column to terminal.
    # TODO: Save updated dataset to target_path.
    click.echo(
        f"[clean clip] Clipping outliers using method='{method}' in {filepath} -> {target_path} (TODO)"
    )
