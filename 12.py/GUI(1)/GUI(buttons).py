from tkinter import *

count = 00

windows = Tk()

def click():
    global count
    count+=1
    display.config(text=f"{count:02}")

button = Button(windows,text="Click Here!")
button.config(font=("Times New Roman",40,"bold"))
button.config(bg="orange",fg="yellow")
button.config(activebackground="red",activeforeground="yellow")
button.config(command=click)


display = Label(windows)
display.config(font=("Times New Roman",60,"bold"),relief=RAISED,bd=8,compound="top")
display.pack()

button.pack()
windows.mainloop()