# https://usaco.org/index.php?page=viewproblem2&cpid=1251
# read: 3 min
# code: 5 min - correct but time limit exceeded (inefficient)

'''
mine: checks every possible tuition value and counts possuble cows
sol: checks only values in tuitions and sorts to count possible cows
'''

n = int(input().strip())
tuitions = [int(x) for x in input().strip().split()]
tuitions.sort()

maxtuition = 0
maxmoney = 0

for i in range(n):
    curr = tuitions[i] * (n-i)   
    if curr > maxmoney:
        maxtuition = tuitions[i]
        maxmoney = curr
print(maxmoney, maxtuition)
