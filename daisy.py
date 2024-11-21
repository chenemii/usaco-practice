# https://usaco.org/index.php?page=viewproblem2&cpid=1060
n = int(input().strip())
flowers = [int(x) for x in input().strip().split()]

count = 0

for i in range(n):
    for j in range(i,n):
        avg = sum(flowers[i : j+1])/(j-i+1)
        for k in range(i, j+1):
            if flowers[k] == avg:
                count+=1
                break

print(count)
