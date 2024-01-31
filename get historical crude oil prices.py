import yfinance as yf
import pandas as pd

# Fetch historical data
ticker_symbol = "CL=F"
ticker = yf.Ticker(ticker_symbol)
historical_data = ticker.history(start="2006-01-01", end="2019-12-31", interval="1d")

# Function to determine the quarter
def determine_quarter(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4

# Apply the function to each row to determine the quarter
historical_data['Quarter'] = historical_data.index.month.map(determine_quarter)

# Calculate the average of "Open" and "Close" and add it as a new column "Price"
historical_data['Price'] = (historical_data['Open'] + historical_data['Close']) / 2

# Remove unwanted columns
columns_to_remove = ["Dividends", "Stock Splits", "High", "Low", "Open", "Close", "Volume"]
historical_data.drop(columns=columns_to_remove, inplace=True)

# Define the file path for saving the CSV file
file_path = "crude_oil_data/crude_oil_prices_2006-2019.csv"  # Replace with your desired file path

# Save the DataFrame to a CSV file in the specified location
historical_data.to_csv(file_path)

print(f"Data saved to {file_path}")
