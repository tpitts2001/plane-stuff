import variables
import os
import re
from collections import defaultdict
import glob

historical_flight_data_downloaded_file_path_os_path = os.path.realpath('../../'+variables.historical_flight_data_downloaded_file_path)


#todo delete all the files that don't contain 'combined'.

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

# Example usage
delete_files_with_db(historical_flight_data_downloaded_file_path_os_path)