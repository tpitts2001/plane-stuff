import os
import pandas as pd

# Directory containing the CSV files
directory = 'flight data/filtered for model/with quarter identification'

# Iterate through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Remove the 'Month-Year' column
        if 'month-year' in df.columns:
            df.drop('month-year', axis=1, inplace=True)

            # Save the modified file (uncomment the line for the desired option)

            # Option 1: Overwrite the original file
            df.to_csv(file_path, index=False)

            # Option 2: Save as a new file (e.g., with "_modified" appended to the filename)
            #new_file_path = os.path.join(directory, filename.split('.csv')[0] + '_modified.csv')
            #df.to_csv(new_file_path, index=False)

        else:
            print(f"'Month-Year' column not found in {filename}")

print("Processing complete.")