"""
utils.py
Reusable utility functions for data cleaning and preprocessing.
"""

import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names in a DataFrame:
    - Converts to lowercase
    - Strips leading/trailing whitespace
    - Replaces spaces with underscores
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
