import yfinance as yf

aal = yf.Ticker("AAL")

print(aal.income_stmt)