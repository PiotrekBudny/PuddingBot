from api.imgwApi import ImgwApi
import logging

class Weather:
    def __init__(self, ctx, city: str):
        self.city=city
        self.ctx=ctx
    
    def execute_command(self):
        data: dict
        
        try:
            data = ImgwApi.GetWeatherFromPolishCity(self.city)
        except:
            self.ctx.send(text=f'Unable to fetch weather.')
            raise Exception(f'Unable to get weather.')
        
        station = data['stacja']
        date = data['data_pomiaru']
        hour = data['godzina_pomiaru']
        temp = data['temperatura']
        wind = data['predkosc_wiatru']
        wind_direction = data['kierunek_wiatru']
        humididty = data['wilgotnosc_wzgledna']
        rain_volume = data['suma_opadu']
        air_pressure = data['cisnienie']
                
        
        

        
        
        