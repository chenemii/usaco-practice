#https://usaco.org/index.php?page=viewproblem2&cpid=665

# first loop thru each character in each line and duplicate it by k times
# then duplicate each line by k times

with open("cowsignal.in") as read:
    height, width, scale = [int(x) for x in read.readline().split()]
    signal = [read.readline().strip() for _ in range(height)]

with open("cowsignal.out", "w") as out:
    for row in signal:
        for repeatrow in range(scale):
            for col in row:
                for repeatcol in range(scale):
                    print(col, end="", file=out)
            print(file = out)

