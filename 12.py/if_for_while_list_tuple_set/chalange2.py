nums = [10, 15, 20, 25, 30, 35]

newNums = [i for x,i in enumerate(nums) if x % 2 == 0]
print(newNums)