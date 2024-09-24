import requests

API_KEY = 'dbcee6578a60c82a8bb67071b9601724'  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# API_KEY = "https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key=API_KEY&include=minutely"
# BASE_URL = "https://api.weatherbit.io/v2.0/current"
def get_weather(city_name):
    """Fetch weather data for a specified city."""
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    print(complete_url)
    response = requests.get(complete_url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        
        # Parsing the data
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]
        
        weather_info = {
            "temperature": main['temp'],
            "humidity": main['humidity'],
            "pressure": main['pressure'],
            "wind_speed": wind['speed'],
            "description": weather['description'],
            "city": data['name'],
            "country": data['sys']['country']
        }
        
        return weather_info
    else:
        return None
get_weather('Chennai')

print(get_weather)
# # main.py
# import tkinter as tk
# from tkinter import messagebox
# from weather_api import get_weather  # Import the get_weather function

# def show_weather():
#     city = city_entry.get()
    
#     if not city:
#         messagebox.showerror("Input Error", "Please enter a city name.")
#         return
    
#     weather_data = get_weather(city)
    
#     if weather_data:
#         display_weather(weather_data)
#     else:
#         messagebox.showerror("Error", "City not found or unable to retrieve data.")

# def display_weather(weather_data):
#     result_text = f"Weather in {weather_data['city']}, {weather_data['country']}:\n"
#     result_text += f"Temperature: {weather_data['temperature']}°C\n"
#     result_text += f"Humidity: {weather_data['humidity']}%\n"
#     result_text += f"Pressure: {weather_data['pressure']} hPa\n"
#     result_text += f"Wind Speed: {weather_data['wind_speed']} m/s\n"
#     result_text += f"Description: {weather_data['description'].capitalize()}"
    
#     result_label.config(text=result_text)

# # Creating the GUI window
# root = tk.Tk()
# root.title("Weather Forecast")
# root.geometry("400x400")

# # Adding user input for city
# tk.Label(root, text="Enter City Name:").pack(pady=10)
# city_entry = tk.Entry(root)
# city_entry.pack(pady=5)

# # Button to trigger weather fetch
# tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

# # Label to display results
# result_label = tk.Label(root, text="", justify="left", font=("Helvetica", 12))
# result_label.pack(pady=10)

# # Start the GUI loop
# root.mainloop()
