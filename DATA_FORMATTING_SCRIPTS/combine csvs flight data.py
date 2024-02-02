import os
import pandas as pd

def combine_csv_in_folder(folder_path, output_file):
    # List to hold data from each CSV file
    all_data = []

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            # Read the CSV file and append to list
            df = pd.read_csv(file_path)
            all_data.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(all_data, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(output_file, index=False)

    print(f"Combined CSV saved as {output_file}")

# Usage
folder_path = 'data/flight_data/CSV/domestic'  # replace with your folder path
output_file = 'data/flight_data/CSV/whole/domestic.csv'  # replace with your desired output file name
combine_csv_in_folder(folder_path, output_file)
