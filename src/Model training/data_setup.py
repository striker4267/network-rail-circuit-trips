import pandas as pd
import torch 
from sklearn.model_selection import train_test_split

def prepare(csv_file_path):
    column_names = ["Cause", "Action"]
    df = pd.read_csv(csv_file_path, header = None, names= column_names)
    print(f"loaded {len(df)} records")

    df['Action'] = df['Action'].fillna('')

    [df , label2id, id2label, num_labels] = label(df)
    [train_df, val_df, test_df] = split(df)
    return [train_df, val_df, test_df, label2id, id2label, num_labels ]

def label(df):
    unique_cases = df["Cause"].unique().tolist()

    label2id = {label: i for i, label in enumerate(unique_cases)}
    id2label = {i: label for i, label in enumerate(unique_cases)}

    df["Labels"] = df["Cause"].map(label2id)

    print("labels encoded")
    print(f"Mapping: {label2id}")
    return df, label2id, id2label, len(unique_cases)

def split (df):
    train_df, temp_df = train_test_split(
    df,
    test_size = 0.2,
    random_state= 42,
    stratify= df["Labels"]
    )

    val_df, test_df = train_test_split(
        temp_df,
        test_size= 0.5,
        random_state= 42,
        stratify= temp_df["Labels"]
    )
    print( f"training set size: {len(train_df)}")
    print(f"Validation set size: {len(val_df)}")
    print(f"Test set size: {len(test_df)}")
    return [train_df, val_df, test_df]