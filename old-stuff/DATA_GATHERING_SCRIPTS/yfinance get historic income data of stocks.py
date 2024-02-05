import yfinance as yf
import varibles

# Function to fetch quarterly income statements for a given list of tickers
def get_quarterly_income_statements(tickers):
    income_statements = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            income_statement = stock.quarterly_income_stmt
            income_statements[ticker] = income_statement
        except Exception as e:
            income_statements[ticker] = f"Error: {e}"
    return income_statements

output_directory = 'yfinance income historical-data'

# Fetching for a subset of tickers due to time constraints
tickers = varibles.all_tickers
income_statements_subset = get_quarterly_income_statements(tickers)

# Displaying the results for the subset
print(income_statements_subset)
for ticker, history in income_statements_subset.items():
    history.to_csv(f"{output_directory}/{ticker}_income_history.csv")