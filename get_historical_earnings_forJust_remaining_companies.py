import requests
import csv
import os
import time
from datetime import datetime, timedelta

def fetch_earnings(symbol, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "EARNINGS",
        "symbol": symbol,
        "apikey": api_key
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def write_to_csv(data, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    keys = data[0].keys() if data else []
    with open(file_path, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def wait_until(target_time):
    while datetime.now() < target_time:
        time.sleep(1)

# Replace with your actual API key.
api_key = 'AIEJB7CL4FJ3WZFY'

# Specify the directory and filename where you want to save the CSV file.
output_directory = 'earnings_data'  # Change this to your desired directory

# Set start time to 1:30 AM. Adjust the day if necessary.
start_time = datetime.now().replace(hour=1, minute=30, second=0, microsecond=0)
if datetime.now() > start_time:
    start_time += timedelta(days=1)

print(f"Script will start at {start_time}")
wait_until(start_time)

tickers = ["AAL", "SKYW", "AFLYY", "LTMAY"]

for symbol in tickers:
    print(f"Fetching earnings data for {symbol}...")

    earnings = fetch_earnings(symbol, api_key)
    if earnings and "quarterlyEarnings" in earnings:
        earnings_data = earnings["quarterlyEarnings"]
        if earnings_data:
            output_filename = f'{symbol}_earnings_data.csv'
            write_to_csv(earnings_data, output_directory, output_filename)
            print(f"Earnings data for {symbol} written to {output_filename}")
        else:
            print(f"No earnings data found for {symbol}")
    else:
        print(f"Error fetching Earnings for {symbol}")

    print("Waiting for 10 minutes before the next request...")
    time.sleep(600)  # Wait for 1 minute