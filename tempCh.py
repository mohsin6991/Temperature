import tkinter as tk  # Importing the tkinter library for creating the GUI
from tkinter import messagebox  # Importing the messagebox module for showing alerts and information
import requests  # Importing the requests library for making HTTP requests to the weather API

# API key for accessing the OpenWeatherMap API
api_key = '8a46d79fd2f88d4fa68b6340974de346'

# Function to get weather data for a given city using the OpenWeatherMap API
def get_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'  # Base URL for the weather API
    params = {
        'q': city,  # City name parameter
        'appid': api_key,  # API key parameter
        'units': 'metric'  # Units parameter to get temperature in Celsius
    }
    response = requests.get(base_url, params=params)  # Sending a GET request to the API
    data = response.json()  # Parsing the response as JSON

    if response.status_code == 200:  # Checking if the request was successful
        main = data['main']  # Extracting the main part of the response which contains the weather data
        weather = {
            'temperature': main['temp'],  # Extracting the temperature
            'humidity': main['humidity'],  # Extracting the humidity
            'pressure': main['pressure'],  # Extracting the pressure
            'wind_speed': data['wind']['speed'],  # Extracting the wind speed
            'precipitation': data['weather'][0]['description']  # Extracting the weather description (precipitation)
        }
        return weather  # Returning the extracted weather data as a dictionary
    else:
        return None  # Returning None if the request was not successful

# Function to display the weather data in a message box
def show_weather():
    city = city_entry.get()  # Getting the city name entered by the user
    if city:  # Checking if the city name is not empty
        weather = get_weather(api_key, city)  # Fetching the weather data for the entered city
        if weather is not None:  # Checking if the weather data was successfully fetched
            # Creating a message string with the weather information
            message = (f"Current weather in {city}:\n"
                       f"Temperature: {weather['temperature']}°C\n"
                       f"Humidity: {weather['humidity']}%\n"
                       f"Pressure: {weather['pressure']} hPa\n"
                       f"Wind Speed: {weather['wind_speed']} m/s\n"
                       f"Precipitation: {weather['precipitation'].capitalize()}")
            messagebox.showinfo("Weather Information", message)  # Displaying the weather information in an info message box
        else:
            messagebox.showerror("Error", "City not found or an error occurred.")  # Displaying an error message if the city is not found or an error occurred
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")  # Displaying a warning message if the city name is empty

# Creating the main application window
root = tk.Tk()
root.title("Weather App")  # Setting the title of the window

# Adding a label to prompt the user to enter a city name
tk.Label(root, text="Enter your city:").pack(pady=10)
city_entry = tk.Entry(root)  # Creating an entry widget for the user to enter the city name
city_entry.pack(pady=5)

# Adding a button to trigger the show_weather function when clicked
tk.Button(root, text="Get Weather", command=show_weather).pack(pady=20)

root.mainloop()  # Starting the main event loop to run the application
