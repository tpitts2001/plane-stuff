from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

# URL of the website containing the desired table
url = "https://topforeignstocks.com/stock-lists/the-complete-list-of-airline-stocks-on-the-nyse/"

# Send a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table by partial match of its title
table_title = "The Complete List of European Airline Stocks trading on the US OTC Markets/Exchanges/Foreign Markets"
table = soup.find('strong', string=lambda text: text and table_title in text).find_next('table')

# Read the table with pandas
df = pd.read_html(str(table))[0]

# Output the DataFrame to a CSV file
csv_file_path = "C:/Users/fisht/Downloads/European_Airline_Stocks_OTC.csv"
df.to_csv(csv_file_path, index=False)

csv_file_path