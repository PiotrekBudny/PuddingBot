from PIL import Image, ImageDraw, ImageFont
import io
from datetime import datetime

class WeatherImage():

    def __init__(self):
        pass
    
    def GetFont(self, size: int):
            try:
                font = ImageFont.truetype("calibrib.ttf", size)
            except IOError:
                font = ImageFont.load_default()
                
            return font
    
    def check_if_it_is_daytime(self):
        current_time = datetime.now()
    
        day_start = 6  # 6 AM
        day_end = 18   # 6 PM

        current_hour = current_time.hour

        if day_start <= current_hour < day_end: return True
        else: return False
    
    def create_weather_image(self, data: dict):           
            
            if(self.check_if_it_is_daytime()):
                background = Image.open('resources/day_weather.jpg')
                fontColor = (255,255,255)
            else:
                background = Image.open('resources/night_weather.jpg')
                fontColor =  (255,255,255)
            
            city = data['stacja']
            temperature = f'{data['temperatura']}°C'
            measuredOn = f'Measured on: {data['data_pomiaru']} {data['godzina_pomiaru']}:00'
            wind = f'Wind: {data['predkosc_wiatru']} km/h'
            precipitation = f'Precipitation: {data['suma_opadu']} mm'
            airPressure = f'Air pressure: {data['cisnienie']} hPa'
            source = f'Source: imgw.pl'
            
            draw = ImageDraw.Draw(background)
            
            cityFont = self.GetFont(40)
            temperatureFont = self.GetFont(80)
            footerFont = self.GetFont(14)
            additionalInfoFont = self.GetFont(17)
            
            draw.text(text=city, font=cityFont, fill=fontColor, xy=[10,10])
            draw.text(text=temperature, font=temperatureFont, fill=fontColor, xy=[270,70])
            draw.text(text=measuredOn, font=footerFont, fill=fontColor, xy=[10, 280])
            draw.text(text=source, font=footerFont, fill=fontColor, xy=[400, 280])
            draw.text(text=wind, font=additionalInfoFont, fill=fontColor, xy=[10, 100])
            draw.text(text=precipitation, font=additionalInfoFont, fill=fontColor, xy=[10, 120])
            draw.text(text=airPressure, font=additionalInfoFont, fill=fontColor, xy=[10, 140])

            byte_io = io.BytesIO()
            background.save(byte_io, 'PNG')
            byte_io.seek(0)
            
            return byte_io