import requests
import pandas as pd
import csv
import os
import time

def fetch_earnings(symbol, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "CASH_FLOW",
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def read_tickers_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df['Ticker'].tolist()
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return []

def write_to_csv(data, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    keys = data[0].keys() if data else []
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Replace with your actual API key and the path to your CSV file.
api_key = 'AIEJB7CL4FJ3WZFY'
csv_file_path = '../../historical-data/airline_identifiers/tickers_cik.csv'

# Specify the directory and filename where you want to save the CSV file.
output_directory = 'historical-data/balance_sheet_data'  # Change this to your desired directory

tickers = read_tickers_from_csv(csv_file_path)
all_data = []

for symbol in tickers:
    print(f"Fetching CASH_FLOW for {symbol}...")

    earnings = fetch_earnings(symbol, api_key)
    if earnings and "quarterlyReports" in earnings:
        earnings_data = earnings["quarterlyReports"]
        if earnings_data:
            output_filename = f'{symbol}_balance_data.csv'
            write_to_csv(earnings_data, output_directory, output_filename)
            print(f"Cashflow historical-data for {symbol} written to {output_filename}")
        else:
            print(f"No CASH_FLOW found for {symbol}")
    else:
        print(f"Error fetching Cashflow for {symbol}")

    print("Waiting for 10 minutes before the next request...")
    time.sleep(600)  # Wait for 1 minute
