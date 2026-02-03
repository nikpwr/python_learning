import requests


def retrieveGoldPrice() -> dict:

    response = requests.get('https://freegoldapi.com/data/latest.json')
    data = response.json()
    latest = data[-1]
    return latest
