import re
import variables
import os
import requests
import zipfile

##############################################################
#correlating stuff to variables file

historical_flight_data_downloaded_file_path_os_path = os.path.realpath('../../'+variables.historical_flight_data_downloaded_file_path)
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

def extract_date_range(filename):
    parts = filename.split('.')
    start_date = ''
    end_date = ''
    for i, part in enumerate(parts):
        if part == 'dm':
            if i + 1 < len(parts):
                start_date = parts[i + 1]
            if i + 2 < len(parts):
                end_date = parts[i + 2]
            break
    return start_date, end_date


def process_files_in_folder(historical_flight_data_downloaded_file_path_os_path):
    files = os.listdir(historical_flight_data_downloaded_file_path_os_path)

    for filename in files:
        start_date, end_date = extract_date_range(filename)
        if start_date and end_date:  # Ensure both dates are extracted
            # Generate new filename
            new_filename = f"{start_date}-{end_date}_{filename}"
            # Construct full old and new file paths
            old_file_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, filename)
            new_file_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")

def extract_and_delete_zip_folders(historical_flight_data_downloaded_file_path):
    # Ensure the extraction directory exists
    if not os.path.exists(historical_flight_data_downloaded_file_path):
        os.makedirs(historical_flight_data_downloaded_file_path)

    # Iterate through all files in the zip directory
    for filename in os.listdir(historical_flight_data_downloaded_file_path):
        if filename.endswith('.zip'):
            # Construct the full path to the file
            file_path = os.path.join(historical_flight_data_downloaded_file_path, filename)
            # Open the zip file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                # Extract all the contents into the specified directory
                zip_ref.extractall(historical_flight_data_downloaded_file_path)
            # After extraction, delete the zip file
            os.remove(file_path)
            print(f"Extracted and deleted '{filename}'")