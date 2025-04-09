from chartDL.dataset import Data
import numpy as np


def tight_box_normalize(data: Data, width: float = 1.62, height: float = 1.0):
    """
    Normalize the OHLC data of a Data object to fit within a tight box defined by width and height.

    Args:
        data (Data): Data object containing OHLC data.
        width (float): Width of the tight box. Default is 1.78.
        height (float): Height of the tight box. Default is 1.0.

    Returns:
        Data: A new Data object with normalized OHLC data and added X-coordinates.
    """
    # Extract OHLC data
    ohlc_cols = ["Open", "High", "Low", "Close"]
    ohlc_data = data[ohlc_cols]

    # Normalize Y-axis
    maximum = ohlc_data[:, 1].max()  # Max of "High"
    minimum = ohlc_data[:, 2].min()  # Min of "Low"
    ohlc_data = height * (ohlc_data - minimum) / (maximum - minimum)

    # Normalize X-axis
    x = np.linspace(0, width, len(data), dtype=ohlc_data.dtype)
    normalized_data = np.hstack((ohlc_data, x[:, np.newaxis]))

    # Create the new Data object
    transformed_data = Data(
        timeframe=data.timeframe,
        dt=data.dt,
        data=normalized_data,
        columns=ohlc_cols + ["X"],
        save_in_f32=True,
    )

    return transformed_data
