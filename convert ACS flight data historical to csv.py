import os
import pandas as pd

def convert_asc_to_csv_with_labels(source_directory, target_directory, column_labels):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Iterate over all files in the source directory
    for file in os.listdir(source_directory):
        if file.endswith(".asc"):
            file_path = os.path.join(source_directory, file)
            # Read the .asc file
            data = pd.read_csv(file_path, sep="|", header=None)  # Modify separator if needed

            # Check if the number of columns matches the number of provided labels
            if len(data.columns) != len(column_labels):
                print(f"Column count mismatch in file {file}. Expected {len(column_labels)} columns, found {len(data.columns)}.")
                continue

            # Assign new column labels
            data.columns = column_labels

            # Create a CSV file path
            csv_file = os.path.splitext(file)[0] + '.csv'
            csv_file_path = os.path.join(target_directory, csv_file)

            # Save as CSV
            data.to_csv(csv_file_path, index=False)

# Column labels
column_labels = [
    "Date of Data: Year", "Date of Data: Month", "Origin Airport: Alpha Code",
    "Origin Airport: Unique Numeric Code", "Origin Airport: World Area Code",
    "Origin Airport: City Name", "Destination Airport: Alpha Code",
    "Destination Airport: Numeric Code", "Destination Airport: World Area Code",
    "Destination Airport: City Name", "Carrier: Alpha Code",
    "Carrier: Entity Code", "Official OAI Group Code", "Distance",
    "Service Class", "Aircraft Type: Group", "Aircraft Type: Type",
    "Aircraft Type: Configuration", "Departures Performed",
    "Departures Scheduled", "Available Capacity: Payload Pounds",
    "Available Seats", "Coach Cabin (No Longer Reported)", "Middle Cabin (No Longer Reported)",
    "Passengers Transported",  "Carrier's World Area Code",
    "null", "Freight Transported", "Mail Transported",
    "Ramp in minutes", "Airborne in minutes"
]

# Usage
source_dir = 'flight_data/RAW ASC/international'  # Replace with the path to your .asc files
target_dir = 'flight_data/CSV/international'  # Replace with the path where you want to save .csv files
convert_asc_to_csv_with_labels(source_dir, target_dir, column_labels)
