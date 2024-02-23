import tkinter as tk
from tkinter import messagebox
import requests

def clear_entry(event):
    if entry_city.get() == "Enter City Name":
        entry_city.delete(0, tk.END)

def get_weather():
    city = entry_city.get()
    if city == "Enter City Name":
        messagebox.showwarning("Warning", "Please enter a city name.")
        return

    api_key = "db4477b447a7dd380ca92c006487953a"  # Enclose the API key in quotes
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"]

        weather_info = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {description}"
        result.set(weather_info)

        # Dynamically adjust window size based on the length of weather details
        lines = weather_info.split('\n')
        window_height = 200 + len(lines) * 20  # Adjust the base height and add extra height for each line
        root_weather.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    except Exception as e:
        messagebox.showwarning("Error", f"Failed to get weather data. {e}")

# Create main window
root_weather = tk.Tk()
root_weather.title("Weather Forecast")
root_weather.configure(bg="#f0f0f0")

# Create UI elements
entry_city = tk.Entry(root_weather, font=("Helvetica", 12))
entry_city.insert(0, "Enter City Name")
entry_city.bind("<FocusIn>", clear_entry)
result = tk.StringVar()

# Place UI elements in the window
title_label = tk.Label(root_weather, text="Weather Forecast", font=("Helvetica", 16, "bold"), bg="White")
title_label.pack(pady=5)
entry_city.pack(pady=5)

frame = tk.Frame(root_weather, bg="#f0f0f0")
frame.pack()

get_button = tk.Button(frame, text="Get Weather", command=get_weather, font=("Helvetica", 12), bg="#4CAF50", fg="white")
get_button.pack(side="left", padx=5 , pady=5)

# Adding space between the button and the result label
space_frame = tk.Frame(frame, height=10, bg="#f0f0f0")
space_frame.pack(side="left")

result_label = tk.Label(root_weather, textvariable=result, font=("Helvetica", 12), wraplength=400, justify="left", anchor="w", bg="#f0f0f0", padx=5, pady=5)
result_label.pack()

# Apply padding and center the window
window_width = 400
screen_width = root_weather.winfo_screenwidth()
screen_height = root_weather.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - 200) / 2)  # Base height
root_weather.geometry(f"{window_width}x120+{x_coordinate}+{y_coordinate}")

# Run the weather forecast application
root_weather.mainloop()
