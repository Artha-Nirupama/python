userList = []
while (userInput := input("Enter a word (type 'stop' to finish):")) != "stop" : 
    userList.append(userInput)
    out = [f"{i}-{x}" for i,x in enumerate(userList)]
    print(out)