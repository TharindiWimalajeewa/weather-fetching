import requests

API_KEY = "API goes here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)

if response.status_code ==200:
    data = response.json()
    weather = data['weather'][0]["description"]
    print("weather: ", weather)
    temperature = data["main"]["temp"]
    print("temperature(Celcius): ",round(temperature-273))
else: print("An error occured")
