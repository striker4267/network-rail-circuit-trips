import pandas as pd
from extract import extract_column_to_csv


excel_file = "data/Trip Data for Matthew.xlsx"
sheet_name = "Sheet1"
column_name = "Causes"
output_csv_file = "Trip_Causes_Cleaned.csv"

def main (excel_file, sheet_name, column_name, output_csv_file):
    """Cleans the data of the excel file """

    #TODO: Load the column into a CSV File
    # 
    extract_column_to_csv(excel_file, sheet_name, column_name, output_csv_file)
    
    #TODO: Get rid of the whitespace and make the first letter of each word capital 

if __name__ == "__main__":
    main (excel_file, sheet_name, column_name, output_csv_file)