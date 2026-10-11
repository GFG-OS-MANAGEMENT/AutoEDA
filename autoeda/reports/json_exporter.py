"""
autoeda/reports/json_exporter.py
---------------------------------
Generates a machine-readable JSON EDA report.

Useful for CI/CD integration, downstream tooling, or feeding results into
dashboards and data pipelines.
"""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from autoeda.reports.report_data import ReportData


def render(report_data: "ReportData", output_path: str) -> None:
    """Serialise the full EDA report to a JSON file at *output_path*.

    Parameters
    ----------
    report_data:
        Aggregated results from all analysis engines.
    output_path:
        Absolute path where the .json file will be written.

    TODO:
    - Convert report_data to a pure-Python dict using a helper
      _to_dict(report_data) function (see below).
    - Serialise with json.dump(..., indent=2, ensure_ascii=False) for
      human-readable output.
    - Write to output_path using open(..., "w", encoding="utf-8").
    - Raise IOError with a descriptive message if the file cannot be written.
    """
    # TODO: Implement JSON report generation.
    raise NotImplementedError("JSON report renderer is not yet implemented.")


def _to_dict(report_data: "ReportData") -> dict:
    """Convert a ReportData object into a plain serialisable Python dict.

    TODO:
    - Traverse all result sub-objects (OverviewResult, StatsResult, etc.)
      and convert each dataclass to a dict using dataclasses.asdict() or
      manual field extraction.
    - Ensure all values are JSON-serialisable (float, int, str, list, dict, None).
    - Handle special cases: NaN and Infinity should be serialised as null.
    """
    # TODO: Implement the dict conversion.
    raise NotImplementedError("_to_dict() is not yet implemented.")
