tuple_2d = (
  (1,2,3),
  (4,5,6),
  (7,8,9)
)
tuple_1d = tuple(x for y in tuple_2d for x in y)
print(tuple_1d)