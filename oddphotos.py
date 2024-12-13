# https://usaco.org/index.php?page=viewproblem2&cpid=1084 no

n = int(input().strip())
even, odd = 0, 0

cows = [int(x) for x in input().strip().split()]
for c in cows:
    if c % 2 == 0:
        even +=1
    else:
        odd+=1

while odd > even:
    odd -=2
    even+=1

if even> odd + 1:
    even = odd + 1

print(even+odd)
