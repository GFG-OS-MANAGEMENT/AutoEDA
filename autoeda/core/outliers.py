"""
autoeda/core/outliers.py
------------------------
Pure computation engine for outlier detection.

Implements two detection strategies:
  - Tukey's IQR (Interquartile Range) method
  - Standard Z-score thresholding

No rendering or CLI logic lives here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Data models / result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class OutlierRow:
    """A single outlier observation within a column."""

    row_index: int
    value: float
    lower_bound: Optional[float]   # Violated lower bound (or None if upper was violated)
    upper_bound: Optional[float]   # Violated upper bound (or None if lower was violated)


@dataclass
class ColumnOutliers:
    """Outlier detection result for a single column."""

    name: str
    method: str                         # "iqr" or "zscore"
    outlier_count: int
    outliers: List[OutlierRow] = field(default_factory=list)

    # TODO: Add bounds metadata fields, e.g.:
    #   lower_fence: Optional[float]    – Q1 - factor * IQR (IQR method)
    #   upper_fence: Optional[float]    – Q3 + factor * IQR (IQR method)
    #   z_threshold: Optional[float]    – Absolute Z-score cutoff (zscore method)


@dataclass
class OutlierResult:
    """Aggregated outlier detection report for all targeted columns."""

    method: str
    columns: List[ColumnOutliers] = field(default_factory=list)

    @property
    def total_flagged(self) -> int:
        """Return the total number of flagged outlier rows across all columns."""
        # TODO: Sum outlier_count across all ColumnOutliers entries.
        raise NotImplementedError("total_flagged is not yet implemented.")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def detect_iqr(
    data: Any,
    columns: Optional[List[str]] = None,
    factor: float = 1.5,
) -> OutlierResult:
    """Detect outliers using Tukey's IQR method.

    Computes lower_fence = Q1 - factor * IQR and upper_fence = Q3 + factor * IQR.
    Values outside [lower_fence, upper_fence] are flagged as outliers.

    Parameters
    ----------
    data:
        The loaded dataset.
    columns:
        Numerical column names to analyse. Defaults to all numerical columns.
    factor:
        IQR multiplier for whisker width. Commonly 1.5 (mild) or 3.0 (extreme).

    Returns
    -------
    OutlierResult
        Flagged rows per column, ready for rendering.
    """
    # TODO: Filter data to numerical columns (or the provided list).
    # TODO: For each column:
    #   1. Compute Q1 (25th percentile) and Q3 (75th percentile).
    #   2. Compute IQR = Q3 - Q1.
    #   3. Compute lower_fence = Q1 - factor * IQR.
    #   4. Compute upper_fence = Q3 + factor * IQR.
    #   5. Iterate over the column values; for each value outside the fences,
    #      create an OutlierRow with the row index, value, and the violated bound.
    #   6. Build a ColumnOutliers object and append to results.
    # TODO: Return OutlierResult(method="iqr", columns=[...]).
    raise NotImplementedError("detect_iqr() is not yet implemented.")


def detect_zscore(
    data: Any,
    columns: Optional[List[str]] = None,
    threshold: float = 3.0,
) -> OutlierResult:
    """Detect outliers using the standard Z-score method.

    Values where |z| > threshold are flagged as outliers.

    Parameters
    ----------
    data:
        The loaded dataset.
    columns:
        Numerical column names to analyse. Defaults to all numerical columns.
    threshold:
        Absolute Z-score cutoff. Commonly 3.0 (99.7% of a normal distribution).

    Returns
    -------
    OutlierResult
        Flagged rows per column, ready for rendering.
    """
    # TODO: Filter data to numerical columns (or the provided list).
    # TODO: For each column:
    #   1. Compute the column mean (μ) and standard deviation (σ).
    #   2. Skip columns where σ == 0 (constant columns have no outliers by definition).
    #   3. For each value v, compute z = (v - μ) / σ.
    #   4. If abs(z) > threshold, create an OutlierRow and flag the value.
    #      Set lower_bound = μ - threshold * σ and upper_bound = μ + threshold * σ
    #      to indicate which bound was violated.
    #   5. Build a ColumnOutliers object and append to results.
    # TODO: Return OutlierResult(method="zscore", columns=[...]).
    raise NotImplementedError("detect_zscore() is not yet implemented.")
