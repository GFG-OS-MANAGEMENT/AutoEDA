"""
autoeda/io/loader.py
--------------------
Multi-format dataset loader.

Detects the file format from the file extension, dispatches to the appropriate
reader, and returns a normalised internal DataResult object that all core
engines consume.

Supported formats
-----------------
  .csv / .tsv   → CSV reader
  .parquet      → Parquet reader
  .json         → JSON reader
  .jsonl        → JSON Lines reader
  .xlsx / .xls  → Excel reader
  .feather      → Feather / Arrow reader
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Internal data model
# ---------------------------------------------------------------------------

@dataclass
class ColumnData:
    """Raw data for a single column."""

    name: str
    values: List[Any]              # Raw Python list of column values (may include None)
    inferred_dtype: str = "unknown"  # e.g. "integer", "float", "string", "datetime", "boolean"

    # TODO: Add a `null_marker` field if special sentinel values (e.g. "N/A", "-")
    #       need to be normalised to None during loading.


@dataclass
class DataResult:
    """Normalised dataset returned by load_file().

    Acts as the single contract between the I/O layer and the core engines.
    All core functions accept a DataResult as their `data` argument.
    """

    filepath: str
    file_format: str                           # e.g. "CSV", "Parquet"
    columns: List[ColumnData] = field(default_factory=list)

    @property
    def row_count(self) -> int:
        """Return the number of rows in the dataset."""
        # TODO: Return len(self.columns[0].values) if columns exist, else 0.
        raise NotImplementedError("row_count is not yet implemented.")

    @property
    def column_names(self) -> List[str]:
        """Return an ordered list of all column names."""
        # TODO: Return [c.name for c in self.columns].
        raise NotImplementedError("column_names is not yet implemented.")

    def get_column(self, name: str) -> ColumnData:
        """Retrieve a ColumnData by name, raising KeyError if not found."""
        # TODO: Search self.columns for a matching name and return it.
        raise NotImplementedError("get_column() is not yet implemented.")

    def numerical_columns(self) -> List[ColumnData]:
        """Return only columns with dtype 'integer' or 'float'."""
        # TODO: Filter self.columns by inferred_dtype in {"integer", "float"}.
        raise NotImplementedError("numerical_columns() is not yet implemented.")

    def categorical_columns(self) -> List[ColumnData]:
        """Return only columns with dtype 'string'."""
        # TODO: Filter self.columns by inferred_dtype == "string".
        raise NotImplementedError("categorical_columns() is not yet implemented.")


# ---------------------------------------------------------------------------
# Format detection
# ---------------------------------------------------------------------------

#: Maps lowercase file extension → canonical format name
_EXTENSION_FORMAT_MAP: Dict[str, str] = {
    ".csv":     "CSV",
    ".tsv":     "TSV",
    ".parquet": "Parquet",
    ".json":    "JSON",
    ".jsonl":   "JSON Lines",
    ".xlsx":    "Excel",
    ".xls":     "Excel",
    ".feather": "Feather",
    ".arrow":   "Arrow",
}


def detect_format(filepath: str) -> str:
    """Detect the file format from the file extension.

    Parameters
    ----------
    filepath:
        Absolute or relative path to the data file.

    Returns
    -------
    str
        Canonical format name (e.g. "CSV", "Parquet").

    Raises
    ------
    ValueError
        If the extension is not recognised.
    """
    _, ext = os.path.splitext(filepath)
    fmt = _EXTENSION_FORMAT_MAP.get(ext.lower())
    if fmt is None:
        raise ValueError(
            f"Unsupported file extension '{ext}'. "
            f"Supported formats: {', '.join(_EXTENSION_FORMAT_MAP)}"
        )
    return fmt


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_file(filepath: str) -> DataResult:
    """Load a dataset file and return a normalised DataResult.

    Automatically detects the format from the file extension and dispatches
    to the appropriate reader function.

    Parameters
    ----------
    filepath:
        Path to the data file. Must exist and be readable.

    Returns
    -------
    DataResult
        Normalised dataset with inferred column dtypes.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the file extension is not supported.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: '{filepath}'")

    file_format = detect_format(filepath)

    # TODO: Dispatch to the correct reader based on file_format:
    #
    #   if file_format in ("CSV", "TSV"):
    #       return _read_csv(filepath, file_format)
    #   elif file_format == "Parquet":
    #       return _read_parquet(filepath)
    #   elif file_format in ("JSON", "JSON Lines"):
    #       return _read_json(filepath, file_format)
    #   elif file_format == "Excel":
    #       return _read_excel(filepath)
    #   elif file_format in ("Feather", "Arrow"):
    #       return _read_feather(filepath)

    raise NotImplementedError(f"Loader for format '{file_format}' is not yet implemented.")


