from tkinter import *
from PIL import Image,ImageTk
windows = Tk()

x=IntVar()
y=IntVar()

def checking():
    if x.get()==1 and y.get()==0:
        print("I like Python and don't like Java")
    elif x.get()==0 and y.get()==1:
        print("I like Java and don't like Python")
    elif x.get()==1 and y.get()==1:
        print("I like both Python and Java")
    else:
        print("I don't like nether python and Java")
    
check1 = Checkbutton(windows,command=checking,variable=x,onvalue=1,offvalue=0)
check1.config(text="Python",font=("Ink Free",35,"bold"),fg="#373bfd",bg="#162519")
image1 = Image.open(r'C:\\Users\\Artha\\Documents\\python\\python\\12.py\\GUI(1)\\python-logo.png')#change the image location if shows error
image1 = image1.resize((30,30))
logo1 = ImageTk.PhotoImage(image1)
check1.config(image=logo1,compound="left")
check1.config(padx=5,pady=5,width=200,height=50)
check1.config(anchor='w')
check1.pack()

check2 = Checkbutton(windows,command=checking,variable=y,onvalue=1,offvalue=0)
check2.config(text="Java",font=("Ink Free",35,"bold"),fg="#373bfd",bg="#162519")
image2 = Image.open(r'C:\\Users\\Artha\\Documents\\python\\python\\12.py\\GUI(1)\\java-logo.png')
image2 = image2.resize((30,30))
logo2 = ImageTk.PhotoImage(image2)
check2.config(image=logo2,compound="left")
check2.config(padx=5,pady=5,width=200,height=50)
check2.config(anchor='w')
check2.pack()

windows.mainloop()