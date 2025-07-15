import torch
from transformers import pipeline
import pandas as pd

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

def translate(cause_csv, action_csv):
    
    df_c = pd.read_csv(cause_csv)
    df_a = pd.read_csv(action_csv)

    




def back_translator(text):
    
    if not isinstance(text, list):
        text = [text] 
    
    # Translate English to French
    # The pipeline returns a list of dictionaries, so access the translation_text
    fr_results = translator_en_fr(text)
    fr_text = fr_results[0]['translaton_text']

    en_results = translator_fr_en(fr_text)
    en_text = en_results[0]['translation_text']

    return en_text