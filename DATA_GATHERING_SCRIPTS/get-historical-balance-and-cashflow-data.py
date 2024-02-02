import requests
import pandas as pd
import json
import os
import datetime
import time


def fetch_financial_data(symbol, api_key, data_type):
    url = "https://www.alphavantage.co/query"
    function_type = "BALANCE_SHEET" if data_type == 'balance_sheet' else "CASH_FLOW"
    params = {
        "function": function_type,
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
        print(f"Error reading tickers from CSV: {e}")
        return []


def save_data_to_file(data, symbol, data_type, output_directory_base):
    output_directory = os.path.join(output_directory_base, data_type)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    filename = f"{symbol}_{data_type}.json"
    filepath = os.path.join(output_directory, filename)
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Saved {data_type} data for {symbol} to {filepath}")


def check_if_ticker_processed(symbol, output_directory_base):
    balance_sheet_path = os.path.join(output_directory_base, 'balance_sheet', f"{symbol}_balance_sheet.json")
    cash_flow_path = os.path.join(output_directory_base, 'cash_flow', f"{symbol}_cash_flow.json")
    return os.path.exists(balance_sheet_path) and os.path.exists(cash_flow_path)


def gather_and_save_financial_data(api_key, file_path, output_directory_base):
    tickers = read_tickers_from_csv(file_path)
    for ticker in tickers:
        if check_if_ticker_processed(ticker, output_directory_base):
            print(f"Data for {ticker} already exists. Skipping.")
            continue

        for data_type in ['balance_sheet', 'cash_flow']:
            financial_data = fetch_financial_data(ticker, api_key, data_type)
            if "quarterlyReports" not in financial_data:
                print(f"No 'quarterlyReports' found in {data_type} data for {ticker}. Skipping.")
                continue  # Skip saving this data type for the current ticker

            save_data_to_file(financial_data, ticker, data_type, output_directory_base)

def run_at_specific_time(hour=15, minute=59):
    while True:
        now = datetime.datetime.now()
        next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if next_run < now:
            next_run += datetime.timedelta(days=1)

        wait_seconds = (next_run - now).total_seconds()
        print(f"Waiting {wait_seconds} seconds until the next run.")

        time.sleep(wait_seconds)

        api_key = "AIEJB7CL4FJ3WZFY"
        file_path = "../data/airline_identifiers/tickers_cik.csv"
        output_directory_base = "../data/temp"
        gather_and_save_financial_data(api_key, file_path, output_directory_base)

        time.sleep(60)  # Wait a bit before calculating the next run


if __name__ == "__main__":
    run_at_specific_time()
