from api.anonymousApiClient import AnonymousApiClient
from api.models.joke_response import JokeResponse

class JokeApiClient:
    
    base_joke_url = 'https://v2.jokeapi.dev/joke/'
    
    def get_a_programming_joke(self):
        url = f"{self.base_joke_url}Programming"
        
        response = AnonymousApiClient().get(url)
        if response.status_code == 200:
            json = response.json()
            joke_response = JokeResponse(**json)
            return joke_response
        else:
            raise Exception("No joke returned")
        
        