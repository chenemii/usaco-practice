# https://usaco.org/index.php?page=viewproblem2&cpid=687
# 5 min
# 15 min


'''
make a dict of all 
    make sure its in total amounts
find min 
find second from min
    tie - if multiple or none
print newline at the end

'''

n = int(input().strip())
cows = {}
for i in range(n):
    a, b = input().strip().split()
    name = str(a)
    milk = int(b)
    if name in cows:
        cows[name]+=milk
    else:
        cows[name] = milk

scows = dict(sorted(cows.items(), key = lambda x: x[1]))

m = 0
second = 0
for c in scows:
    if m == 0 and len(scows) >= 7:
        m = scows[c]
    if scows[c] > m:
        second = scows[c]
        break

list = []
for c in scows:
    if scows[c] == second:
        list.append(c)

if len(list) == 1:
    print(list[0], "\n")
    
else:
    print("Tie\n")



