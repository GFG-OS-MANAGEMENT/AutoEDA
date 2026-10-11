"""
autoeda/core/nulls.py
---------------------
Pure computation engine for missing value (null/NaN) detection.

No rendering or CLI logic lives here — this module only computes missingness
metrics and returns structured result dataclasses.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List


# ---------------------------------------------------------------------------
# Data models / result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class ColumnMissing:
    """Per-column missing value statistics."""

    name: str
    total_rows: int
    missing_count: int
    missing_pct: float    # 0.0 – 100.0
    above_threshold: bool  # True if missing_pct > the threshold supplied by the caller

    # TODO: Add a `dtype` field so renderers can indicate the column type.


@dataclass
class MissingResult:
    """Aggregated missing value report for all columns."""

    total_rows: int
    columns: List[ColumnMissing] = field(default_factory=list)

    @property
    def columns_with_missing(self) -> List[ColumnMissing]:
        """Return only columns that have at least one missing value."""
        # TODO: Implement this filter.
        raise NotImplementedError("columns_with_missing is not yet implemented.")

    @property
    def total_missing_cells(self) -> int:
        """Return the total count of missing cells across the entire dataset."""
        # TODO: Sum missing_count across all columns.
        raise NotImplementedError("total_missing_cells is not yet implemented.")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def compute_missing(data: Any, threshold: float = 0.0) -> MissingResult:
    """Compute per-column missing value counts and percentages.

    Parameters
    ----------
    data:
        The loaded dataset (internal DataResult from autoeda/io/loader.py).
    threshold:
        Percentage threshold (0–100). Columns with missing_pct above this
        value will have `above_threshold=True` in their ColumnMissing entry.

    Returns
    -------
    MissingResult
        Fully populated result object ready for rendering.
    """
    # TODO: Extract total row count from data.
    # TODO: For each column in data:
    #   - count null/NaN values → missing_count
    #   - compute missing_pct = missing_count / total_rows * 100
    #   - set above_threshold = missing_pct > threshold
    #   - construct a ColumnMissing and append to the results list.
    # TODO: Return MissingResult(total_rows=..., columns=[...]).
    raise NotImplementedError("compute_missing() is not yet implemented.")
