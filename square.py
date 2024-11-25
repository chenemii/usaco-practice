# https://usaco.org/index.php?page=viewproblem2&cpid=663

x1, y1, x2, y2 = [int(x) for x in input().strip().split()]
x3, y3, x4, y4 = [int(x) for x in input().strip().split()]

max = max(x2, x4)
min = min(x1, x3)
side = max-min

print(side*side)
