import pandas as pd
import os

# Define the path to the original CSV file and the folder for the new file
input_csv_path = 'historical-data/flight_data/CSV/whole/domestic.csv'  # Update this with the actual path
output_folder_path = 'historical-data/flight_data/CSV/whole/filtered to traded companies'  # Update this with the desired output folder path
output_csv_path = os.path.join(output_folder_path, 'domestic.csv')

# Check if the output folder exists, if not, create it
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# List of designated alpha codes
designated_alpha_codes = [
    "DL", "CM", "Y4", "4M", "JJ", "UC", "LA", "4C", "LU", "PZ", "LP", "B6", "HA",
    "G4", "AS", "F9", "YV", "AF", "SY", "WN", "AD", "G3", "FR", "RK", "UA", "NK",
    "OO", "AA"
]

# Read the CSV file
df = pd.read_csv(input_csv_path)

# Filter the DataFrame
filtered_df = df[df["Carrier: Alpha Code"].isin(designated_alpha_codes)]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_csv_path, index=False)

print("Filtered CSV file saved to", output_csv_path)