# https://usaco.org/index.php?page=viewproblem2&cpid=1011
# 8 - 8:05
# 8:05 - 8:25 - attempt 1
# 8:25 - 8:50 - attempt 2
# no

n = int(input().strip())
xcoord = []
ycoord = []
for i in range(n):
    a, b = [int(x) for x in input().strip().split()]
    xcoord.append(a)
    ycoord.append(b)

maxarea = 0
for i in range(n): #corner
    for j in range(n): # parallel
        for k in range(n): # above or below
            if ycoord[i] == ycoord[j] and xcoord[i] == xcoord[k]:
                area = abs((xcoord[j]-xcoord[i]) * (ycoord[k]-ycoord[i]))
                maxarea = max(area, maxarea)

print(maxarea)
