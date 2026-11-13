"""
tests/test_io_loader.py
------------------------
Unit tests for autoeda.io.loader — format detection and file loading.
"""

import csv
import os
import pytest

from autoeda.io.loader import detect_format, load_file


# ---------------------------------------------------------------------------
# detect_format() tests
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("filename,expected", [
    ("data.csv",     "CSV"),
    ("data.tsv",     "TSV"),
    ("data.parquet", "Parquet"),
    ("data.json",    "JSON"),
    ("data.jsonl",   "JSON Lines"),
    ("data.xlsx",    "Excel"),
    ("data.xls",     "Excel"),
    ("data.feather", "Feather"),
])
def test_detect_format_known_extensions(filename: str, expected: str) -> None:
    """detect_format() should correctly identify known extensions."""
    assert detect_format(filename) == expected


def test_detect_format_unknown_extension() -> None:
    """detect_format() should raise ValueError for unsupported extensions."""
    with pytest.raises(ValueError, match="Unsupported file extension"):
        detect_format("data.txt")


def test_detect_format_case_insensitive() -> None:
    """detect_format() should handle uppercase extensions gracefully."""
    assert detect_format("DATA.CSV") == "CSV"
    assert detect_format("archive.PARQUET") == "Parquet"


# ---------------------------------------------------------------------------
# load_file() tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Not yet implemented — remove skip when _read_csv() is done.")
def test_load_csv_basic(sample_csv: str) -> None:
    """load_file() should load a CSV and return a DataResult with correct shape."""
    result = load_file(sample_csv)
    assert result.row_count == 5   # Adjust to fixture row count.
    assert len(result.columns) == 6  # Adjust to fixture column count.
    # TODO: Assert column names match expectations.
    # TODO: Assert inferred dtypes are reasonable (age → integer, name → string).


@pytest.mark.skip(reason="Not yet implemented — remove skip when _read_csv() is done.")
def test_load_csv_missing_values(sample_csv: str) -> None:
    """load_file() should represent empty CSV cells as None in ColumnData.values."""
    result = load_file(sample_csv)
    age_col = result.get_column("age")
    assert None in age_col.values


def test_load_file_not_found() -> None:
    """load_file() should raise FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        load_file("/nonexistent/path/data.csv")
