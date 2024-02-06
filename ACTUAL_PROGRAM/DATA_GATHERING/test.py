import variables
import os
import re

def test1():
    repo_root_path = os.path.realpath('../../'+variables.historical_flight_data_downloaded_file_path)
    print(repo_root_path)
    historical_flight_data_downloaded_file_path = os.path.join(repo_root_path, variables.historical_flight_data_html_file_path)

    #print(historical_flight_data_downloaded_file_path)

def test2 ():
    import os

    # Step 2: Get the repository root path. This example assumes the script is run from the repo root.
    repo_root_path = os.getcwd()  # or specify manually, e.g., repo_root_path = '/path/to/repo/root'

    # Step 3: Define the relative path to the directory from the repo root
    relative_path_to_directory = variables.historical_flight_data_downloaded_file_path  # Example path

    print(repo_root_path)
    print(relative_path_to_directory)

    # Step 4: Combine the paths to get the absolute path
    directory_path = os.path.join(repo_root_path, relative_path_to_directory)

    #print(f"The OS path to the directory is: {directory_path}

import os

import os
import re


def rename_files_keep_date_range(historical_flight_data_downloaded_file_path_os_path):
    """
    Renames files in the specified directory to keep only the date range in the format "YYYYMM.YYYYMM".

    Parameters:
    - directory_path: Path to the directory where the files are located.
    """
    # Regular expression pattern to match date ranges in the format "YYYYMM.YYYYMM"
    date_range_pattern = re.compile(r'\d{6}\.\d{6}')

    # Check if the directory exists
    if not os.path.exists(historical_flight_data_downloaded_file_path_os_path):
        print(f"The directory {historical_flight_data_downloaded_file_path_os_path} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(historical_flight_data_downloaded_file_path_os_path):
        # Construct the full path of the file
        old_file = os.path.join(historical_flight_data_downloaded_file_path_os_path, filename)

        # Check if the current item is a file and not a directory
        if os.path.isfile(old_file):
            # Search for the date range in the file name
            match = date_range_pattern.search(filename)
            if match:
                # Extract the date range and construct the new file name
                date_range = match.group()
                new_file = os.path.join(historical_flight_data_downloaded_file_path_os_path, date_range + '.asc')

                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed '{filename}' to '{date_range + '.asc'}'")


# Example usage

# Example usage

historical_flight_data_downloaded_file_path_os_path = os.path.realpath('../../'+variables.historical_flight_data_downloaded_file_path)

rename_files_keep_date_range(historical_flight_data_downloaded_file_path_os_path)