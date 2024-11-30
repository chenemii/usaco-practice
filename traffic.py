# https://usaco.org/index.php?page=viewproblem2&cpid=917
# start from beginning
# on = add to both
# off = subtract from both
# if on ->  add max to both
# if off -> subtract max off from both 
# if none -> take max of first, and min of second

n = int(input().strip())
type = [""]*n
minnums = [0]*n
maxnums = [0]*n
for i in range(n):
    a, b, c = input().strip().split()
    type[i] = a
    minnums[i] = int(b)
    maxnums[i] = int(c)

currsmall = 0
currlarge = float("inf")

for i in range(n-1, -1, -1):
    if type[i] == "on":
        currsmall-=minnums[i]
        currlarge-=maxnums[i]
        currsmall = max(0, currsmall)
    if type[i] == "off":
        currsmall+=maxnums[i]
        currlarge+=minnums[i]
    if type[i] == "none":
        currsmall = max(currsmall, minnums[i])
        currlarge = min(currlarge, maxnums[i])
print(currsmall, currlarge)

for i in range(n):
    if type[i] == "none":
        firstnone = i
        break

currsmall = 0
currlarge = float("inf")

for i in range(n):
    if type[i] == "on":
        currsmall+=minnums[i]
        currlarge+=maxnums[i]
    if type[i] == "off":
        currsmall-=maxnums[i]
        currlarge-=minnums[i]
        currsmall = max(0, currsmall)
    if type[i] == "none":
        currsmall = max(currsmall, minnums[i])
        currlarge = min(currlarge, maxnums[i])
print(currsmall, currlarge)





