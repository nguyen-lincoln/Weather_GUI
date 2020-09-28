import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
    except:
        final_str = 'Invalid Entry'
    return final_str


def get_weather(city):
    api_key = '32738a39806b1707ab65af54c419a360'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': api_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size = int(lower_frame.winfo_height()*.25)
    img = ImageTk.PhotoImage(Image.open('./img/' + icon + '.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()
root.title("Weather GUI")
icon = Image.open('icon.ico')
iconImg = ImageTk.PhotoImage(icon)
root.iconphoto(False, iconImg)


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_image = tk.PhotoImage(file='Gray-Transparent-Background.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.image = bg_image
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='gray', bd=5)
frame.place(relx=.5, rely=.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 14))
entry.place(relwidth=.69, relheight=1)

button = tk.Button(frame, text="GET WEATHER", font=('Courier', 14), command=lambda: get_weather(entry.get()))
button.place(relx=.7, relwidth=.3, relheight=1)

lower_frame = tk.Frame(root, bg='gray', bd=5)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

label = tk.Label(lower_frame, bg='#606060', font=('Courier', 17), fg='white', anchor='w', justify='left')
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='#606060', highlightthickness=0, bd=0)
weather_icon.place(relx=0, rely=0, relwidth=1, relheight=.5)

root.mainloop()
