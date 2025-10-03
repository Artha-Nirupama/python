list2d = [[1,2,3,4,5],
        [1,6,3,4,5],
        [1,4,3,4,5],
        [1,6,3,4,5],
        [1,8,3,4,5]]
list1d = [x for y in list2d for x in y if x %2 == 0]
print(list1d)