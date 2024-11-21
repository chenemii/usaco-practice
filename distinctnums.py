# https://cses.fi/problemset/task/1621

n = int(input())
nums = [int(x) for x in input().strip().split()]

nummy = 1
nums.sort()

for i in range(n-1):
    if nums[i] != nums[i+1]:
        nummy+=1

print(nummy)
