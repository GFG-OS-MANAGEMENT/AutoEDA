"""
tests/conftest.py
-----------------
Shared pytest fixtures for AutoEDA tests.

Fixtures defined here are automatically available to all test modules
without needing an explicit import.
"""

import csv
import os
import pytest


# ---------------------------------------------------------------------------
# Sample dataset fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def sample_csv(tmp_path) -> str:
    """Create a small well-formed CSV file and return its path.

    The file contains a mix of integer, float, string, and datetime columns
    and intentionally includes a few missing values for testing purposes.

    TODO:
    - Expand with more edge-case rows (empty strings, special characters, etc.)
    - Add a second fixture for a TSV file.
    - Add a fixture for a CSV file with all-null columns.
    """
    filepath = tmp_path / "sample.csv"
    rows = [
        ["id", "name",    "age", "salary",  "join_date",  "department"],
        ["1",  "Alice",   "30",  "70000.0", "2020-01-15", "Engineering"],
        ["2",  "Bob",     "25",  "55000.0", "2021-03-22", "Marketing"],
        ["3",  "Charlie", "",    "80000.0", "2019-07-01", "Engineering"],
        ["4",  "Diana",   "28",  "",        "2022-11-05", "HR"],
        ["5",  "Eve",     "35",  "95000.0", "2018-06-30", "Engineering"],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return str(filepath)


@pytest.fixture()
def sample_csv_no_missing(tmp_path) -> str:
    """Create a small CSV file with no missing values.

    TODO: Add more rows for a more robust fixture.
    """
    filepath = tmp_path / "complete.csv"
    rows = [
        ["x", "y", "label"],
        ["1", "10.5", "A"],
        ["2", "20.1", "B"],
        ["3", "30.9", "A"],
        ["4", "40.2", "C"],
    ]
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return str(filepath)
