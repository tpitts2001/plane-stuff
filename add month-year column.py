import pandas as pd

# Specify the file paths
input_file_path = 'flight data/CSV/whole/filtered to traded companies/combined.csv'  # Replace with the path to your input CSV file
output_file_path = 'flight data/CSV/whole/filtered to traded companies/combined-reformatted.csv'  # Replace with the path where you want to save the new CSV file

# Read the CSV file
df = pd.read_csv(input_file_path)

# Combine the two columns into a new column
df['month-year'] = df['Date of Data: Month'].astype(str) + '-' + df['Date of Data: Year'].astype(str)

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file_path, index=False)

print("CSV file has been updated and saved at:", output_file_path)