ro2d = ((1,2,3),
        (4,5,6),
        (7,8,9))
roResult = tuple(tuple((y,y-3,y-6))for y in range(7,10))
print(roResult)
