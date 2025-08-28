
try:
    country=input("1.USA or 2.Europe?")      #this program for USA pepole
    coun=int(country)
except:
    conn=3
fl =0

if coun==1:
    fl = input('Enter your floor: ')
    fl = int(fl)
    print('The floor is',fl)

elif coun==2:
    fl = input('Enter your floor: ')
    fl = int(fl)
    fl = fl-1
    print('The floor is',fl)
else:
    print("Wrong user input!")
