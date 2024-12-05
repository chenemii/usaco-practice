# https://usaco.org/index.php?page=viewproblem2&cpid=736
# 9:20 - 9:30
# 9:30 - looked at sol

n, m = [int(x) for x in input().strip().split()]
spot = []
plain = []
for i in range(n):
    spot.append([str(x) for x in input().strip()])
for i in range(n):
    plain.append([str(x) for x in input().strip()])

pos = 0
# mine: loop through by column, make lists for each column and compare lists
# solution: Loop by column, check each letter in spot with each one in plain

for i in range(m):
    common = False
    for j in range(n):
        for k in range(n):
            if spot[j][i] == plain[k][i]:
                common = True
                break

    if not common:
        pos+=1

print(pos)
