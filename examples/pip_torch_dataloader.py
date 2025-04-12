from pipdet.dataset import PipDataset, CombinedDataset
from torch.utils.data import Dataset, DataLoader
from pathlib import Path


class CustomDataset(Dataset):
    def __init__(self, dataset):
        self.dataset = dataset  # store to use it as data source

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        pip_data = self.dataset[index]

        retrive_data = {
            "input": pip_data[["High", "Low", "X"]].to_numpy(),
            "target": pip_data[["dist", "hilo"]].to_numpy(),
        }

        return retrive_data


# Define the paths to the .pkl files containing PipDatasets
pkl_path1 = Path("./DATA/pip/EURUSD-1h.pkl")
pkl_path2 = Path("./DATA/pip/EURUSD-15m.pkl")

# Load the PipDatasets and Combine the PipDatasets into a single CombinedDataset
dataset1 = PipDataset(pkl_path1)
dataset2 = PipDataset(pkl_path2)
combined_dataset = CombinedDataset([dataset1, dataset2])

# Split the combined dataset into training (80%), validation (15%), and testing (5%)
train_ds, valid_ds, test_ds = combined_dataset.split(0.8, 0.15)

# Create a DataLoader for batching and shuffling
data_loader = DataLoader(CustomDataset(train_ds), batch_size=64, shuffle=True)

# Iterate through batches during model training
for batch in data_loader:
    ...
