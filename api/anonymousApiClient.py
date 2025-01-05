import requests

class AnonymousApiClient():
    def Get(url: str) -> dict:
        raw_response = requests.get(url)
        data = raw_response.json()
        return data       