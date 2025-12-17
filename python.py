import requests
import tkinter as tk
from tkinter import messagebox
import json

# using the Tkinter library to create a simple GUI for the app

# Main window

root = tk.Tk()
root.title("Weather App")

# Create and configure lables and entry fields

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Creating a button to fetch weather data

fetch_button = tk.Button(root, text="Fetch Weather")
fetch_button.pack()

# Label to display weather information

weather_label = tk.Label(root, text="")
weather_label.pack()

# function to fetch weather data

def fetch_weather():
    city = city_entry.get()
    api_key = "d565bf6125d789248c4fe444c117c47b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
        print(data.text)
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")
fetch_button.config(command=fetch_weather)

# Start the GUI main loop
root.mainloop()