from PIL import Image, ImageDraw, ImageFont
import io
from datetime import datetime
from cmds.utils.weatherData import WeatherData
from cmds.utils.weatherDataBuilder import WeatherDataBuilder

class WeatherImage():

    def __init__(self):
        pass
    
    def _get_font(self, size: int):
            try:
                font = ImageFont.truetype("calibrib.ttf", size)
            except IOError:
                font = ImageFont.load_default()
                
            return font
    
    def _check_if_it_is_daytime(self):
        current_time = datetime.now()
    
        day_start = 6  # 6 AM
        day_end = 18   # 6 PM

        current_hour = current_time.hour

        if day_start <= current_hour < day_end: return True
        else: return False
    
    def create_weather_image(self, data: dict):           
            
            if(self._check_if_it_is_daytime()):
                background = Image.open('resources/day_weather.jpg')
                fontColor = (255,255,255)
            else:
                background = Image.open('resources/night_weather.jpg')
                fontColor =  (255,255,255)
            
            weatherData = WeatherData(city=data.get("stacja"),temperature=data.get("temperatura"), measuredOnDate = data.get("data_pomiaru"), measuredOnHour = data.get("godzina_pomiaru"),
                                       wind=data.get("predkosc_wiatru"), precipitation=data.get("suma_opadu"), airPressure=data.get("cisnienie"))

            weatherDataBuilder = WeatherDataBuilder(weatherData)
                      
            draw = ImageDraw.Draw(background)
            
            if (len(weatherDataBuilder.get_temperature()) > 4):
                temperatureFont = self._get_font(70)
            else:
                temperatureFont = self._get_font(80)
            
            cityFont = self._get_font(40)
            footerFont = self._get_font(14)
            additionalInfoFont = self._get_font(17)
            
            draw.text(text=weatherDataBuilder.get_city(), font=cityFont, fill=fontColor, xy=[10,10])
            draw.text(text=weatherDataBuilder.get_temperature(), font=temperatureFont, fill=fontColor, xy=[270,70])
            draw.text(text=weatherDataBuilder.get_measuredOnDateTime(), font=footerFont, fill=fontColor, xy=[10, 280])
            draw.text(text=weatherDataBuilder.get_data_source(), font=footerFont, fill=fontColor, xy=[400, 280])
            draw.text(text=weatherDataBuilder.get_wind(), font=additionalInfoFont, fill=fontColor, xy=[10, 100])
            draw.text(text=weatherDataBuilder.get_precipitation(), font=additionalInfoFont, fill=fontColor, xy=[10, 120])
            draw.text(text=weatherDataBuilder.get_airPressure(), font=additionalInfoFont, fill=fontColor, xy=[10, 140])

            byte_io = io.BytesIO()
            background.save(byte_io, 'PNG')
            byte_io.seek(0)
            
            return byte_io