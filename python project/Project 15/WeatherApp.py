from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Weather App")
win.config(bg="blue")
win.geometry("500x570")
name_label=Label(win,text="Weather App",font=("Time New Roman",35,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather App",font=("Time New Roman",20,"bold"),values=list_name)
com.place(x=25,y=120,height=50,width=450)



done_button=Button(win,text="Done",font=("Time New Roman",20,"bold"))
done_button.place(x=200,y=190,height=50,width=100)

w_label=Label(win,text="Weather Climate",font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

wb_label=Label(win,text="Weather Description",font=("Time New Roman",17))
wb_label.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

per_label=Label(win,text="Pressure",font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)


win.mainloop()