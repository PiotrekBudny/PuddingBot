from api.anonymousApiClient import AnonymousApiClient
from api.models.joke_two_part_response import JokeTwoPartResponse
from api.models.joke_single_part_response import JokeSinglePartResponse

class JokeApiClient:
    
    base_joke_url = 'https://v2.jokeapi.dev/joke/'
    
    def get_a_programming_joke(self):
        url = f"{self.base_joke_url}Programming"
        
        response = AnonymousApiClient().get(url)
        if response.status_code == 200:
            json = response.json()
            try:
                return JokeTwoPartResponse(**json)
            except (TypeError, KeyError) as e:
                try:
                    return JokeSinglePartResponse(**json)
                except Exception as finalException:
                    raise finalException    
        else:
            raise Exception("No joke returned")
        
        