import requests
import json
import sys
import varibles
import csv

sys.path.append(r'C:\Users\fisht\PycharmProjects\plane stuff')

def get_api_key():
    # Retrieve the API key from varibles.py
    return varibles.access_key

def get_airlines_by_country(api_key, country):
    url = "http://api.aviationstack.com/v1/airlines"
    params = {'access_key': api_key}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        airlines = response.json()['data']
        return [airline for airline in airlines if airline['country_name'].lower() == country.lower()]
    else:
        print(f"Error: {response.status_code}")
        return None
def write_airlines_to_csv(airlines, filename):
    # Define the header for the CSV file
    headers = ['airline_name', 'iata_code', 'icao_code', 'country_name', 'fleet_size']

    # Open the file and write the data
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the header
        writer.writeheader()

        # Write the airline data
        for airline in airlines:
            writer.writerow({key: airline.get(key, '') for key in headers})

# Usage
api_key = get_api_key()
usa_airlines = get_airlines_by_country(api_key, 'United States')
for airline in usa_airlines:
    print(airline['airline_name'])

write_airlines_to_csv(usa_airlines, 'usa_airlines.csv')