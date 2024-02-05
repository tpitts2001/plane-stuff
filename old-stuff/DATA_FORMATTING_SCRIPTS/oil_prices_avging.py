import pandas as pd


def average_prices_per_quarter(input_csv, output_csv):
    # Load the historical-data
    df = pd.read_csv(input_csv)

    # Directly extract the year from the 'Date' column using the first four characters
    df['Year'] = df['Date'].str[:4].astype(int)

    # Group by 'Year' and 'Quarter', then calculate the average price
    quarterly_averages = df.groupby(['Year', 'Quarter'])['Price'].mean().reset_index()

    # Rename columns for clarity
    quarterly_averages.columns = ['Year', 'Quarter', 'Price']

    # Save to a new CSV file
    quarterly_averages.to_csv(output_csv, index=False)

    print(f"File saved to {output_csv}")


# Define input and output file paths
input_csv = 'historical-data/crude_oil_data/raw/crude_oil_prices_2006-2019.csv'
output_csv = 'historical-data/crude_oil_data/rolled_into_quarter_avg/quarterly_oil_prices.csv'

# Execute the function
average_prices_per_quarter(input_csv, output_csv)
