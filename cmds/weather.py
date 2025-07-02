from api.imgwApi import ImgwApi
import logging
from cmds.utils.weatherImage import WeatherImage
import discord
import unicodedata
import re

class Weather:
    def __init__(self, ctx, city: str):
        self.city=city
        self.ctx=ctx
    
    def _normalize_polish_city_name(self, city: str) -> str:
        normalized_text = unicodedata.normalize('NFD', city)
        
        polish_to_non_polish = {
        'ł': 'l', 'Ł': 'L', 'ó': 'o', 'Ó': 'O', 'ą': 'a', 'Ą': 'A', 
        'ę': 'e', 'Ę': 'E', 'ś': 's', 'Ś': 'S', 'ć': 'c', 'Ć': 'C',
        'ż': 'z', 'Ż': 'Z', 'ź': 'z', 'Ź': 'Z', 'ń': 'n', 'Ń': 'N',
        'ą': 'a', 'ę': 'e', 'ż': 'z'
        }
        
        city_name_without_polish_chars = ''.join(polish_to_non_polish.get(c, c) for c in normalized_text)        
        city_name_without_polish_chars = city_name_without_polish_chars.replace(" ", "")
        
        return re.sub(r'[^a-zA-Z\s]', '', city_name_without_polish_chars).lower()
        
    async def execute_command(self):
        data: dict
        city = self._normalize_polish_city_name(self.city)
        
        try:
            imgw = ImgwApi()
            data = imgw.get_weather_for_polish_city(city)
        except Exception as error:
            await self.ctx.send(f'Unable to fetch weather.')
            logging.warning(f'Unable to get weather {error}')
        
        weatherImg = WeatherImage()
        
        byte_io = weatherImg.create_weather_image(data)
        await self.ctx.send(file=discord.File(byte_io, filename='image.png'))