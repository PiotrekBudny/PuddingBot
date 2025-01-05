import requests

class AnonymousApiClient():
    
    def Get(url: str):
        raw_response = requests.get(url)
        return raw_response