import requests

class AnonymousApiClient:
    
    def get(self, url: str):
        raw_response = requests.get(url)
        return raw_response