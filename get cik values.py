import pandas
import requests
import pandas as pd

headers = {'User-Agent': "sevenmilespersecond@yahoo.com"}

tickers_cik = requests.get("https://www.sec.gov/files/company_tickers.json", headers=headers)

tickers_cik = pd.json_normalize(pd.json_normalize(tickers_cik.json(), \
                                                  max_level=0).values[0])

tickers_cik["cik_str"] = tickers_cik["cik_str"].astype(str).str.zfill(10)
tickers_cik.set_index("ticker", inplace=True)

print(tickers_cik)

df = pd.DataFrame(tickers_cik)

# Exporting the DataFrame to a CSV file
df.to_csv('C:/Users/fisht/PycharmProjects/plane stuff/cik_values.csv')  # Set index=False if you don't want to include the index in your CSV file

#response = requests.get("https://data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/Assets.json", headers=headers)
