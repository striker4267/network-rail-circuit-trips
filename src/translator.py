import torch
from transformers import pipeline

if torch.cuda.is_available():
    print(f"CUDA is available. Using GPU: {torch.cuda.get_device_name(0)}")
    device_id = 0
else:
    print ("CUDA is not available. Using CPU")
    device_id = -1

translator_en_fr = pipeline(
    "translation",
    model = "Helsinki-NLP/opus-mt-en-fr",
    device= device_id
)

translator_fr_en = pipeline(
    "translation", 
    model= "Helsinki-NLP/opus-mt-fr-en",
    device = device_id
)