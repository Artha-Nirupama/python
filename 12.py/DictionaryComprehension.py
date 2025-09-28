cuDic = { x : pow(x,3) for x in range(6)}
print(cuDic)

y = "hello"
letCount = {x : y.count(x) for x in y}
print(letCount)

li = ["apple","banana","cherry"]
countDi = {x : len(x) for x in li}
print(countDi)