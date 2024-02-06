import variables
from ACTUAL_PROGRAM.DATA_GATHERING import historical_flight_data as hfd

def get_historical_flight_data():

    hfd.download_historical_flight_data(variables.historical_flight_data_html_file_path, variables.historical_flight_data_downloaded_file_path, variables.historical_flight_data_base_domain)
    hfd.extract_and_delete_zip_folders(variables.historical_flight_data_downloaded_file_path)
    hfd.process_files_in_folder(hfd.historical_flight_data_downloaded_file_path_os_path)

    return