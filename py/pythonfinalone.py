from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz
import requests
from PIL import ImageTk,Image
from tkinter.ttk import *
import os

root=tk.Tk()
root.title("Weather predictor")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    city=textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj= TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=87658f1f86e1731baabd33831fc87135"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    description=json_data['weather'][0]['description']
    temp=int(json_data['main']['temp']-273.15)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

bi=ImageTk.PhotoImage(Image.open("nature.jpg"))
l=tk.Label(root,image=bi)
l.pack(side="bottom",fill="y",expand="yes")
root.configure(background='black')

Search_image=ImageTk.PhotoImage(Image.open("cloudy-day.png"))
myimage=tk.Label(root,image=Search_image)
myimage.place(x=200,y=150)

Search_image1=ImageTk.PhotoImage(Image.open("snow.png"))
myimage=tk.Label(root,image=Search_image1)
myimage.place(x=300,y=150)

Search_image2=ImageTk.PhotoImage(Image.open("storm.png"))
myimage=tk.Label(root,image=Search_image2)
myimage.place(x=400,y=150)

Search_image3=ImageTk.PhotoImage(Image.open("sun.png"))
myimage=tk.Label(root,image=Search_image3)
myimage.place(x=500,y=150)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=57)
textfield.focus()

search_icon=ImageTk.PhotoImage(Image.open("search.png"))
myimage_icon=tk.Button(root,image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=360,y=50)

box_image=ImageTk.PhotoImage(Image.open("rounded-rectangle.png"))
myimage=tk.Label(root,image=box_image)
myimage.place(x=100,y=300)


name=Label(root,font=("arial",15,"bold"))
name.place(x=40,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=40,y=130)



l=Label(root,text="WIND")
l.config(font=("Courier",14))
l.place(x=120,y=300)

l1=Label(root,text="HUMIDITY")
l1.config(font=("Courier",14))
l1.place(x=260,y=300)

l2=Label(root,text="DESCRIPTION")
l2.config(font=("Courier",14))
l2.place(x=450,y=300)

l3=Label(root,text="PRESSURE")
l3.config(font=("Courier",14))
l3.place(x=650,y=300)

t=Label(root,font=("arial",50,"bold"))
t.place(x=650,y=150)
c=Label(font=("ariel",15,'bold'))
c.place(x=650,y=250)


w=Label(root,text="...")
w.config(font=("Courier",14))
w.place(x=120,y=350)
h=Label(root,text="...")
h.config(font=("Courier",14))
h.place(x=260,y=350)
d=Label(root,text="...")
d.config(font=("Courier",14))
d.place(x=450,y=350)
p=Label(root,text="...")
p.config(font=("Courier",14))
p.place(x=650,y=350)



           


root.mainloop()


