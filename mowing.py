# https://usaco.org/index.php?page=viewproblem2&cpid=593
# some grid
# traverse along grid, keep track of each step and time it was at
# if we pass through step again, put that coordinate somewhere
# at the end, subtract time2 and time 1 to find max x

# 9:15-9:30 - thinking
# 9:30-9:45 - code
# 9:45 - 10 - debugging

# list of all coords?

n = int(input().strip())
directions = []
steps = []
for i in range(n):
    a, b = input().strip().split()
    directions.append(str(a))
    steps.append(int(b))

coords = []
twice = []
starting = [0,0]

for i in range(n):
    for j in range(steps[i]):
        if directions[i] == "N":
            starting[1]+=1

        if directions[i] == "S":
            starting[1]-=1
    
        if directions[i] == "E":
            starting[0]+=1

        if directions[i] == "W":
            starting[0]-=1
    
        curr = starting.copy()

        for k in range(len(coords)):
            if curr == coords[k]: 
                twice.append(k)
                twice.append(len(coords))
        coords.append(curr)


maxx = float("inf")
if len(twice) == 0:
    print(-1)
else:
    for i in range(0,len(twice)-1,2):
        maxx = min(abs(twice[i+1]-twice[i]), maxx)
    print(maxx)
