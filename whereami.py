# https://usaco.org/index.php?page=viewproblem2&cpid=964 hard
n = int(input().strip())
str = str(input().strip())

k = n

for i in range(1, n+1): #possible substring lengths
    s = set()
    for j in range(n-i+1): # max range given substring lengths
        s.add(str[j: j+i]) # adding substrings
    if len(s) == n-i+1: #substrings added - unique vs total substrings possible
        k = i
        print(k)
        break
    

