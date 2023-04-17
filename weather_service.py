import requests

api_key = "129f96a54f0ea96553a85b95a535eca6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        if "main" in data:
            temp = round(float(data["main"]["temp"]) - 273.15, 2) # convertir Kelvin a Celsius
            humidity = data["main"]["humidity"]
        else:
            temp = "Unknown"
            humidity = "Unknown"

        if "weather" in data:
            weather = data["weather"][0]["description"]
        else:
            weather = "Unknown"

        if "wind" in data:
            wind_speed = data["wind"]["speed"]
        else:
            wind_speed = "Unknown"

        return {"weather": weather, "temp": temp, "humidity": humidity, "wind_speed": wind_speed}
    else:
        return {"error": "City not found."}

print(get_weather("London, GB"))
