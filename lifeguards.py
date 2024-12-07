# https://usaco.org/index.php?page=viewproblem2&cpid=784
# 5:50 - 5:55
# 5:55 - 6:15


n = int(input().strip())
starting = []
ending = []
for i in range(n):
    a, b = [int(x) for x in input().strip().split()]
    starting.append(a)
    ending.append(b)

sorted = sorted(zip(ending, starting), key = lambda x:x[0])
sortedending, sortedstarting = list(zip(*sorted))

maxtime = 0

for i in range(n): # remove each i
    time = 0
    for t in range(1, max(ending)+1): # check each minute
        for j in range(n): # make sure minute is being covered
            if j!=i:
                if starting[j] <= t < ending[j]:
                    time+=1
                    break
    maxtime = max(time, maxtime)

print(maxtime)
