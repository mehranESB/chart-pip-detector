from pipdet.dataset import PipDataset  # Import the PipDataset class
from pathlib import Path  # Import Path for handling file paths

# Define the path to the pre-saved .pkl file containing the dataset
pkl_path = Path("./DATA/pip/EURUSD-1h.pkl")

# Load the dataset from the .pkl file
dataset = PipDataset(pkl_path)

# Retrieve a single sample from the dataset (at index 10 for this example)
# Each sample contains normalized OHLC data and its associated PIP information
normalized_data = dataset[10]

# Print the normalized data in a readable format
print("Normalized OHLC Data:")
print(normalized_data)
