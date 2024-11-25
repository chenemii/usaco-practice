# https://usaco.org/index.php?page=viewproblem2&cpid=783
x1, y1, x2, y2 = [int(x) for x in input().strip().split()]
x3, y3, x4, y4 = [int(x) for x in input().strip().split()]

tarp = (x2-x1)*(y2-y1)
xs = []
ys = []

for i in range(x1, x2+1):
    for j in range(y1, y2+1):
        if x3 <= i <= x4 and y3 <= j <= y4:
            xs.append(i)
            ys.append(j)

coveredlength = xs[len(xs)-1]-xs[0]
coveredheight = ys[len(ys)-1]-ys[0]

if coveredheight == y2-y1:
    tarp = abs(xs[0]-x1)*(y2-y1)

print(tarp)
