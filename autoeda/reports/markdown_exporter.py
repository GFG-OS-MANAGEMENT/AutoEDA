"""
autoeda/reports/markdown_exporter.py
--------------------------------------
Generates a Markdown EDA summary report.

Suitable for embedding in GitHub pull requests, wikis, and documentation sites.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from autoeda.reports.report_data import ReportData


def render(report_data: "ReportData", output_path: str) -> None:
    """Generate and write a Markdown EDA report to *output_path*.

    Parameters
    ----------
    report_data:
        Aggregated results from all analysis engines.
    output_path:
        Absolute path where the .md file will be written.

    TODO:
    - Build Markdown sections using f-strings or a string builder:
        # AutoEDA Report — <filename>
        Generated: <timestamp>
        ## Overview
        ## Missing Values
        ## Statistics
        ## Correlation Matrix
        ## Outliers
        ## Categorical Profiles
    - Use GitHub Flavored Markdown (GFM) pipe tables for tabular data.
    - Write the final Markdown string to output_path using
      open(..., "w", encoding="utf-8").
    - Raise IOError with a descriptive message if the file cannot be written.
    """
    # TODO: Implement Markdown report generation.
    raise NotImplementedError("Markdown report renderer is not yet implemented.")
