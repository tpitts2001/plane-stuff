import variables
import os
import re
from collections import defaultdict
import glob
from ACTUAL_PROGRAM.DATA_GATHERING import historical_flight_data as hfd
import pandas as pd

historical_flight_data_downloaded_file_path_os_path = os.path.realpath('../../'+variables.historical_flight_data_downloaded_file_path)

def convert_asc_to_csv(historical_flight_data_downloaded_file_path_os_path):
    # List all .asc files in the directory
    asc_files = [f for f in os.listdir(historical_flight_data_downloaded_file_path_os_path) if f.endswith('.asc')]

    for asc_file in asc_files:
        # Construct the full file path
        full_asc_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, asc_file)

        # Read the .asc file using pandas (assuming space-separated values)
        # Adjust the sep parameter as needed (e.g., sep='\t' for tab-separated values)
        df = pd.read_csv(full_asc_path, sep=' ', header=None)

        # Construct the CSV file name
        csv_file = asc_file.replace('.asc', '.csv')
        full_csv_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, csv_file)

        # Write the dataframe to a CSV file
        df.to_csv(full_csv_path, index=False)

        print(f"Converted {asc_file} to {csv_file}")

# Example usage:
convert_asc_to_csv(historical_flight_data_downloaded_file_path_os_path)