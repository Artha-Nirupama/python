from tkinter import *

window = Tk()
window.title("Entry")

def submitf():
    username = Uinput.get()
    print(f"Hello! {username}")
    
def backspacef():
    Uinput.delete(len(Uinput.get())-1,END)
    
def deletef():
    Uinput.delete(0,END)

Uinput = Entry(window,font=("Ink Free",40),fg="#2be049",bg="#373d38")
Uinput.pack()

submit = Button(window,text="Submit",command=submitf,compound="bottom")
submit.config(fg="white",bg="green",font=("Times New Roman",30,"bold"))
submit.pack(side = RIGHT)

backspace = Button(window,text="Backspace",command=backspacef,compound="bottom")
backspace.config(fg="white",bg="black",font=("Times New Roman",30,"bold"))
backspace.pack(side = RIGHT)

delete = Button(window,text="Delete",command=deletef,compound="bottom")
delete.config(fg="white",bg="red",font=("Times New Roman",30,"bold"))
delete.pack(side = RIGHT)

window.mainloop()