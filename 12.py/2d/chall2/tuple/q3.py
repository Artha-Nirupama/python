tuple_2d =((1,2,3),
          (2,4,6),
          (3,6,9))
rev2DTuple = reversed(tuple_2d)
rev1dTuple = [x for y in rev2DTuple for x in y]
print(rev1dTuple) 