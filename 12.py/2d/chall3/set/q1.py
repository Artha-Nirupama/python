set2D = {
  frozenset({1,2,3}),
  frozenset({2,3,4}),
  frozenset({4,5,6})
}
inlist = [x for y in set2D for x in y]
hes = {x for y in set2D for x in y}
outlist = [x for x in inlist if ]
print(outlist)
print(hes)
print(inlist)