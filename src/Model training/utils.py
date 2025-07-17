import torch 

class CircuitDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    
    def __getitem__(self, index):
        item = {key: torch.tensor(val[index]) for key, val in self.encodings.items() }
        item["labels"] = torch.tensor(self.labels[index])
        return item
    
    def __len__(self):
        return len(self.labels)