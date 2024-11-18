
#https://usaco.org/index.php?page=viewproblem2&cpid=735
with open("lostcow.in") as read:
    x, y = [int(x) for x in read.readline().split()]

n = 1
distance = 0
p = x
c = x

while(True):
    print(c,p)
    if(y>= min(c, p) and y<= max(c,p)):
        distance += abs(y-p)
        break
    distance +=abs(c-p)
    p = c
    c = x+n
    n*=-2
    

with open("lostcow.out", "w") as out:
    print(distance, file = out)
