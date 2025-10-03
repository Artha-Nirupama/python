set_2d = {frozenset({1, 2, 3}), frozenset({4, 5, 6}), frozenset({8, 9, 7})}

totle = {x for y in set_2d for x in y}
print(totle)