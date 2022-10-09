# Sky.py -  module to get weather data
# aka knowing if its hot without even opening my door
import requests

class Sky:
    def __init__(self):
        pass

    def get_weather(self):

        API_KEY  = "218977d47345c7b68bba837d21cb2d47"
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

        city = "clarksville"
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)
        
        data = response.json()
        #print(data)
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        temp = round(1.8*(temperature-273) + 32.)
        #? equation to turn it from kelvin to fahrenheit and round 
        return weather, temp #? Returns tuple and has to be this order when using function
        
#? How to use |
#?           \_/
if __name__ == "__main__":
    S = Sky()
    weather,temp = S.get_weather()
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}")

#works perfectly fine problaly going to add the "feels like" data