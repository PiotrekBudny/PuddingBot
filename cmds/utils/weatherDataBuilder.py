from cmds.utils.weatherData import WeatherData

class WeatherDataBuilder:
    
    def __init__(self, weatherData: WeatherData):
        self.weatherData = weatherData
        
    def _validate_weather_value(self, value: str):
        return value if value is not None else '----'
    
    def get_city(self):
        city = self._validate_weather_value(self.weatherData.city)
        return f'{city}'
    
    def get_temperature(self):
        temperature = self._validate_weather_value(self.weatherData.temperature)
        return f'{temperature}°C'
    
    def get_measuredOnDateTime(self):
        date = self._validate_weather_value(self.weatherData.measuredOnDate)
        time = self._validate_weather_value(self.weatherData.measuredOnHour)
        return f'Measured on: {date} {time}:00'
    
    def get_wind(self):
        windspeed = self._validate_weather_value(self.weatherData.wind)
        return f'Wind: {windspeed} km/h'
    
    def get_precipitation(self):
        precipitation = self._validate_weather_value(self.weatherData.precipitation)
        return f'Precipitation: {precipitation} mm'
    
    def get_airPressure(self):
        airPressure = self._validate_weather_value(self.weatherData.airPressure)
        return f'Air pressure: {airPressure} hPa'
    
    def get_data_source(self):
        return f'Source: imgw.pl'