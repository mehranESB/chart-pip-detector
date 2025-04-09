from pipdet.dataset import PipDataset, CombinedDataset
from pathlib import Path

# Define the paths to the .pkl files containing PipDatasets
pkl_path1 = Path("./DATA/pip/EURUSD-1h.pkl")
pkl_path2 = Path("./DATA/pip/EURUSD-15m.pkl")

# Load the PipDatasets
dataset1 = PipDataset(pkl_path1)  # Load the first PipDataset
dataset2 = PipDataset(pkl_path2)  # Load the second PipDataset

# Combine the PipDatasets into a single CombinedDataset
# Merge datasets for unified management
combined_dataset = CombinedDataset([dataset1, dataset2])

# Split the combined dataset into training (80%), validation (15%), and testing (5%)
# Assumes the `split` method of CombinedDataset is implemented
train_ds, valid_ds, test_ds = combined_dataset.split(0.8, 0.15)

# Example output to verify splits
print(f"Total samples in combined dataset: {len(combined_dataset)}")
print(f"Training dataset size: {len(train_ds)}")
print(f"Validation dataset size: {len(valid_ds)}")
print(f"Testing dataset size: {len(test_ds)}")

# Optionally, print a sample from the training dataset
print("\nFirst training sample (normalized data and score):")
print("Normalized Data (Training):")
# Assuming normalized data can be converted to a DataFrame
print(train_ds[8000])
