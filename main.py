from tkinter import *
from tkinter import ttk
import requests
def data_get():
    city=city_name.get()
    data= requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=4a25accb531aeb9f279bd26c145efe3d").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(round(data["main"]["temp"]-273.15))+"°C")
    pressure_label1.config(text=data["main"]["pressure"])
win = Tk()
win.title("The Skyline")
win.config(bg="pink")
win.geometry("500x500") 

name_label = Label(
    win,
    text="The Skyline", 
    font=("Times New Roman", 30, "bold"),
    bg="pink",
    fg="black"
)
name_label.place(x=25, y=50, height=50, width=450)
city_name=StringVar()
list_name=["Delhi",
    "Mumbai",
    "Kolkata",
    "Chennai",
    "Bengaluru",
    "Hyderabad",
    "Pune",
    "Ahmedabad"
    
    
]
com=ttk.Combobox(win,
    text="The Skyline",values=list_name,
    font=("Times New Roman", 30, "bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)
w_label = Label(
    win,
    text="weather climate",
    font=("Times New Roman", 12,"bold"),
)
w_label.place(x=25, y=260, height=40, width=110)
w_label1 = Label(
    win,
    text="t",
    font=("Times New Roman", 22,"bold"),
)
w_label1.place(x=150, y=260, height=40, width=210)
wb_label = Label(
    win,
    text="weather description",
    font=("Times New Roman", 10,"bold"),
)
wb_label.place(x=25, y=440, height=40, width=110)
wb_label1 = Label(
    win,
    text=" ",
    font=("Times New Roman", 10,"bold"),
)
wb_label1.place(x=150, y=440, height=40, width=210)
temp_label = Label(
    win,
    text="Temperature",
    font=("Times New Roman", 15,"bold"),
)
temp_label.place(x=25, y=320, height=40, width=110)
temp_label1 = Label(
    win,
    text=" ",
    font=("Times New Roman", 15,"bold"),
)
temp_label1.place(x=150, y=320, height=40, width=210)
pressure_label = Label(
    win,
    text="pressure",
    font=("Times New Roman", 15,"bold"),
)
pressure_label.place(x=25, y=380, height=40, width=110)
pressure_label1 = Label(
    win,
    text=" ",
    font=("Times New Roman", 15,"bold"),
)
pressure_label1.place(x=150, y=380, height=40, width=210)

done_button=Button(win,
    text="DONE",
    font=("Times New Roman", 20, "bold"),
command=data_get)
done_button.place(y=190,height=50,width=100,x=200)

win.mainloop()