"""
autoeda/cli/correlate.py
------------------------
Click command: `autoeda correlate <file>`

Computes a pairwise correlation matrix for numerical columns and renders a
colour-coded terminal heatmap. Supports Pearson, Spearman, and Kendall methods.
Flags collinear pairs whose absolute correlation exceeds a configurable minimum.
"""

import click


_CORRELATION_METHODS = ("pearson", "spearman", "kendall")


@click.command("correlate")
@click.argument(
    "filepath",
    type=click.Path(exists=True, dir_okay=False, readable=True, resolve_path=True),
)
@click.option(
    "--method",
    "-m",
    default="pearson",
    show_default=True,
    type=click.Choice(_CORRELATION_METHODS, case_sensitive=False),
    help="Correlation coefficient method to use.",
)
@click.option(
    "--min",
    "min_corr",
    default=0.0,
    show_default=True,
    type=click.FloatRange(min=0.0, max=1.0),
    help=(
        "Minimum absolute correlation value to include in the collinearity "
        "report. Pairs below this threshold are not flagged."
    ),
    metavar="FLOAT",
)
@click.option(
    "--columns",
    "-c",
    default=None,
    help="Comma-separated list of numerical columns to include. Defaults to all numerical columns.",
    metavar="COL1,COL2,...",
)
def correlate(filepath: str, method: str, min_corr: float, columns: str | None) -> None:
    """Compute a pairwise correlation matrix and display a terminal heatmap.

    Collinear pairs (|r| >= --min) are listed below the matrix for review.

    \b
    Examples:
      autoeda correlate data.csv
      autoeda correlate data.csv --method spearman --min 0.7
      autoeda correlate data.csv --columns age,salary,score
    """
    # TODO: Call autoeda.io.loader.load_file(filepath) to load the dataset.

    # TODO: Filter to numerical columns only; optionally further filter by
    #       --columns if provided. Raise click.BadParameter if any specified
    #       column is non-numerical or doesn't exist.

    # TODO: Call autoeda.core.correlation.compute_correlation(data, method)
    #       to compute the full pairwise correlation matrix.
    #       Return a CorrelationResult dataclass (to be defined in core/correlation.py)
    #       containing the n×n matrix and column labels.

    # TODO: Call autoeda.renderers.table.render_correlation_heatmap(result)
    #       to print a colour-coded heatmap in the terminal.
    #       Positive high correlations → green; negative strong → red; weak → neutral.

    # TODO: Extract collinear pairs from the matrix where abs(r) >= min_corr
    #       (excluding the diagonal). Call
    #       autoeda.renderers.table.render_collinear_pairs(pairs)
    #       to print a summary table of flagged pairs.

    click.echo(f"[correlate] Not yet implemented — target file: {filepath}")
    raise click.ClickException("This command is not yet implemented. See TODO comments.")
