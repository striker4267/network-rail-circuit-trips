import torch
from transformers import pipeline
import pandas as pd
import math
import os

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

def translate(cause_csv, action_csv, cause_types_csv, combined_csv):

    if not os.path.exists("back_translation_has_run.flag"):
        # Do your one-time-only code here
        print("Running this block once...")

        # Create a temp flag file if it does not exist
        if not os.path.exists( "back_translation_temp.flag"):
            with open("back_translation_temp.flag", "w") as f:
                f.write("0")

    else:
        print("Already back translated before, skipping.")
        return
    
    df_c = pd.read_csv(cause_csv)
    df_a = pd.read_csv(action_csv)
    df_ct = pd.read_csv(cause_types_csv) #cause types csv will have the causes in column 1 and the count in column 2

    count = 1
    for cause, frequency in df_ct.itertuples(index=False ):

        with open("back_translation_temp.flag", 'r') as f:
            if int(f.read()) >= count:
                count +=1 
                continue

        if frequency < 400 and frequency>100:
            if frequency > 250:
                factor = math.ceil(1000/frequency)
            else:
                factor = math.ceil(800/ frequency)
            
            indexes = df_c.index[df_c['Cause'] == cause].tolist()
            sentences = df_a.loc[indexes, 'Action'].tolist()
            if len(sentences) == 0:
                continue

            mod_sentences = sentences.copy()

            for _ in range(factor -1):
                mod_sentences.extend(batch_translator(sentences))
            
            


        elif frequency < 100:
            if frequency > 80:
                factor = math.ceil( 600/ frequency)
                max = 2
            elif frequency > 50:
                factor = math.ceil( 500/ frequency)
                max = 2
            else:
                factor = math.ceil(300/frequency)
                max = 3

            indexes = df_c.index[df_c['Cause'] == cause].tolist()
            sentences = df_a.loc[indexes, 'Action'].tolist()
            if len(sentences) == 0:
                continue


            i = 0    
            augmented = sentences.copy()
            for _ in range(0, max):
                augmented.extend(batch_translator(augmented))
                i+=1

            mod_sentences = augmented.copy()
            for _ in range(i, factor -1):
                mod_sentences.extend(batch_translator(augmented))


        append_sentences_to_csv(mod_sentences, cause, combined_csv )

        
        with open("back_translation_temp.flag", "w") as f:
            f.write(str(count))
        count +=1
        
    os.rename("back_translation_temp.flag", "back_translation_has_run.flag")


def batch_translator(texts, batch_size = 16):
    
    results = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]

        fr_results = translator_en_fr(batch)
        fr_text = [res['translation_text'] for res in fr_results]

        en_results = translator_fr_en(fr_text)
        en_text = [res['translation_text'] for res in en_results]
        results.extend(en_text)
    return results


def append_sentences_to_csv(sentences, cause, combined_csv ):
    df_new = pd.DataFrame({
        'Cause': [cause] * len(sentences),
        'Action': sentences

    })
    df_new.to_csv(combined_csv, mode= 'a', header=False, index=False)