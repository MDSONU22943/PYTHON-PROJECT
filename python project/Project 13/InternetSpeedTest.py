from tkinter import *
import speedtest

def speedCheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    download=str(round(sp.download()/(10**6),3))+"Mbps"
    upload=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=download)
    lab_up.config(text=upload)

sp=Tk()
sp.geometry("500x650")
sp.title("Internet Speed Test")
sp.config(bg="Blue")
lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="blue",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Downloading Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Uploading Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_up=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_up.place(x=60,y=360,height=50,width=380)

button=Button(sp,text="Check Speed",font=("Time New Roman",30,"bold"),relief=RAISED,bg="red",command=speedCheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()