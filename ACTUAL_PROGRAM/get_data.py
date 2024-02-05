import re
import variables
import os
import requests

##############################################################
#correlating stuff to variables file

historical_flight_data_html_file_path = variables.historical_flight_data_html_file_path
historical_flight_data_downloaded_file_path = variables.historical_flight_data_downloaded_file_path
historical_flight_data_base_domain = variables.historical_flight_data_base_domain

##############################################################
#methods

def download_historical_flight_data(historical_flight_data_html_file_path, historical_flight_data_downloaded_file_path, historical_flight_data_base_domain):
    # Open the file and read its contents
    with open(historical_flight_data_html_file_path, 'r', encoding='utf-8') as file:
        html_text = file.read()

    # Define the regex pattern to match URLs that start with '/sites' and end with '.zip'
    pattern = r'"/sites[^"]+\.zip"'

    # Use re.findall to find all occurrences that match the pattern
    urls = re.findall(pattern, html_text)

    # The pattern includes quotes around the URLs, so remove them
    urls = [url.strip('"') for url in urls]

    print('Found' + str(urls) + '. Downloading...')

    """
        Download ZIP files from a list of URLs.

        Args:
        - urls (list): A list of relative URLs to ZIP files.
        - base_domain (str): The base domain to prepend to each URL to form a complete URL.
        - destination_folder (str): The destination folder where the ZIP files should be saved.
        """
    if not os.path.exists(historical_flight_data_downloaded_file_path):
        os.makedirs(historical_flight_data_downloaded_file_path)

    for url in urls:
        # Form the complete URL
        full_url = historical_flight_data_base_domain + url
        try:
            # Send a GET request to the URL
            response = requests.get(full_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Extract the file name from the URL
            file_name = url.split('/')[-1]
            destination_path = os.path.join(historical_flight_data_downloaded_file_path, file_name)

            # Write the content to a file in the destination folder
            with open(destination_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {file_name} to {historical_flight_data_downloaded_file_path}")
        except requests.HTTPError as e:
            print(f"Failed to download {url}: HTTP Error {e.response.status_code}")
        except requests.RequestException as e:
            print(f"Failed to download {url}: {e}")

    return
