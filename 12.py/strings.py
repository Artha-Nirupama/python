x = 0

while x == 0:

    Uname = input("Enter your name(Please do not enter spaces and digits maxchar=12): ")

    if Uname.isalpha() and Uname.count(" ") == 0 and len(Uname) <= 12 :
        print(f"Hello {Uname}! Welcome")
        x = 1
    else:
        print("Invalid user name and try agin!")