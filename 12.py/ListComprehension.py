squ = [pow(x,2) for x in range(11)]

print(squ)

even = [ x for x in range(20) if x%2 == 0]
print(even)

fui = ["apple", "mango", "kiwi", "banana"]

fuInFour = [x for x in fui if len(x)>4]
print(fuInFour)