from tkinter import *

window = Tk()

def submitf():
    foods=[]
    
    print("🤵Your oder is : ")
    
    for food in listbox.curselection():
        foods.insert(food,listbox.get(food))
    
    for displaying in foods:
        print(displaying)

def insertf():
    texts = Uinput.get()
    if Uinput != "":
        listbox.insert(listbox.size(),texts)
        listbox.config(height=listbox.size())
    Uinput.delete(0,END)
    
    for i in reversed(range(listbox.size())):
        if listbox.get(i)=="":
            listbox.delete(i)
    
def deletf():
    for food in reversed(listbox.curselection()):
        listbox.delete(food)
    listbox.config(height=listbox.size())

label = Label(window,text="The Food Menu🍽",font=("Ink Free",50,"bold"))
label.pack()

listbox = Listbox(window,font=("Ink Free",20,"bold"),selectmode=MULTIPLE)
listbox.pack()

listbox.insert(0,"Fired Rice")
listbox.insert(1,"Kotthu")
listbox.insert(2,"Pittu")
listbox.insert(3,"Soup")
listbox.insert(4,"Parata")

Uinput = Entry(window,font=("Ink Free",20,"bold"))
Uinput.pack()

submit = Button(window,text="Submit",command=submitf,font=("Ink Free",20,"bold"),compound="bottom")
submit.config(fg="#fad532",bg="#5fe91f",width=15)
submit.pack(side="left")

add = Button(window,text="Insert",command=insertf,font=("Ink Free",20,"bold"),compound="bottom")
add.config(fg="#fad532",bg="#1f4ee9",width=15)
add.pack(side="left")

delete = Button(window,text="Delete",command=deletf,font=("Ink Free",20,"bold"),compound="bottom")
delete.config(fg="#fad532",bg="#f02929",width=15)
delete.pack(side="left")

window.mainloop()