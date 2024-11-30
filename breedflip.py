# https://usaco.org/index.php?page=viewproblem2&cpid=1012

n = int(input().strip())
a = list(input().strip())
b = list(input().strip())

i = 0
flips = 0

while i<n:
    if a[i] != b[i]:
        start = i
        while i<n and a[i] != b[i]:
            i+=1
        flips +=1
    else:
        i+=1

print(flips)
