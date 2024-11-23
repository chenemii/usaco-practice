# https://cses.fi/problemset/task/1640
size, target = [int(x) for x in input().strip().split()]
listy = [int(x) for x in input().strip().split()]

found = False

for i in range(size):
    for j in range(i+1,size):
        if listy[i]+listy[j] == target:
            print(i+1, j+1)
            found = True
            break
if found == False:
    print("IMPOSSIBLE")
