list2d = [[1,2,3,4,5],
    [1,6,3,4,5],
    [1,4,3,4,5],
    [1,6,3,4,5],
    [1,8,3,4,5]]
totleByrow = [f"count:{sum(x)}" for x in list2d]
print(totleByrow)