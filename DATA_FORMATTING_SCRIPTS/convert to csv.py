import csv
import os

def convert_to_csv(file_path, output_directory):
    # Create the output directory if it does not exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Extracting file name without extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Setting the path for the output CSV file
    csv_file_path = os.path.join(output_directory, f"{file_name}.csv")

    with open(file_path, 'r') as txt_file, open(csv_file_path, 'w', newline='') as csv_file:
        # Creating a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Reading and writing each line from the text file to the CSV file
        for line in txt_file:
            csv_writer.writerow(line.strip().split('\t'))

def process_subfolders(parent_folder, output_parent_folder):
    # List all subfolders in the parent folder
    subfolders = [f.path for f in os.scandir(parent_folder) if f.is_dir()]

    for subfolder in subfolders:
        # Extracting the name of the subfolder
        subfolder_name = os.path.basename(subfolder)

        # Creating a new subfolder path in the output parent folder
        new_output_directory = os.path.join(output_parent_folder, subfolder_name)

        # Specify the files to be converted in each subfolder
        files_to_convert = ['num.txt', 'pre.txt', 'sub.txt', 'tag.txt']
        for file_name in files_to_convert:
            file_path = os.path.join(subfolder, file_name)
            if os.path.exists(file_path):
                convert_to_csv(file_path, new_output_directory)

# Example usage
parent_folder = 'SEC income data/RAW' # Replace with the path to the folder containing subfolders
output_parent_folder = 'SEC income data/filtered' # Replace with the path to the parent folder for output
process_subfolders(parent_folder, output_parent_folder)
