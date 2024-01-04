import requests
import json
import sys
import varibles

sys.path.append(r'C:\Users\fisht\PycharmProjects\plane stuff')

def get_api_key():
    # Retrieve the API key from varibles.py
    return varibles.access_key

def get_global_airlines(api_key):
    url = "http://api.aviationstack.com/v1/airlines"
    params = {
        'access_key': api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return json.loads(response.text)['data']
    else:
        print(f"Error: {response.status_code}")
        return None


# Usage
api_key = get_api_key()
if api_key:
    airlines = get_global_airlines(api_key)
    if airlines:
        for airline in airlines:
            print(airline['airline_name'], airline['iata_code'])