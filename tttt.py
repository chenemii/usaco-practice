# Did not work for all test cases! Did not control for the teams must have 2 present on board
#https://usaco.org/index.php?page=viewproblem2&cpid=831
# go thru each row, col, diagonal
# if row/col/diagonal has all one type, independent +=1
# if --- has all 2 types, team +=1
# go to next one
lines = []
for i in range(3):
    lines.append(list(input().strip()))
print(lines)

indiv = 0
team = 0

for row in range(3):
    if lines[row][0] == lines[row][1] == lines[row][2]:
        indiv+=1
    if (lines[row][0] == lines[row][1] or lines[row][1] == lines[row][2] or lines[row][0] == lines[row][2]) and (lines[row][0] != lines[row][1] or lines[row][1] != lines[row][2] or lines[row][0] != lines[row][2]):
        team+=1
    print(team, "row")
for col in range(3):
    if lines[0][col] == lines[1][col] == lines[2][col]:
        indiv+=1
    if (lines[0][col] == lines[1][col] or lines[1][col] == lines[2][col] or lines[0][col] == lines[2][col]) and (lines[0][col] != lines[1][col] or lines[1][col] != lines[2][col] or lines[0][col] != lines[2][col]):
        team+=1
    print(team, "col")
        
if lines[0][0] == lines[1][1] == lines[2][2]:
    indiv +=1
if (lines[0][0] == lines[1][1] or lines[0][0] == lines[2][2] or lines[1][1] == lines[2][2]) and (lines[0][0] != lines[1][1] or lines[0][0] != lines[2][2] or lines[1][1] != lines[2][2]):
    team+=1
    print(team, "diag1")
if lines[0][2] == lines[1][1] == lines[2][0]:
    indiv+=1
if (lines[0][2] == lines[1][1] or lines[0][2] == lines[2][0] or lines[2][0] == lines[1][1]) and (lines[0][2] != lines[1][1] or lines[0][2] != lines[2][0] or lines[2][0] != lines[1][1]):
    team+=1
    print(team, "diag2")

print(indiv, team)

