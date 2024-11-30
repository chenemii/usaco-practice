# https://usaco.org/index.php?page=viewproblem2&cpid=1301

n, k = [int(x) for x in input().strip().split()]
days = [int(x) for x in input().strip().split()]


cost = k+1
lastday = days[0]

for i in days:
    if i-lastday < k+1:
        cost+= i-lastday
    else:
        cost+=k+1

    lastday=i


print(cost)
