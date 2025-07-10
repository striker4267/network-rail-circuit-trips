import pandas as pd
import os
import glob 

subfolder_name = "data"
def extract_column_to_csv(excel_file, sheet_name, column_name, output_csv_file):

    if not os.path.exists(subfolder_name):
        os.makedirs(subfolder_name)

    output_csv_file_path = os.path.join(subfolder_name,output_csv_file)
    
    try:
        with pd.read_excel(excel_file, sheet_name = sheet_name) as df:
            #Check if the column exists
            if column_name not in df.columns:
                print(f"Error: Column {column_name} not found in {excel_file}")
                print(f" Available columns are { df.columns.tolist()}")
                return

            selected_column = df[column_name]  

            selected_column.to_csv(output_csv_file_path, index = False, header=True)

            print(f" Successfully extraced column '{column_name}' from '{excel_file}' \n and saved it to '{output_csv_file}.csv'") 

    except FileNotFoundError:
        print( f"Error Excel file not found at '{excel_file}")
    except Exception as e:
        print( f"An error occurred: {e}")