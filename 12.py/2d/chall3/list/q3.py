matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
firstD = [x for y in matrix for x in y if x in range(1,10,4)]
print(sum(firstD))

secoundD = [x for y in matrix for x in y if x in range(3,8,2)]
print(sum(secoundD))