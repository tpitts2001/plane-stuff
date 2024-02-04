import time

import pandas as pd

#TODO: COLUMN REGRESS

# Define the path to the existing CSV file and the path for the new CSV file
input_csv_path = '../data/rev_data/ALK_income_data.csv'  # Update this with your input CSV file path
output_csv_path = '../data/FINAL/temp/path_to_your_output_csv'  # Update this with your desired output CSV file path
oil_price_csv_path = '../data/crude_oil_data/rolled_into_quarter_avg/quarterly_oil_prices.csv'  # The CSV with Price, Year, Quarter

# Load the CSV file into a DataFrame
df = pd.read_csv(input_csv_path)
# Load the oil price CSV file into another DataFrame \\\\\\\\\\\\\\
oil_df = pd.read_csv(oil_price_csv_path)


# Function to determine fiscal quarter from a date
def get_fiscal_quarter(date):
    month = pd.to_datetime(date).month
    if 1 <= month <= 3:
        return '1'
    elif 4 <= month <= 6:
        return '2'
    elif 7 <= month <= 9:
        return '3'
    elif 10 <= month <= 12:
        return '4'

def get_plane_type(plane_type):
    plane_type = pd.to_numeric(plane_type)
    return

# Apply the function to determine fiscal quarter and year
df['Quarter'] = df['fiscalDateEnding'].apply(get_fiscal_quarter)
df['Year'] = pd.to_datetime(df['fiscalDateEnding']).dt.year

# Rename the 'Price' column to 'oil_price' for clarity \\\\\\\\\\\\\\\\\\
oil_df.rename(columns={'Price': 'oil_price'}, inplace=True)

df['Quarter'] = df['Quarter'].astype(str)
oil_df['Quarter'] = oil_df['Quarter'].astype(str)

# Merge the original DataFrame with the oil price DataFrame on 'year' and 'quarter' \\\\\\\\\\\\\\\\\\\\\\
df = pd.merge(df, oil_df, on=['Year', 'Quarter'], how='left')

# Extract the desired columns
output_data = df[['Year', 'Quarter', 'operatingIncome', 'oil_price']]

# Write the data to a new CSV file
output_data.to_csv(output_csv_path, index=False)

print(f"Data with operating income, fiscal date ending, quarter, and year has been successfully written to {output_csv_path}")
