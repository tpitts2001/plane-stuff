import os
import pandas as pd

def process_csv_files(source_folder, destination_folder):
    # List of columns to be deleted
    columns_to_delete = [
        "Origin Airport: World Area Code",
        "Origin Airport: City Name",
        "Destination Airport: World Area Code",
        "Destination Airport: City Name",
        "Carrier: Entity Code",
        "Official OAI Group Code",
        "Service Class",
        "Aircraft Type: Group",
        "Aircraft Type: Configuration"
    ]

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Process each CSV file in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(source_folder, filename)
            df = pd.read_csv(file_path)

            # Drop the specified columns if they exist in the DataFrame
            df = df.drop(columns=[col for col in columns_to_delete if col in df.columns])

            # Save the modified DataFrame to a new CSV file
            df.to_csv(os.path.join(destination_folder, filename), index=False)

# Example usage
source_folder = 'flight_data/CSV/seperated by companies'  # Replace with your source folder path
destination_folder = 'flight_data/filtered for model/without'  # Replace with your destination folder path
process_csv_files(source_folder, destination_folder)