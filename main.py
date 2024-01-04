import requests
import json
import sys
import varibles

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

# Usage
api_key = get_api_key()
usa_airlines = get_airlines_by_country(api_key, 'United States')
for airline in usa_airlines:
    print(airline['airline_name'])