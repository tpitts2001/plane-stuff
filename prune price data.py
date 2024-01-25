import pandas as pd
import os

def filter_dates(csv_file, output_folder):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True)  # Added utc=True

    # Filter out rows with dates outside the desired range
    start_date = pd.to_datetime('2006-01-01', utc=True)  # Convert to datetime
    end_date = pd.to_datetime('2019-12-31', utc=True)    # Convert to datetime
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Save the filtered data to a new CSV file
    output_file = os.path.join(output_folder, os.path.basename(csv_file))
    filtered_df.to_csv(output_file, index=False)

def process_all_csv(input_folder, output_folder, keywords):
    # Iterate over all files in the input directory
    for file in os.listdir(input_folder):
        if file.endswith('.csv') and any(keyword in file for keyword in keywords):
            filter_dates(os.path.join(input_folder, file), output_folder)

# Usage
input_folder = 'price data'
output_folder = 'price data/filtered for model'
keywords = ["DAL", "CPA", "VLRS", "LTMAY", "JBLU", "HA", "ALGT", "ALK", "ULCC",
            "MESA", "AFLYY", "SNCY", "LUV", "AZUL", "GOL", "UAL", "SAVE", "SKYW", "AAL"]
process_all_csv(input_folder, output_folder, keywords)
