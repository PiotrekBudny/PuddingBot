from api.jokeApiClient import JokeApiClient
import logging
import time

class Joke:
    def __init__(self, ctx):
        self.ctx=ctx
        
    async def execute_command(self):      
        try:
            jokeApi = JokeApiClient()
            joke_response = jokeApi.get_a_programming_joke()
            if hasattr(joke_response, "setup") and hasattr(joke_response, "delivery"):
                if joke_response.setup and joke_response.delivery:
                    await self.ctx.send(f'{joke_response.setup}')
                    time.sleep(5)
                    await self.ctx.send(f'{joke_response.delivery}')
            elif hasattr(joke_response, "joke"):
                if joke_response.joke:
                    await self.ctx.send(f'{joke_response.joke}')
                else:
                    raise Exception()
        except Exception as error:
            await self.ctx.send(f'Unable to fetch joke.')
            logging.warning(f'Unable to fetch joke {error}')
        
