fruits = ["apple", "kiwi", "banana", "pear", "grape", "mango"]

newFruits = {x:len(x) for x in fruits if len(x) >= 5}
print(newFruits)