import pandas as pd
import os

def get_quarter(month):
    if 1 <= month <= 3:
        return '1'
    elif 4 <= month <= 6:
        return '2'
    elif 7 <= month <= 9:
        return '3'
    else:
        return '4'

def add_quarter_column_to_csv(input_folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    for filename in os.listdir(input_folder_path):
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, filename)
            try:
                df = pd.read_csv(input_file_path)

                # Ensure the 'Date of Data: Month' column exists
                if 'Date of Data: Month' in df.columns:
                    df['Quarter'] = df['Date of Data: Month'].apply(get_quarter)
                    df.to_csv(output_file_path, index=False)
                    print(f"Processed and saved file: {output_file_path}")
                else:
                    print(f"Column 'Date of Data: Month' not found in {filename}")

            except Exception as e:
                print(f"Error processing file {filename}: {e}")

# Specify the input and output folder paths here
input_folder_path = 'flight_data/filtered for model/without'
output_folder_path = 'flight_data/filtered for model/with quarter identification'
add_quarter_column_to_csv(input_folder_path, output_folder_path)
