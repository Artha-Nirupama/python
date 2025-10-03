set2D = {frozenset({x,x+1}) for x in range(1,6,2)}
out = {y for y in set2D if y == frozenset({3,4})}

if out:
    print("It exists😁")
else:
    print("It not exists😐")