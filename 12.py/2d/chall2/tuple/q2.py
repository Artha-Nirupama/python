tuple_2d =((1,2,3),
          (2,4,6),
          (3,6,9))
tupCheck = tuple(x for y in tuple_2d for x in y)

while True:
    userInput = int(input("enter your number: "))
    outSet = {y for y in tupCheck if y==userInput}
    if len(outSet)==1:
        print("The number is exists!😉")
        break
    else:
        print("The number is not exists!😐")
