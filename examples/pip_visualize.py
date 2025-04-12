from chartDL.utils import csv as csv_utils
from chartDL.dataset import SingleDataset
from pipdet.pip import FastPip
from pipdet.utils import tight_box_normalize_df
from pipdet.utils import plot_pip_on_chart, plot_pip_score
from pathlib import Path
import matplotlib.pyplot as plt

# Import source DataFrame
csv_source_path = Path("./DATA/csv/EURUSD-1h.csv")
if not csv_source_path.exists():
    raise FileNotFoundError(f"File not found: {csv_source_path}")

df_source = csv_utils.import_ohlcv_from_csv(
    csv_source_path, header=True, datetime_format="%Y-%m-%d %H:%M:%S"
)

# Create dataset with 128-length chunks and fetch a sample
dataset = SingleDataset(df_source, 128)
sample_data = dataset[500]

# Normalize the sample data
normalized_data = tight_box_normalize_df(sample_data)

# Initialize FastPip for finding perceptually important points just for 10 pip points
fast_pip = FastPip(normalized_data, dist_method="perpendicular", num_points=10)
pip_data = fast_pip.find_pips(time_it=True, dtype="df")

# Plot PIP data on the chart
fig, ax = plt.subplots()
ax = plot_pip_on_chart(
    pip_data, ax=ax, title="pip point segment line"
)  # Plot the PIP points on a candlestick chart

# Initialize FastPip for finding perceptually important points just for all chandles
fast_pip = FastPip(normalized_data, dist_method="perpendicular", num_points=None)
pip_data = fast_pip.find_pips(time_it=True, dtype="df")

# plot distnace from segment of pip point as score of point
fig2, ax2 = plt.subplots()
ax2 = plot_pip_score(
    pip_data, ax=ax2, max_markersize=50, title="distance score of pip points"
)

# show all plots
plt.show()
