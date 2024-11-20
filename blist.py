#https://usaco.org/index.php?page=viewproblem2&cpid=856 - hard
# starting time list
# ending time list
# buckets needed per cow
# buckets list of size total buckets
# var for highest bucket num used
# start from first starting, take away i buckets.
# compare first ending and second starting . if second starting is smaller, go to that. otherwise go to ending. add/remove buckets



change = [0 for _ in range(1001)]
with open("blist.in") as read:
    n = int(read.readline())
    for i in range(n):
        start, end, amt = [int(x) for x in read.readline().split()]
        change[start] +=amt
        change[end] -= amt

maxx = 0
curr = 0
for i in range(1001):
    curr+=change[i]
    maxx = max(curr, maxx)

with open("blist.out", "w") as out:
    print(maxx, file = out)
