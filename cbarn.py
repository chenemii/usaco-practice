# https://usaco.org/index.php?page=viewproblem2&cpid=616
#7+8*2+6*3+4*4 = 57
# 8*1+6*2+4*3+4*4 = 48
# simulate each door

n = int(input().strip())
cows = []
for i in range(n):
    cows.append(int(input().strip()))

mindist = float("inf")
distance = 0

# for each starting room, multiply number for each room by doors
for i in range(n): # starting rooms
    doors = 0
    distance = 0
    for j in range(n):
        distance+=cows[(i+j)%n]*doors
        doors+=1
        print(distance)
    mindist = min(distance, mindist)
print(mindist)
