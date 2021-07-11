
import tkinter as tk
import requests
import datetime
import time

def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    print(updated_at)
    date = datetime.datetime.fromtimestamp(updated_at/1e3)



    label.config(text = "\n" + "Total Cases: "+total_cases+"\n"+
        "\n"+"Total Deaths: "+total_deaths+"\n"+
        "\n"+"Today Cases: "+today_cases+"\n"+
        "\n"+"Today Deaths: "+today_deaths+"\n"+
        "\n"+"Today Recovered: "+today_recovered+"\n")

    label2.config(text = "Updated at:  "+ str(date))

canvas = tk.Tk()
canvas.geometry("500x600")
canvas.title("Corona Tracker App")
canvas.config(bg = '#caf7e3')
f = ("calibiri", 15, "bold")
f1 = ("calibiri", 12, "italic")

tk.Label(canvas, font = f, text = "Click on load to get latest covid data",bg = '#caf7e3').pack(pady=20)
button =  tk.Button(canvas, font = f, text = "Load", command = getCovidData)
button.pack(pady = 20)

label = tk.Label(canvas, font = f,bg = '#caf7e3')
label.pack(pady=20)

label2 = tk.Label(canvas, font = f1,bg = '#caf7e3')
label2.pack()
getCovidData()

canvas.mainloop()