# ---------------------------------------------------------------------------
# Private reader stubs (one per format)
# ---------------------------------------------------------------------------

def _read_csv(filepath: str, file_format: str = "CSV") -> DataResult:
    """Read a CSV or TSV file into a DataResult.

    TODO:
    - Open the file using the built-in `csv` module (no pandas).
    - Auto-detect delimiter: comma for .csv, tab for .tsv; or sniff with csv.Sniffer.
    - Parse the header row as column names.
    - Read remaining rows and build per-column value lists.
    - Call _infer_dtype() on each column's values to populate inferred_dtype.
    - Return a DataResult.
    """
    raise NotImplementedError("_read_csv() is not yet implemented.")


def _read_parquet(filepath: str) -> DataResult:
    """Read a Parquet file into a DataResult.

    TODO:
    - Use a lightweight Parquet reader (e.g. pyarrow or fastparquet) to read
      the file into a columnar format.
    - Map Arrow/Parquet types to AutoEDA dtype strings.
    - Extract per-column value lists.
    - Return a DataResult.
    """
    raise NotImplementedError("_read_parquet() is not yet implemented.")


def _read_json(filepath: str, file_format: str = "JSON") -> DataResult:
    """Read a JSON or JSON Lines file into a DataResult.

    TODO:
    - For JSON: parse the entire file with the `json` stdlib module.
      Expect a list of objects (records) or a dict-of-lists format.
    - For JSON Lines: parse line-by-line, accumulating records.
    - Transpose records into column-oriented lists.
    - Call _infer_dtype() on each column.
    - Return a DataResult.
    """
    raise NotImplementedError("_read_json() is not yet implemented.")


def _read_excel(filepath: str) -> DataResult:
    """Read an Excel (.xlsx / .xls) file into a DataResult.

    TODO:
    - Use openpyxl (for .xlsx) or xlrd (for .xls) to read the active sheet.
    - Parse the first row as column headers.
    - Read remaining rows into per-column value lists.
    - Call _infer_dtype() on each column.
    - Return a DataResult.
    """
    raise NotImplementedError("_read_excel() is not yet implemented.")


def _read_feather(filepath: str) -> DataResult:
    """Read a Feather / Arrow file into a DataResult.

    TODO:
    - Use pyarrow.feather or pyarrow.ipc to read the file.
    - Map Arrow types to AutoEDA dtype strings.
    - Extract per-column value lists.
    - Return a DataResult.
    """
    raise NotImplementedError("_read_feather() is not yet implemented.")


def _infer_dtype(values: List[Any]) -> str:
    """Infer a human-readable dtype string from a list of raw values.

    Heuristic detection order: boolean → integer → float → datetime → string.

    TODO:
    - Skip None values during inference.
    - Attempt to cast a sample of non-null values to int, then float.
    - Attempt to parse as ISO datetime if string.
    - Fall back to "string" if no numeric or datetime match.
    - Return one of: "boolean", "integer", "float", "datetime", "string".
    """
    raise NotImplementedError("_infer_dtype() is not yet implemented.")
