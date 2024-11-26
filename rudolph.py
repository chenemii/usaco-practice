#https://codeforces.com/contest/1846/problem/D
n, length, height = [int(x) for x in input().strip().split()]
location = [int(x) for x in input().strip().split()]

# find area of all branches
# see if branches overlap
# if overlap, subtract intersection

area = 0

area += n*(0.5*length*height)

for i in range(n-1):
    h2 = location[i]+height - location[i+1]
    if h2 > 0:
        slope = length/height
        b2 = slope*h2
        coveredarea = 0.5*b2*h2
        area -= coveredarea

print(area)
