# https://codeforces.com/problemset/problem/1914/C
# take 1st for each one, tracks BEST 2nd row one

totalquests, monoquests = [int(x) for x in input().strip().split()]
points1 = [int(x) for x in input().strip().split()]
points2 = [int(x) for x in input().strip().split()]

first = points1[0]
bestnext = points2[0]

points = points1[0] + bestnext*(monoquests-1) # adds 2nd for the rest of quests as current max

for i in range(1, min(totalquests, monoquests)):
    bestnext = max(points2[i], bestnext) # update to highest of 2nds
    points = max(points, first + points1[i] + bestnext * (monoquests-i-1)) # adds 2nd for rest of quests
    first+=points1[i]

print(points)


# old code
# count = 0
# for i in range(1, min(totalquests, monoquests)):
#    if count==monoquests:
#       break
#    points+=points1[i]
#    count+=1

#    if(i!=(len(points1)-1) and points2[i]>=points1[i+1] and count<=monoquests):
#       points+=points2[i]
#       count+=1


#if count<monoquests:
#    for i in range(min(totalquests, monoquests)):
#        if(i!=(len(points1)-1) and points2[i]<points1[i+1] and count<=monoquests):
#            points+=points2[i]
#            count+=1

#print(points)
