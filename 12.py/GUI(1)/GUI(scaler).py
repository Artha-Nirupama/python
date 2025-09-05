from tkinter import *

window = Tk()
window.title("Temparatur scaler!")

label = Label(window,text="The Scaler🧐",font=("Ink Free",40,"bold"),compound="top")
label.pack()

def sumbitf():
    if scaler.get() > 40:
        print(f"{scaler.get()}°C temparatur is realy hot 🥵")
    elif scaler.get() < 18:
        print(f"{scaler.get()}°C temparatur is realy cool 🥶")
    else:
        print(f"{scaler.get()}°C temparatur is realy good 😎")

scaler = Scale(window,from_=100,to=0,font=("Times New Roman",25,"bold"),resolution = 5,orient="vertical",tickinterval=10,troughcolor="#3250fa",length=600,fg="#76ecf5",bg="#4a495a")
scaler.pack()

submit = Button(window,text="Submit",command=sumbitf,compound="bottom",font=("Times New Roman",30,"bold"),padx=10,pady=5,relief=RAISED,bd=5,fg="#faed32",bg="#fa6132")
submit.pack()

window.mainloop()