# data/api.py
import requests

def get_api_data(api_url):
    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data.get('results', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None
