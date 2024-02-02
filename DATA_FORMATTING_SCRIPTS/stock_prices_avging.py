import pandas as pd
import os

def date_to_fiscal_quarter(date):
    """
    Convert a date to a fiscal quarter string.

    Parameters:
    - date: A pandas Timestamp object.

    Returns:
    - A string representing the fiscal quarter.
    """
    # Assuming fiscal quarters align with calendar quarters
    fiscal_quarters = {1: '1', 2: '1', 3: '1', 4: '2', 5: '2', 6: '2',
                       7: '3', 8: '3', 9: '3', 10: '4', 11: '4', 12: '4'}
    return fiscal_quarters[date.month]

def process_csv_file(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['quarter'] = df['Date'].apply(date_to_fiscal_quarter)
    df['Price'] = df[['Open', 'High', 'Low', 'Close']].mean(axis=1)
    df = df.drop(['Date', 'Dividends', 'Stock Splits', 'Repaired?', 'Open', 'High', 'Low', 'Close'], axis=1, errors='ignore')
    aggregated_df = df.groupby(['Year', 'quarter'])['Price'].mean().reset_index()
    aggregated_df.to_csv(output_csv, index=False)

def process_all_csvs(input_directory, output_directory):
    for filename in os.listdir(input_directory):
        if filename.endswith(".csv"):
            input_csv = os.path.join(input_directory, filename)
            output_csv = os.path.join(output_directory, filename.replace(".csv", "_processed.csv"))
            process_csv_file(input_csv, output_csv)
            print(f"Processed and saved: {output_csv}")

# Example usage
input_directory = '../data/price_data/filtered for model'
output_directory = '../data/price_data/rolled-into-quarter'
process_all_csvs(input_directory, output_directory)
