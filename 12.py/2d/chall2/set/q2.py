set2D = {frozenset({x,x+1}) for x in range(1,6,2)}

set1D = {x for y in set2D for x in y}
print(set1D)