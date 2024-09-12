# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:24:35 2024

@author: recha
"""
from tkinter import *
import tkinter as tk
import math
import json
import requests
from statistics import mean
from tkinter import messagebox

root = Tk()
root.resizable(False, False)
import pandas as pd
valid = False


capital_cities = [
                  [0,213,680,594,288,890],[213,0,546,638,485,687],
                  [680,546,0,267,1033,935],[594,638,267,0,1163,952],
                  [288,485,1033,1163,0,1172],[890,687,935,952,1172,0]
                  ]

df = pd.DataFrame(capital_cities, columns= ['london','paris','berlin','copenhagen','dublin','rome'])   
df.index = ['london','paris','berlin','copenhagen','dublin','rome']

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&hourly=temperature_2m&forecast_days=1&models=ukmo_seamless"
r = requests.get(url)
results = json.loads(r.text)
pd.DataFrame(results)
database = pd.json_normalize(results)
dataset = database.iloc[0]['hourly.temperature_2m']
temperature = max(dataset)
finaltemp = math.trunc(temperature)
print(temperature)

def retrieve():
    location1 = input_field.get()
    location1 = location1.lower()
    input_field.delete(0, END)
    location2 = input_field2.get()
    location2 = location2.lower()
    input_field2.delete(0,END)
    try:
        Distance = df.loc[location1,location2]
        messagebox.showinfo("Distance", "The distance between "  + location1 + " and " + location2  + " is " + str(Distance) )
    except:
        messagebox.showerror("Error","Input not on List")
        

root.geometry("958x958")
root.title('Loc8tor')
input_field = Entry(root, width =15, font = ('Arial', 14))
input_field.place(x=350, y=300)
input_field2 = Entry(root, width = 15, font = ('Arial', 14))
input_field2.place(x=350, y=360)


prompt = Label(root, text = 'Please input two capital cities from the available list: London ,Paris ,Berlin ,Copenhagen ,Dublin ,Rome')
prompt.place(x=160, y = 200)


weather = Label(root, text = "Today's highest temperature is: " + str((finaltemp))  )
weather.place(x=330, y=800)


submit = Button(root, text='submit', command=retrieve)
submit.place(x=410, y= 700 )


Location2 = input_field2.get()

root.mainloop()