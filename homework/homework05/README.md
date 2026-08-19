# Homework 05 — Data Storage

## Data Storage

**Folder structure:** `data/raw/` holds the original data as CSV; `data/processed/` holds the same data as Parquet.

**Formats:** CSV for raw data (simple, human-readable). Parquet for processed data (compressed, faster, preserves dtypes better).

**Env-driven paths:** Folder locations come from `.env` (`DATA_DIR_RAW`, `DATA_DIR_PROCESSED`), loaded via `os.getenv()` — no hardcoded paths in the code.

**Utilities:** `write_df()`/`read_df()` auto-detect CSV vs Parquet by file extension, and raise a clear error if the Parquet engine is missing.

**Validation:** Reloaded CSV and Parquet files were checked for matching shape and correct dtypes (date, price) — all checks passed.