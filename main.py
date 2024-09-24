# main.py
import tkinter as tk
from tkinter import messagebox
from weather_forecast import get_weather  # Import the get_weather function

def show_weather():
    city = city_entry.get()
    
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    
    weather_data = get_weather(city)
    
    if weather_data:
        display_weather(weather_data)
    else:
        messagebox.showerror("Error", "City not found or unable to retrieve data.")

def display_weather(weather_data):
    result_text = f"Weather in {weather_data['city']}, {weather_data['country']}:\n"
    result_text += f"Temperature: {weather_data['temperature']}°C\n"
    result_text += f"Humidity: {weather_data['humidity']}%\n"
    result_text += f"Pressure: {weather_data['pressure']} hPa\n"
    result_text += f"Wind Speed: {weather_data['wind_speed']} m/s\n"
    result_text += f"Description: {weather_data['description'].capitalize()}"
    
    result_label.config(text=result_text)

# Creating the GUI window
root = tk.Tk()
root.title("Weather Forecast")
root.geometry("400x400")

# Adding user input for city
tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Button to trigger weather fetch
tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

# Label to display results
result_label = tk.Label(root, text="", justify="left", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the GUI loop
root.mainloop()
