import os
import shutil


def replace_files(source_dir, destination_dir):
    # Ensure trailing slash is present for consistency
    source_dir = os.path.join(source_dir, '')
    destination_dir = os.path.join(destination_dir, '')

    # Check if both directories exist
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    if not os.path.exists(destination_dir):
        print(f"Destination directory {destination_dir} does not exist.")
        return

    # List and remove all files in the destination directory
    for filename in os.listdir(destination_dir):
        file_path = os.path.join(destination_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    # Copy all files from source to destination
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)
        print('Replaced' + destination_file + 'with' + source_file)

        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)  # copy2 to preserve metadata
        elif os.path.isdir(source_file):
            shutil.copytree(source_file, destination_file)

    print("Files replaced successfully.")


# Prompt user for source and destination folder paths
source_folder = '/mnt/300gig-drv/PycharmProjects/plane-stuff/historical-data/historical-flight-data/raw'
destination_folder = '/mnt/300gig-drv/PycharmProjects/plane-stuff/historical-data/historical-flight-data/temp'

replace_files(source_folder, destination_folder)
