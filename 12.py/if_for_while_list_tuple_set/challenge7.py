UserList = []
while True:
    UserInput = input("Please enter your word(exit=stop):")
    
    if UserInput == "stop":
        break
    else:
        UserList.append(UserInput)
outputList = [x.upper() for x in UserList if len(x)>3]        
print(outputList)