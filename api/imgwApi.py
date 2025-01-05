from anonymousApiClient import AnonymousApiClient

class ImgwApi():
    
    def GetWeatherFromPolishCity(city: str) -> dict:
        url = f'https://danepubliczne.imgw.pl/api/data/synop/station/{city}'
        return AnonymousApiClient().Get(url)