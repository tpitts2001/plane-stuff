import requests
from bs4 import BeautifulSoup
import os
import zipfile
import io

# URL of the SEC financial statement data sets page
url = "https://www.sec.gov/dera/data/financial-statement-data-sets.html"

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find and filter zip file links
zip_links = [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').endswith('.zip')]

# Your desired destination directory
destination_dir = 'SEC income data/RAW'

# Ensure the destination directory exists
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Download and extract each zip file
for zip_link in zip_links:
    # Complete the URL if it's relative
    if not zip_link.startswith('http'):
        zip_link = 'https://www.sec.gov' + zip_link

    # Download the zip file
    zip_response = requests.get(zip_link)
    zip_file = zipfile.ZipFile(io.BytesIO(zip_response.content))

    # Extract the zip file
    zip_file.extractall(destination_dir)