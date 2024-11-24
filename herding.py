#https://usaco.org/index.php?page=viewproblem2&cpid=915
cows = [int(x) for x in input().strip().split()]
cows.sort()

if cows[2] == cows[0]+2:
    print(0)
elif cows[1] == cows[0]+2 or cows[2] == cows[1]+2:
    print(1)
else:
    print(2)
    

maxmoves = 0
while True:
    cows.sort()
    if cows[0]+1== cows[1] and cows[1]+1==cows[2]:
        print(maxmoves)
        break
    first = cows[1]-cows[0]
    second = cows[2]-cows[1]
    if first>second:
        cows[2] = int((cows[0]+cows[1])/2)
        maxmoves+=1
    else:
        cows[0] = int((cows[1]+cows[2])/2)
        maxmoves+=1
    
