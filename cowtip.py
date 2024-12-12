# https://usaco.org/index.php?page=viewproblem2&cpid=689
'''
work from bottom right to top left
if tipped, untip

'''

n = int(input().strip())
square = []
for line in range(n):
    row = [int(x) for x in input().strip()]
    square.append(row)

count = 0

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if square[i][j] == 1:
            count+=1

            for k in range(i+1):
                for l in range(j+1):
                    if square[k][l] == 0:
                        square[k][l] = 1
                    else:
                        square[k][l] = 0
        
print(count)
