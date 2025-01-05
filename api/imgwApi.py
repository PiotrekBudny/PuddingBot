from api.anonymousApiClient import AnonymousApiClient

class ImgwApi():
    
    def GetWeatherFromPolishCity(city: str) -> dict:
        url = f'https://danepubliczne.imgw.pl/api/data/synop/station/{city}'
        response =  AnonymousApiClient.Get(url)
        
        if(response.status_code == 404):
            raise Exception("Station not found.")
        
        data = response.json()
        return data