"""Unit tests for the DataResult helper methods in autoeda.io.loader."""

import pytest

from autoeda.io.loader import ColumnData, DataResult


def make_result() -> DataResult:
    return DataResult(
        filepath="sample.csv",
        file_format="CSV",
        columns=[
            ColumnData("age", [25, 30, 35], "integer"),
            ColumnData("height", [1.7, 1.8, None], "float"),
            ColumnData("name", ["a", "b", "c"], "string"),
        ],
    )


def test_row_count() -> None:
    assert make_result().row_count == 3


def test_row_count_empty() -> None:
    assert DataResult(filepath="x.csv", file_format="CSV").row_count == 0


def test_column_names() -> None:
    assert make_result().column_names == ["age", "height", "name"]


def test_get_column_found() -> None:
    assert make_result().get_column("age").values == [25, 30, 35]


def test_get_column_missing_raises_key_error() -> None:
    with pytest.raises(KeyError):
        make_result().get_column("missing")


def test_numerical_columns() -> None:
    names = [c.name for c in make_result().numerical_columns()]
    assert names == ["age", "height"]


def test_categorical_columns() -> None:
    names = [c.name for c in make_result().categorical_columns()]
    assert names == ["name"]
