import variables
import os
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

    #print(f"The OS path to the directory is: {directory_path}")


test1()