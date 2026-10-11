"""
autoeda/core/correlation.py
---------------------------
Pure computation engine for pairwise column correlation analysis.

Supports Pearson, Spearman, and Kendall rank correlation methods.
No rendering logic lives here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List, Tuple


# ---------------------------------------------------------------------------
# Data models / result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class CollinearPair:
    """A pair of columns whose absolute correlation exceeds the minimum threshold."""

    col_a: str
    col_b: str
    correlation: float   # Signed correlation coefficient value


@dataclass
class CorrelationResult:
    """Full correlation matrix and collinear pair summary."""

    method: str                       # "pearson", "spearman", or "kendall"
    columns: List[str]                # Ordered list of column names (axis labels)
    matrix: List[List[float]]         # n×n correlation matrix (row-major)
    collinear_pairs: List[CollinearPair] = field(default_factory=list)

    # TODO: Add a helper method to retrieve the correlation value between two columns:
    #   def get(self, col_a: str, col_b: str) -> float: ...


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def compute_correlation(
    data: Any,
    method: str = "pearson",
    min_corr: float = 0.0,
) -> CorrelationResult:
    """Compute a pairwise correlation matrix for all numerical columns in *data*.

    Parameters
    ----------
    data:
        The loaded dataset (internal DataResult from autoeda/io/loader.py).
    method:
        Correlation method to use: "pearson", "spearman", or "kendall".
    min_corr:
        Minimum absolute correlation value used to populate collinear_pairs.
        Pairs with |r| >= min_corr (excluding the diagonal) are included.

    Returns
    -------
    CorrelationResult
        Correlation matrix and collinear pair list ready for rendering.
    """
    # TODO: Filter data to numerical columns only.
    # TODO: Validate that at least 2 numerical columns are present; raise a
    #       descriptive ValueError if not.

    # TODO: Compute the n×n correlation matrix using the chosen method:
    #   - "pearson"  → Pearson's r (linear correlation)
    #   - "spearman" → Spearman's ρ (rank-order correlation)
    #   - "kendall"  → Kendall's τ (concordance-based rank correlation)
    #   Each requires a different formula or library call. Implement without
    #   importing pandas; use pure Python or a lightweight math library.

    # TODO: Iterate over the upper triangle of the matrix (i < j).
    #       For each pair (i, j), if abs(matrix[i][j]) >= min_corr,
    #       create a CollinearPair and add it to the list.

    # TODO: Return CorrelationResult(method, columns, matrix, collinear_pairs).
    raise NotImplementedError("compute_correlation() is not yet implemented.")
