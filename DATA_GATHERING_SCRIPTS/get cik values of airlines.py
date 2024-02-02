import csv
import varibles

# Define the path to your CSV file
file_path = r"C:\Users\fisht\PycharmProjects\plane stuff\cik_values.csv"

# Define your list of tickers
all_tickers = varibles.all_tickers

# Function to find cik_str by ticker
def find_cik_str(file_path, ticker):
    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            if row['ticker'] == ticker:
                return row['cik_str']
    return None

# List to store tickers and their cik_str
ticker_cik_pairs = []

# Iterate through all tickers and find their cik_str
for ticker in all_tickers:
    cik_str = find_cik_str(file_path, ticker)
    if cik_str:
        ticker_cik_pairs.append([ticker, cik_str])

# Save the results to a new CSV file
output_file_path = r"C:\Users\fisht\PycharmProjects\plane stuff\tickers_cik.csv"
with open(output_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticker", "CIK_Str"])  # Writing header
    writer.writerows(ticker_cik_pairs)

print("File saved:", output_file_path)