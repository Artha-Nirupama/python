from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("My First GUI")

img = Image.open(r"C:\\Users\\Artha\\Documents\\python\\python\\12.py\\GUI(1)\\logo.png")
img = img.resize((400,400))
logo = ImageTk.PhotoImage(img)

label1 = Label(window,text="Welcome to Gaming Community!😼",font=("Times New Roman",50,"bold"),
               fg="red",bg="black",relief=RAISED,bd=10,padx=10,pady=10,image=logo,compound="top")

label1.pack()

window.geometry("1050x500")

window.mainloop()