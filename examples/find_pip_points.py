from pipdet.pip import FastPip
from chartDL.utils.csv import import_ohlcv_from_csv
from pathlib import Path

# Import source DataFrame
csv_source_path = Path("./DATA/csv/EURUSD-1h.csv")
if not csv_source_path.exists():
    raise FileNotFoundError(f"File not found: {csv_source_path}")

# Assumes the CSV contains OHLCV (Open-High-Low-Close-Volume) data with a 'datetime' column.
df_source = import_ohlcv_from_csv(
    csv_source_path, header=True, datetime_format="%Y-%m-%d %H:%M:%S"
)

# get ohlcv sample data and normalize them
market_data = df_source.loc[:127, ["Open", "High", "Low", "Close"]].copy()
low_min = market_data["Low"].min()
high_max = market_data["High"].max()
market_data = (market_data - low_min) / (high_max - low_min)

# initialize pip finder and find pip points
pip_finder = FastPip(market_data, dist_method="perpendicular", num_points=10)
market_data_with_pip = pip_finder.find_pips(dtype="df", time_it=True)

# print market data
print("market data with pip informations: ")
print(market_data_with_pip.head())
