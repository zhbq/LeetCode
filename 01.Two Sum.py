
nums = input().split()
target = input()
nums = [int(i) for i in nums]
i = 0
while True:
    remain = int(target) - nums[0]
    nums.pop(0)
    if remain in nums: 
        print(i,nums.index(remain)+i+1)
        break
    i = i+1