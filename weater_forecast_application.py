# Weather Forecast Application
import requests

# Replace 'your_api_key_here' with your actual API key from OpenWeatherMap
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("❌ City Not Found. Please check the spelling.\n")
        else:
            main = data["main"]
            weather = data["weather"][0]
            print(f"\n🌤 Weather in {city.capitalize()}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Condition: {weather['description'].capitalize()}\n")
    except requests.exceptions.RequestException as e:
        print("❌ Error fetching data:", e)

def main():
    print("--- Weather Forecast Application ---")
    while True:
        city_name = input("Enter city name (or type 'exit' to quit): ")
        if city_name.lower() == 'exit':
            print("👋 Exiting Weather App. Goodbye!")
            break
        get_weather(city_name)

if __name__ == "__main__":
    main()
