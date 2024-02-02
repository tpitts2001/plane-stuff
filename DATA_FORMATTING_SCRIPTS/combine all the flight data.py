import pandas as pd

# Replace these file paths with the actual paths of your CSV files
csv_file_path1 = 'data/flight_data/CSV/whole/filtered to traded companies/domestic.csv'
csv_file_path2 = 'data/flight_data/CSV/whole/filtered to traded companies/international-reformatted.csv'

# Read the CSV files
df1 = pd.read_csv(csv_file_path1)
df2 = pd.read_csv(csv_file_path2)

# Combine the DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Specify the location where you want to save the combined CSV file
output_file_path = 'data/flight_data/CSV/whole/filtered to traded companies/combined.csv'

# Save the combined DataFrame to a CSV file
combined_df.to_csv(output_file_path, index=False)

print(f'Combined CSV saved at {output_file_path}')