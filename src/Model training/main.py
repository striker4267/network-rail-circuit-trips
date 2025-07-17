from data_setup import prepare
from tokeniser import tokenise
from train_model import train 

def main():

    

    combined_csv_file_path = "data/combined_data.csv"
    MODEL_NAME = "distilbert-base-uncased"

    [train_df, val_df, test_df, label2id, id2label, num_labels] = prepare(combined_csv_file_path)

    [ train_dataset, val_dataset, test_dataset] = tokenise(train_df, val_df, test_df, MODEL_NAME)

    train(train_dataset, val_dataset, test_dataset,MODEL_NAME, num_labels, label2id, id2label)

if __name__ == "__main__":
    main()



    
