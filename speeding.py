# https://usaco.org/index.php?page=viewproblem2&cpid=568
# input data
# 2 lists
# compare mile by mile


with open("speeding.in") as read:
    n, m = [int(x) for x in read.readline().split()]

    road = [0]*101
    bessie = [0]*101

    currmile = 0
    for i in range(n):
        length, speed = [int(x) for x in read.readline().split()]
        for mile in range(currmile, currmile+length):
            road[mile] = speed
        currmile+=length

    currmile = 0
    for i in range(m):
        length, speed = [int(x) for x in read.readline().split()]
        for mile in range(currmile, currmile+length):
            bessie[mile] = speed
        currmile+=length

    maxx = 0
    for i in range(101):
        maxx = max(maxx, bessie[i]-road[i])

    with open("speeding.out", "w") as out:
        print(maxx, file=out)
