import pandas as pd 
import csv

def clean_csv(csv_file ):
    try:
        df = pd.read_csv( csv_file)
        column_name = df.columns[0]

        df[column_name] = df[column_name].astype(str).str.strip()
        df[column_name] = df[column_name].astype(str).str.capitalize()

        output_file = "data/Trip_Causes_Cleaned.csv"
        df.to_csv(output_file, index = False)

        print(f"The cleaned data has been saved to {output_file} ")
        return output_file


    except FileNotFoundError:
        print( f"Error: the file {csv_file} has not been found")

if __name__ == "__main__":
    clean_csv("data/Trip_Causes_Uncleaned.csv")