# https://usaco.org/index.php?page=viewproblem2&cpid=713
# 5 min planning
# 20 min code

'''
2 lists
sort by starting
if next starting is less than current starting + time, 
    add current starting + time + next time
if equal/next starting has a gap between curent end

'''

n = int(input().strip())
s = []
t = []
for i in range(n):
    a, b = [int(x) for x in input().strip().split()]
    s.append(a)
    t.append(b)

sorted = sorted(zip(s, t), key = lambda x: x[0])
starting, time = list(zip(*sorted))

curr = starting[0] + time[0]
for i in range(1, n):
    if starting[i] < curr: # if overlapping
        curr += time[i]
        print(starting[i], time[i])
    else:
        curr = starting[i] + time[i]
print(curr)
