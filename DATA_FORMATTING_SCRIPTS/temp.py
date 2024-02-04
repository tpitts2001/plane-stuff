import pandas as pd

# Define the path to the existing CSV file and the path for the new CSV file
input_csv_path = 'path_to_your_input_csv.csv'  # Update this with your input CSV file path
output_csv_path = 'path_to_your_output_csv.csv'  # Update this with your desired output CSV file path

# Load the CSV file into a DataFrame
df = pd.read_csv(input_csv_path)

# Function to determine fiscal quarter from a date
def get_fiscal_quarter(date):
    month = pd.to_datetime(date).month
    if 1 <= month <= 3:
        return 'Q1'
    elif 4 <= month <= 6:
        return 'Q2'
    elif 7 <= month <= 9:
        return 'Q3'
    elif 10 <= month <= 12:
        return 'Q4'

# Apply the function to determine fiscal quarter and year
df['quarter'] = df['fiscalDateEnding'].apply(get_fiscal_quarter)
df['year'] = pd.to_datetime(df['fiscalDateEnding']).dt.year

# Extract the desired columns
output_data = df[['operatingIncome', 'fiscalDateEnding', 'quarter', 'year']]

# Write the data to a new CSV file
output_data.to_csv(output_csv_path, index=False)

print(f"Data with operating income, fiscal date ending, quarter, and year has been successfully written to {output_csv_path}")
