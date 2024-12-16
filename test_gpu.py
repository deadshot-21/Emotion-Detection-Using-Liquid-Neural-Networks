import torch

# Check if GPU is available
if torch.cuda.is_available():
    print("GPU is available and will be used for training.")
else:
    print("No GPU available. Training will be done on CPU.")