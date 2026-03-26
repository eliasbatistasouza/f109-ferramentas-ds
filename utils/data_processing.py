from pathlib import Path

import pandas as pd


def clean_dataframe(
    df, remove_nas=True, drop_duplicates=True, reset_index=True
):
    df_clean = df.copy()

    if remove_nas:
        df_clean = df_clean.dropna()

    if drop_duplicates:
        df_clean = df_clean.drop_duplicates()

    if reset_index:
        df_clean = df_clean.reset_index(drop=True)

    return df_clean


def convert_to_datetime(df, columns):
    df_converted = df.copy()

    for col in columns:
        df_converted[col] = pd.to_datetime(df_converted[col])

    return df_converted
