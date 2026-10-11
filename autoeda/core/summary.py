"""
autoeda/core/summary.py
-----------------------
Pure computation engine for descriptive and overview statistics.

This module is entirely free of CLI / rendering concerns.
All functions receive a raw dataset (dict-of-lists or equivalent internal
representation) and return structured result dataclasses that the CLI layer
passes to renderers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Data models / result dataclasses
# ---------------------------------------------------------------------------

@dataclass
class ColumnOverview:
    """Per-column metadata produced by compute_overview()."""

    name: str
    dtype: str               # e.g. "integer", "float", "string", "datetime", "boolean"
    missing_count: int
    missing_pct: float       # 0.0 – 100.0
    distinct_count: int

    # TODO: Add additional fields as needed, e.g.:
    #   sample_values: List[Any]   – first N non-null values


@dataclass
class OverviewResult:
    """Top-level dataset overview returned by compute_overview()."""

    filepath: str
    file_format: str         # e.g. "CSV", "Parquet"
    row_count: int
    column_count: int
    memory_mb: float
    duplicate_row_count: int
    columns: List[ColumnOverview] = field(default_factory=list)

    # TODO: Add file size in bytes field.


@dataclass
class ColumnStats:
    """Per-column descriptive statistics returned by compute_stats()."""

    name: str
    dtype: str
    count: int
    mean: Optional[float]
    median: Optional[float]
    mode: Optional[Any]
    std: Optional[float]
    variance: Optional[float]
    min: Optional[float]
    max: Optional[float]
    skewness: Optional[float]
    kurtosis: Optional[float]
    iqr: Optional[float]
    percentiles: Dict[float, float] = field(default_factory=dict)  # {25.0: val, 50.0: val, ...}

    # TODO: Add top_values field for categorical columns:
    #   top_values: Optional[List[Tuple[Any, int]]]  – [(value, count), ...]


@dataclass
class StatsResult:
    """Aggregated statistics for all requested columns."""

    columns: List[ColumnStats] = field(default_factory=list)


@dataclass
class CategoricalStats:
    """Frequency profile for a single categorical column."""

    name: str
    distinct_count: int
    top_values: List[tuple]   # [(value, count, pct), ...]

    # TODO: Add least_common_values field.


@dataclass
class CategoricalResult:
    """Aggregated categorical profiles for all requested columns."""

    columns: List[CategoricalStats] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def compute_overview(data: Any, filepath: str = "", file_format: str = "") -> OverviewResult:
    """Compute a high-level diagnostic overview of *data*.

    Parameters
    ----------
    data:
        The loaded dataset. Type will depend on the internal DataResult
        abstraction defined in autoeda/io/loader.py (to be implemented).
    filepath:
        Original file path, stored in the result for display purposes.
    file_format:
        Detected file format string (e.g. "CSV").

    Returns
    -------
    OverviewResult
        Fully populated result object ready for rendering.
    """
    # TODO: Extract row count from data.
    # TODO: Extract column count from data.
    # TODO: Compute memory usage in MB.
    # TODO: Compute duplicate row count.
    # TODO: For each column, determine dtype, missing_count, missing_pct, distinct_count.
    #       Populate a list of ColumnOverview objects.
    # TODO: Return a fully populated OverviewResult.
    raise NotImplementedError("compute_overview() is not yet implemented.")


def compute_stats(
    data: Any,
    columns: Optional[List[str]] = None,
    percentiles: Optional[List[float]] = None,
) -> StatsResult:
    """Compute descriptive statistics for numerical and categorical columns.

    Parameters
    ----------
    data:
        The loaded dataset.
    columns:
        Column names to include. If None, include all columns.
    percentiles:
        Percentile breakpoints to compute, e.g. [25.0, 50.0, 75.0].

    Returns
    -------
    StatsResult
        Per-column statistics ready for rendering.
    """
    # TODO: Default percentiles to [25.0, 50.0, 75.0] if not provided.
    # TODO: Filter data to requested columns.
    # TODO: For each numerical column compute:
    #   count, mean, median, mode, std, variance, min, max, skewness, kurtosis, IQR.
    #   percentile values for each p in percentiles.
    # TODO: For each categorical column compute: count, mode, top values.
    # TODO: Return StatsResult populated with a list of ColumnStats.
    raise NotImplementedError("compute_stats() is not yet implemented.")


def compute_categorical_stats(
    data: Any,
    columns: Optional[List[str]] = None,
    top_n: int = 10,
) -> CategoricalResult:
    """Compute frequency distributions for categorical columns.

    Parameters
    ----------
    data:
        The loaded dataset.
    columns:
        Categorical column names to profile. Defaults to all string columns.
    top_n:
        Number of most frequent values to include per column.

    Returns
    -------
    CategoricalResult
        Per-column frequency profiles ready for rendering.
    """
    # TODO: Filter to categorical/string columns only (or the provided list).
    # TODO: For each column, compute distinct value count and value frequency table.
    # TODO: Sort by frequency descending and take the top_n entries.
    #       Store as list of (value, count, pct) tuples.
    # TODO: Return CategoricalResult populated with CategoricalStats objects.
    raise NotImplementedError("compute_categorical_stats() is not yet implemented.")
