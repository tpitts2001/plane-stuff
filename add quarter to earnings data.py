import os
import pandas as pd
from datetime import datetime


def determine_quarter(date_str):
    """
    Determine the fiscal quarter for a given date.

    Parameters:
    - date_str (str): Date string in the format "YYYY-MM-DD".

    Returns:
    - str: The fiscal quarter ("Q1", "Q2", "Q3", "Q4").
    """
    date = datetime.strptime(date_str, "%Y-%m-%d")
    month = date.month
    if 1 <= month <= 3:
        return "1"
    elif 4 <= month <= 6:
        return "2"
    elif 7 <= month <= 9:
        return "3"
    elif 10 <= month <= 12:
        return "4"


def process_csv_files(input_dir, output_dir):
    """
    Process all CSV files in the input directory, add "Quarter" based on "fiscalDateEnding",
    and save them to the output directory.

    Parameters:
    - input_dir (str): The directory containing the input CSV files.
    - output_dir (str): The directory where the modified CSV files will be saved.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(input_dir, file)
            df = pd.read_csv(file_path)

            # Check if "fiscalDateEnding" column exists
            if "fiscalDateEnding" in df.columns:
                df['Quarter'] = df['fiscalDateEnding'].apply(determine_quarter)

                # Save the modified dataframe to a new CSV file
                output_file_path = os.path.join(output_dir, file)
                df.to_csv(output_file_path, index=False)
                print(f"Processed and saved: {output_file_path}")
            else:
                print(f"No 'fiscalDateEnding' column found in {file_path}")


# Example usage
input_directory = 'earnings_data/unformatted'  # Replace 'path/to/input' with the path to your input files
output_directory = 'earnings_data/formatted-quarter'  # Replace 'path/to/output' with the path to your output files
process_csv_files(input_directory, output_directory)
