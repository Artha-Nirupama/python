from tkinter import *

windows = Tk()

languaes = ["Python","Java","Rust","JavaScript"]

def checking():
    match x.get():
        case 0:
            print("I choose Python!")
        case 1:
            print("I choose Java")
        case 2:
            print("I choose Rust")
        case 3:
            print("I choose JavaScript")
            
x=IntVar()

label = Label(windows,font=("Ink Free",40,"bold"),fg="blue",text="Please select a language!",compound="top")
label.pack()

for language in range(len(languaes)):
    radiobutton = Radiobutton(windows,text=languaes[language],value=language,variable=x,command=checking,font=("Ink Free",40,"bold"))
    radiobutton.pack(anchor='w')
windows.mainloop()