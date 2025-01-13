import requests
import os
def city_coordinates(city, api_key):
    url_loc='https://api.openweathermap.org/geo/1.0/direct'
    params_loc={
       'q':city,
       'limit': 1,
       'appid':api_key
    }
    resp=requests.get(url_loc,params=params_loc)
    resp.raise_for_status()
    city_loc=resp.json()
    if city_loc:
        return city_loc[0]['lat'], city_loc[0]['lon']
    else:
        return None, None
    
def weather_info(lat, lon, api_key):
    url='https://api.openweathermap.org/data/2.5/weather'
    params={
       'lat':lat,
       'lon': lon,
       'appid':api_key,
       'units':'metric'

    }
    res=requests.get(url,params=params)
    res.raise_for_status()
    return res.json()

def display_weather_info(city, info):
    temp=info['main']['temp']
    feels_like=info['main']['feels_like']
    humidity=info['main']['humidity']
    desc=info['weather'][0]['description']
    print(f'City: {city}')
    print(f'Temperature: {temp}°C')
    print(f'Feels like: {feels_like}°C')
    print(f'Humidity: {humidity}%')
    print(f'Weather description: {desc.capitalize()}')

    
if __name__=='__main__':
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("API key not found! Set the OPENWEATHER_API_KEY environment variable.")
    city = input("Enter the city name: ").strip()
    if city:
        try:
            lat, lon = city_coordinates(city, api_key)
            if lat and lon:
                weather_data = weather_info(lat, lon, api_key)
                display_weather_info(city, weather_data)
            else:
                print(f"No location found for city: {city}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("City name cannot be empty!")


