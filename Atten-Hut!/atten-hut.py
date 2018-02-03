numcount = int(input())
#print(numcount)
nums = []
for i in range(numcount):
    temp = int(input())
    #print(temp)
    if (temp == 0):
        nums.pop(-1)
    else:
        nums.append(temp)
    #print(nums)
print(sum(nums))
