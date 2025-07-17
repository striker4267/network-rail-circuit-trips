from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from utils import CircuitDataset

def tokenise(train_df, val_df, test_df, MODEL_NAME):
    # load tokeniser
    tokeniser = AutoTokenizer.from_pretrained(MODEL_NAME)

    # Tokenis the text from each split

    train_encodings = tokeniser(train_df['Action'].tolist(), truncation = True, padding = True, max_length = 128)
    val_encodings = tokeniser(val_df['Action'].tolist(), truncation = True, padding = True, max_length = 128)
    test_encodings = tokeniser(test_df['Action'].tolist(), truncation = True, padding = True, max_length = 128)

    print("Tokenisation complete")

    train_dataset = CircuitDataset(train_encodings, train_df["Labels"].tolist())
    val_dataset = CircuitDataset(val_encodings, val_df["Labels"].tolist())
    test_dataset = CircuitDataset(test_encodings, test_df["Labels"].tolist())
    print("Datasets created")

    return [ train_dataset, val_dataset, test_dataset]