import pandas as pd
import os

# List of file names
file_names = ["4M.csv", "JJ.csv", "UC.csv", "LA.csv", "4C.csv", "LU.csv", "PZ.csv", "LP.csv"]

# Folder containing the CSV files
folder_path = "historical-data/flight_data/CSV/seperated by companies"  # Update this to your folder path

# List to hold each DataFrame
data_frames = []

# Loop through the file names and read each file into a DataFrame
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        data_frames.append(data)
    else:
        print(f"File not found: {file_path}")

# Combine all DataFrames in the list
combined_data = pd.concat(data_frames, ignore_index=True)

# Specify the location to save the new combined CSV file
output_path = "historical-data/flight_data/CSV/seperated by companies/LTMAY.csv"  # Update this to your desired path

# Save the combined historical-data to a new CSV file
combined_data.to_csv(output_path, index=False)

print(f"Combined CSV saved to {output_path}")