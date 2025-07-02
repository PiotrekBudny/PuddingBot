from api.imgwApi import ImgwApi
import logging
from cmds.utils.weatherImage import WeatherImage
import discord

class weatherLowestTemp:
    def __init__(self, ctx):
        self.ctx=ctx
    
    def get_lowest_value(self, data) -> dict:
        iteration = 0
        lowest_temp_station: dict
        list = data
        
        for iteration in range(len(list)):
            
            if (list[iteration]['temperatura'] is None):
                continue
            
            if iteration == 0:
                lowest_temp_station=list[iteration]
                continue
            
            if (list[iteration]['temperatura'] is None):
                continue
            currentLowestTemp=float(lowest_temp_station['temperatura'])
            analysedTemp=float(list[iteration]['temperatura'])
            
            if  currentLowestTemp > analysedTemp:
                lowest_temp_station = list[iteration]
            
        return lowest_temp_station
     
    async def execute_command(self):      
        try:
            imgwApi = ImgwApi()
            data = imgwApi.get_all_weather_station_data()
        except Exception as error:
            await self.ctx.send(f'Unable to fetch weather.')
            logging.warning(f'Unable to get weather {error}')
        
        lowestTempStationData = self.get_lowest_value(data)
        weatherImg = WeatherImage()
        
        byte_io = weatherImg.create_weather_image(lowestTempStationData)
        await self.ctx.send(file=discord.File(byte_io, filename='image.png'))