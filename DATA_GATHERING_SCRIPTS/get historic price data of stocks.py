import yfinance as yf
import pandas as pd
import varibles


# Function to fetch entire price history for a list of tickers
def get_price_history(tickers):
    price_histories = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        history = stock.history(repair=True, period="max")
        price_histories[ticker] = history
    return price_histories

output_directory = 'price_data'

tickers = varibles.all_tickers

price_histories = get_price_history(tickers)

# Example: Save the data to CSV files
for ticker, history in price_histories.items():
    history.to_csv(f"{output_directory}/{ticker}_price_history.csv")