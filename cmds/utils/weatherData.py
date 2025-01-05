class WeatherData:
    
    def __init__(self, city: str, temperature: str, measuredOnDate: str, measuredOnHour: str, wind: str, precipitation: str, airPressure: str):
        self.city = city
        self.temperature = temperature
        self.measuredOnDate = measuredOnDate
        self.measuredOnHour = measuredOnHour
        self.wind = wind
        self.precipitation = precipitation
        self.airPressure = airPressure