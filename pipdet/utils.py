import pandas as pd
import numpy as np


def tight_box_normalize_df(
    df: pd.DataFrame, width: float = 1.62, height: float = 1.0
) -> pd.DataFrame:
    """
    Normalize the OHLC data in a DataFrame to fit within a tight box defined by width and height.

    Args:
        df (pd.DataFrame): DataFrame containing OHLC data.
        width (float): Width of the tight box. Default is 1.62.
        height (float): Height of the tight box. Default is 1.0.

    Returns:
        pd.DataFrame: A new DataFrame with normalized OHLC data and an added 'X' column.
    """

    ohlc_cols = ["Open", "High", "Low", "Close"]

    # Copy to avoid modifying original
    df_norm = df.copy()

    # Normalize Y-axis (OHLC)
    maximum = df_norm["High"].max()
    minimum = df_norm["Low"].min()

    df_norm[ohlc_cols] = height * (df_norm[ohlc_cols] - minimum) / (maximum - minimum)

    # Normalize X-axis
    df_norm["X"] = np.linspace(0, width, len(df_norm))

    return df_norm
