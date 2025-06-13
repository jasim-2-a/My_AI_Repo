import requests

def real_weather(city_name, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city_name.title()}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"☀️ Description: {description}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.HTTPError:
        print("❌ Error: Invalid city name or API key.")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")

def main():
    print("===== Real Time Weather (OpenWeatherMap) =====")
    city = input("Enter your city name (e.g., Lahore): ")
    
    # ✅ Your actual API key inserted here
    api_key = "4fee9b8231e3c1e9638bf0a86a890846"
    
    real_weather(city, api_key)

if __name__ == "__main__":
    main()
