# https://usaco.org/index.php?page=viewproblem2&cpid=963
# 7:55 - 8:05
# 8:05 - 8:40 - looked at sol

# mine: for every cow what is always behind it

k, n = [int(x) for x in input().strip().split()]
rankings = []
for i in range(k):
    rankings.append([int(x) - 1 for x in input().strip().split()])

# Check every possible pair for 2 cows and sees if their rankings are consistent
pairs = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for x in rankings:
            if x.index(i) < x.index(j):
                break
            else:
                pairs+=1

print(pairs)
