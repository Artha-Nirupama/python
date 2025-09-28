animals = ["cat", "dog", "rabbit"]
for index,animal in enumerate(animals):
    print(index,animal)
    
for index,char in enumerate("Python"):
     print(index,char)
     
fruits = [x==input("Enter the furit name:") for x in range(3)]

for index,fruit in enumerate(fruits):
    print(index,fruit)
    