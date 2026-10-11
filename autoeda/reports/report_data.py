"""
autoeda/reports/report_data.py
-------------------------------
Aggregated report data container.

This dataclass bundles all individual analysis results into a single object
that is passed to report exporters (HTML, Markdown, JSON).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from autoeda.core.summary import OverviewResult, StatsResult, CategoricalResult
    from autoeda.core.nulls import MissingResult
    from autoeda.core.correlation import CorrelationResult
    from autoeda.core.outliers import OutlierResult
    from autoeda.core.pca import PCAResult
    from autoeda.core.distribution import DistributionReport
    from autoeda.core.collinearity import MulticollinearityReport
    from autoeda.core.timeseries import TimeSeriesProfile
    from autoeda.core.normalization import NormalizationResult
    from autoeda.core.transformation import TransformationSummary


@dataclass
class ReportData:
    """Container that bundles all EDA results for report export."""

    filepath: str
    generated_at: str               # ISO 8601 timestamp string

    overview: Optional["OverviewResult"] = None
    stats: Optional["StatsResult"] = None
    missing: Optional["MissingResult"] = None
    correlation: Optional["CorrelationResult"] = None
    outliers: Optional["OutlierResult"] = None
    categorical: Optional["CategoricalResult"] = None
    pca: Optional["PCAResult"] = None
    distributions: Optional["DistributionReport"] = None
    collinearity: Optional["MulticollinearityReport"] = None
    timeseries: Optional["TimeSeriesProfile"] = None
    normalization: Optional["NormalizationResult"] = None
    transformations: Optional["TransformationSummary"] = None

    # TODO: Add an autoeda_version field (imported from autoeda.__version__).
    # TODO: Add a metadata dict for any arbitrary key-value pairs contributors
    #       may want to include in the report (e.g. dataset description, author).
