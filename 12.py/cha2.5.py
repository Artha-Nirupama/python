evenSET = {f"{i}-{x}" for i,x in enumerate([y for y in range(20) if int(y) % 2 == 0])}
print(evenSET)