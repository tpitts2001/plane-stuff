import pandas as pd

access_key = "4fe4500b6fd8b45c547faa198e9fdb45"

# File paths for the uploaded CSV files
nasdaq_file = 'tickers/Airline_Stocks_NASDAQ.csv'
nyse_file = 'tickers/Airline_Stocks_NYSE.csv'
otc_file = 'tickers/Airline_Stocks_OTC.csv'
euro_file = 'tickers/European_Airline_Stocks_OTC.csv'

# Reading the CSV files
nasdaq_stocks = pd.read_csv(nasdaq_file)
nyse_stocks = pd.read_csv(nyse_file)
otc_stocks = pd.read_csv(otc_file)
euro_stocks = pd.read_csv(euro_file)

# Extracting ticker symbols from each file
nasdaq_tickers = nasdaq_stocks['Ticker'].unique()
nyse_tickers = nyse_stocks['Ticker'].unique()
otc_tickers = otc_stocks['Ticker'].unique()
euro_tickers = euro_stocks['Ticker on US OTC Market/Exchanges'].unique()

# Combining all tickers into a single list
all_tickers = list(set(nasdaq_tickers) | set(nyse_tickers) | set(otc_tickers) | set(euro_tickers))

# Displaying the tickers
all_tickers