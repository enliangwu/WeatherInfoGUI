import tkinter
from tkinter import END
import requests
import time

'''
@author Enliang Wu
reference: evanemran

This is a weather GUI app that requires a input of a city name, 
then it will display the weather information of that city
'''


def set_app():
    def get_weather():
        city = input_text.get()
        res = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                           + city + "&appid=ceeb7ae863c13d5ec02da765470b82f3")

        res_json = res.json()
        diff_temp = 273.15
        diff_gmt_est = 18000
        condition = res_json['weather'][0]['main']
        temp = int(res_json['main']['temp'] - diff_temp)
        min_temp = int(res_json['main']['temp_min'] - diff_temp)
        max_temp = int(res_json['main']['temp_max'] - diff_temp)
        pressure = res_json['main']['pressure']
        humidity = res_json['main']['humidity']
        wind = res_json['wind']['speed']
        sunrise = time.strftime('%H:%M:%S', time.gmtime(res_json['sys']['sunrise'] - diff_gmt_est))
        sunset = time.strftime('%H:%M:%S', time.gmtime(res_json['sys']['sunset'] - diff_gmt_est))

        input_text.delete(0, END)
        final_info = city + "\n\n" + condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " \
                     + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " \
                     + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" \
                     + "Sunrise: " + sunrise + "EST" + "\n" + "Sunset: " + sunset + "EST"
        label1.config(text=final_info)
        label2.config(text=final_data)

    screen = tkinter.Tk()  # set up a GUI
    screen.title("Weather App")
    screen.geometry("500x500")

    font1 = ("poppins", 20)
    font2 = ("poppins", 35, "bold")
    welcome_text = tkinter.Label(screen, text="Please enter the city name", font=font2, fg="red", bg="yellow")
    welcome_text.pack(pady=10)

    input_text = tkinter.Entry(screen, justify='center', width=20, font=font2)
    input_text.pack(pady=10)
    input_text.focus()
    # input_text.bind('<Return>', get_weather)

    button = tkinter.Button(text="GET WEATHER", command=get_weather)
    button.pack(pady=10)

    label1 = tkinter.Label(screen, font=font1)
    label1.pack()
    label2 = tkinter.Label(screen, font=font1)
    label2.pack()

    screen.mainloop()  # put the application in a main loop


if __name__ == "__main__":
    set_app()
