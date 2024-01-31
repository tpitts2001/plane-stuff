import pandas as pd
import os

# Replace with the path to your CSV file
input_csv_path = 'flight_data/CSV/whole/filtered to traded companies/combined-reformatted.csv'

# Replace with the directory where you want to save the new CSV files
output_directory = 'flight_data/CSV/seperated by companies/'

# Read the CSV file
df = pd.read_csv(input_csv_path)

# Check and create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Group by 'Carrier: Alpha Code' and save each group as a CSV
for (carrier_code), group in df.groupby('Carrier: Alpha Code'):
    output_path = os.path.join(output_directory, f"{carrier_code}.csv")
    group.to_csv(output_path, index=False)

print("CSV files have been created in the specified directory.")
