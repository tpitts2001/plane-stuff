import os
import pandas as pd

def convert_asc_to_csv(historical_flight_data_downloaded_file_path_os_path, headers_csv_file_path):
    # Read headers from the specified CSV file
    headers_df = pd.read_csv(headers_csv_file_path)
    # Assuming the headers are in the first row
    headers = headers_df.columns.tolist()

    # List all .asc files in the directory
    asc_files = [f for f in os.listdir(historical_flight_data_downloaded_file_path_os_path) if f.endswith('.asc')]

    for asc_file in asc_files:
        # Construct the full file path
        full_asc_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, asc_file)

        # Read the .asc file using pandas with the specified separator and apply headers
        df = pd.read_csv(full_asc_path, sep='|', header=None, names=headers, low_memory=False)

        # Construct the CSV file name
        csv_file = asc_file.replace('.asc', '.csv')
        full_csv_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, csv_file)

        # Write the dataframe to a CSV file
        df.to_csv(full_csv_path, index=False)

        print(f"Converted {asc_file} to {csv_file} with headers")
