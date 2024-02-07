import re
import time

import variables
import os
import requests
import zipfile
from collections import defaultdict
import glob
import pandas as pd

##############################################################
#correlating stuff to variables file

files_group = defaultdict(list)
historical_flight_data_downloaded_file_path_os_path = os.path.realpath(variables.historical_flight_data_downloaded_file_path)
historical_flight_data_html_file_path = variables.historical_flight_data_html_file_path
historical_flight_data_html_file_path_int = variables.historical_flight_data_html_file_path_int
historical_flight_data_downloaded_file_path = variables.historical_flight_data_downloaded_file_path
historical_flight_data_base_domain = variables.historical_flight_data_base_domain
labels_file_path = variables.historical_flight_data_label_file_path
glob_pattern = os.path.join(historical_flight_data_downloaded_file_path_os_path, '*.asc')
asc_files = glob.glob(glob_pattern)

##############################################################
# domestic data methods

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

def move_first_10_chars_to_back(historical_flight_data_downloaded_file_path_os_path):

# Use glob to find all text files if you're only interested in .txt files, for example
    for filename in os.listdir(historical_flight_data_downloaded_file_path_os_path):
        # Check if the filename is long enough to be modified
        if len(filename) > 10:
            # Split the filename into name and extension
            name, extension = os.path.splitext(filename)
            # Move the first 10 characters to the end of the name
            new_name = name[10:] + name[:10] + extension
            # Construct the full old and new file paths
            old_file = os.path.join(historical_flight_data_downloaded_file_path_os_path, filename)
            new_file = os.path.join(historical_flight_data_downloaded_file_path_os_path, new_name)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")

def combine_flight_data_files(historical_flight_data_downloaded_file_path_os_path):
    """
    Group and combine .asc files in the given directory.

    Args:
    directory_path (str): The path to the directory containing the files.
    """
    # Initialize a defaultdict to group files
    files_grouped = defaultdict(list)

    # List and group all .asc files by the first 13 characters of their filename
    for filename in os.listdir(historical_flight_data_downloaded_file_path_os_path):
        if filename.endswith(".asc"):
            # Use the first 13 characters as the key
            group_key = filename[:13]
            print(f'Grouped {filename}.')
            files_grouped[group_key].append(filename)

    # Combine the files in each group
    for group_key, filenames in files_grouped.items():
        combined_file_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, f"{group_key}.asc")
        with open(combined_file_path, 'w') as combined_file:
            for filename in filenames:
                file_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, filename)
                with open(file_path, 'r') as file:
                    combined_file.write(file.read() + "\n")  # Add a newline between files' content if needed
                    print(f'Combined {file_path}.')

def delete_files_with_db(historical_flight_data_downloaded_file_path_os_path):
    """
    Deletes all files in the specified directory that contain 'db' in their title.

    Args:
    directory_path (str): The path to the directory where files will be checked and deleted.
    """
    # Ensure the directory exists before proceeding
    if not os.path.isdir(historical_flight_data_downloaded_file_path_os_path):
        print("Directory does not exist.")
        return

    # Counter for deleted files
    deleted_files_count = 0

    # Loop through each file in the directory
    for filename in os.listdir(historical_flight_data_downloaded_file_path_os_path):
        # Check if "db" is in the file title
        if "db" in filename:
            # Construct the full file path
            file_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, filename)
            # Delete the file
            os.remove(file_path)
            deleted_files_count += 1
            print(f"Deleted {file_path}")

    # Print a summary of the operation
    if deleted_files_count == 0:
        print("No files containing 'db' found to delete.")
    else:
        print(f"Total deleted files containing 'db': {deleted_files_count}")

def convert_asc_to_csv(historical_flight_data_downloaded_file_path_os_path, labels_file_path):
    # Read headers from the specified CSV file
    headers_df = pd.read_csv(labels_file_path)
    # Assuming the headers are in the first row
    headers = headers_df.columns.tolist()

    # List all .asc files in the directory
    asc_files = [f for f in os.listdir(historical_flight_data_downloaded_file_path_os_path) if f.endswith('.asc')]

    for asc_file in asc_files:
        # Construct the full file path
        full_asc_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, asc_file)

        # Read the .asc file using pandas with the specified separator and apply headers
        df = pd.read_csv(full_asc_path, sep='|', header=None, names=headers, low_memory=False)

        # Construct the CSV file name
        csv_file = asc_file.replace('.asc', '.csv')
        full_csv_path = os.path.join(historical_flight_data_downloaded_file_path_os_path, csv_file)

        # Write the dataframe to a CSV file
        df.to_csv(full_csv_path, index=False)

        print(f"Converted {asc_file} to {csv_file} with headers")


def delete_all_ascs_in_dir(historical_flight_data_downloaded_file_path_os_path):
    for historical_flight_data_downloaded_file_path_os_path in asc_files:
        try:
            os.remove(historical_flight_data_downloaded_file_path_os_path)
            print(f"Deleted {historical_flight_data_downloaded_file_path_os_path}")
        except Exception as e:
            print(f"Error deleting {historical_flight_data_downloaded_file_path_os_path}: {e}")


##############################################################################################
# international data methods
#todo this lol

##############################################################################################
#main methods
def download_and_format_historical_flight_data():
    download_historical_flight_data(variables.historical_flight_data_html_file_path, variables.historical_flight_data_downloaded_file_path, variables.historical_flight_data_base_domain)
    extract_and_delete_zip_folders(variables.historical_flight_data_downloaded_file_path)
    move_first_10_chars_to_back(historical_flight_data_downloaded_file_path_os_path)
    combine_flight_data_files(historical_flight_data_downloaded_file_path_os_path)
    delete_files_with_db(historical_flight_data_downloaded_file_path_os_path)
    convert_asc_to_csv(historical_flight_data_downloaded_file_path_os_path, labels_file_path)
    time.sleep(20)
    delete_all_ascs_in_dir(historical_flight_data_downloaded_file_path_os_path)
    print(f"Finished downloading historical flight data.")

def download_and_format_historical_flight_data_int():
    #todo this lol
    print(f"Finished downloading international historical flight data.")

###############################################################################################
#test method

def test_method():
    delete_all_ascs_in_dir(historical_flight_data_downloaded_file_path_os_path)
    print(f"Finished downloading historical flight data.")