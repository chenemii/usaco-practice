# https://codeforces.com/contest/1808/problem/B

t = int(input())
chips = [0]*t

for blah in range(t):
    n, m = (int(x) for x in input().strip().split())

    list = []
    for i in range(n):
        list.append([int(x) for x in input().strip().split()])

    for i in range(n-1):
        for j in range(i,n):
            A = list[i]
            B = list[j]
            for k in range(m):
                chips[blah] += abs(A[k]-B[k])

for x in chips:
    print(x)

