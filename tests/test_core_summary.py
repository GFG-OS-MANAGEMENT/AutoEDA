"""
tests/test_core_summary.py
---------------------------
Unit tests for autoeda.core.summary — descriptive statistics engines.

Tests target pure computation functions in isolation, with no CLI involvement.
Use the sample DataResult objects defined in fixtures, not real file I/O.
"""

import pytest

# TODO: Once autoeda.io.loader.DataResult is implemented, import it here:
# from autoeda.io.loader import DataResult, ColumnData
from autoeda.core.summary import compute_overview, compute_stats, compute_categorical_stats


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

# TODO: Create a helper fixture that builds a lightweight in-memory DataResult
#       without reading from disk. Example:
#
# @pytest.fixture()
# def simple_data() -> DataResult:
#     return DataResult(
#         filepath="test.csv",
#         file_format="CSV",
#         columns=[
#             ColumnData(name="age",  values=[25, 30, None, 35], inferred_dtype="integer"),
#             ColumnData(name="name", values=["Alice", "Bob", "Charlie", "Diana"],
#                        inferred_dtype="string"),
#         ],
#     )


# ---------------------------------------------------------------------------
# compute_overview tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_overview() is done.")
def test_overview_row_count(simple_data) -> None:
    """compute_overview() should correctly count the number of rows."""
    result = compute_overview(simple_data)
    assert result.row_count == 4  # TODO: adjust to fixture size.


@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_overview() is done.")
def test_overview_column_count(simple_data) -> None:
    """compute_overview() should correctly count the number of columns."""
    result = compute_overview(simple_data)
    assert result.column_count == 2  # TODO: adjust to fixture size.


@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_overview() is done.")
def test_overview_missing_detection(simple_data) -> None:
    """compute_overview() should detect None values in the 'age' column."""
    result = compute_overview(simple_data)
    age_col = next(c for c in result.columns if c.name == "age")
    assert age_col.missing_count == 1
    assert age_col.missing_pct == pytest.approx(25.0)


# ---------------------------------------------------------------------------
# compute_stats tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_stats() is done.")
def test_stats_mean(simple_data) -> None:
    """compute_stats() should compute the correct mean for a numerical column."""
    result = compute_stats(simple_data, columns=["age"])
    age_stats = next(c for c in result.columns if c.name == "age")
    # Mean of [25, 30, 35] ignoring None = 30.0
    assert age_stats.mean == pytest.approx(30.0)


@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_stats() is done.")
def test_stats_std(simple_data) -> None:
    """compute_stats() should compute the correct standard deviation."""
    # TODO: Implement and assert std value.
    pass


@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_stats() is done.")
def test_stats_percentiles(simple_data) -> None:
    """compute_stats() should return the requested percentile values."""
    result = compute_stats(simple_data, columns=["age"], percentiles=[50.0])
    age_stats = next(c for c in result.columns if c.name == "age")
    assert 50.0 in age_stats.percentiles
    # TODO: Assert the 50th percentile value.


# ---------------------------------------------------------------------------
# compute_categorical_stats tests
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_categorical_stats() is done.")
def test_categorical_distinct_count(simple_data) -> None:
    """compute_categorical_stats() should return the correct distinct value count."""
    result = compute_categorical_stats(simple_data, columns=["name"])
    name_stats = next(c for c in result.columns if c.name == "name")
    assert name_stats.distinct_count == 4  # 4 unique names.


@pytest.mark.skip(reason="Not yet implemented — remove skip once compute_categorical_stats() is done.")
def test_categorical_top_values(simple_data) -> None:
    """compute_categorical_stats() top_values should be sorted by frequency desc."""
    result = compute_categorical_stats(simple_data, columns=["name"], top_n=2)
    name_stats = next(c for c in result.columns if c.name == "name")
    assert len(name_stats.top_values) <= 2
    # TODO: Assert first entry has count >= second entry count.
