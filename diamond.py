# https://usaco.org/index.php?page=viewproblem2&cpid=639
#sort ascending
# if i and next i are less or equal  k apart, d +1
diamonds = []
with open("diamond.in") as read:
    n, k = [int(x) for x in read.readline().strip().split()]
    diamonds = [int(read.readline()) for _ in range(n)]

max_d = 0
for i in range(n):
    d = 0
    for j in range(i,n):
        if abs(diamonds[i]-diamonds[j])<=k:
            d+=1
    max_d = max(max_d, d)
with open("diamond.out", "w") as out:
    print(max_d, file = out)
