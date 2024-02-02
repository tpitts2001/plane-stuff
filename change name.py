import os
import re

def rename_file(filepath):
    filename = os.path.basename(filepath)
    match = re.search(r'\d{6}', filename)
    if match:
        date_str = match.group()
        new_date_str = f"{date_str[4:6]}-{date_str[0:4]}"
        new_filename = new_date_str + os.path.splitext(filename)[1]
        new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
        return new_filepath
    else:
        return None

def rename_files_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        new_filepath = rename_file(filepath)
        if new_filepath:
            os.rename(filepath, new_filepath)
            print(f"Renamed '{filename}' to '{os.path.basename(new_filepath)}'")

# Replace 'your_directory_path' with the path to your folder
your_directory_path = 'data/flight_data/RAW ASC/international'
rename_files_in_directory(your_directory_path)