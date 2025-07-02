from api.anonymousApiClient import AnonymousApiClient

class ImgwApi():
    
    base_url = 'https://danepubliczne.imgw.pl/api/data/synop/station'
         
    def get_weather_for_polish_city(self, city: str) -> dict:
        url = f'{self.base_url}/{city}'
        response =  AnonymousApiClient.get(url)
        
        if(response.status_code == 404):
            raise Exception("Station not found.")
        
        data = response.json()
        return data
    
    def get_all_weather_station_data(self):
        response =  AnonymousApiClient.get(self.base_url)
        return response.json()
        
    