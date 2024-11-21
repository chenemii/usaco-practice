#https://usaco.org/index.php?page=viewproblem2&cpid=615
# 17x + 25y = 77

# diff = abs(M and current total)

# loop multiplying x up to 1000
# inner loop multiplying y up to 1000
# compare total w M every time

with open("pails.in") as read:
    x, y, m = [int(x) for x in read.readline().strip().split()]

diff = m

for i in range(int(m/x)+1):
    for j in range(int(m/y) + 1):
        if(x*i + j*y)>m:
            continue
        diff = min((m-(x*i + j*y)), diff)

with open("pails.out", "w") as out:
    print(m-diff, file = out)



