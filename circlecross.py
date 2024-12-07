# https://usaco.org/index.php?page=viewproblem2&cpid=712
# 1:25 -1:32 understanding
# 1:32-1:50 coding and debugging

'''
go through string
    for each letter, find its second letter
        add the amount of unfinished pairs in the middle 
'''

stringy = str(input().strip())
pairs = 0

for i in range(52): # go thru each letter
    for j in range(i+1, 52): # find its pair
        if stringy[j] == stringy[i] and j-i != 1:
            seen = set()
            for k in range(i+1, j): # find number of unfinished pairs inside the pair
                if stringy[k] not in seen:
                    for l in range(j+1, 52): # find the pairs inside j-i
                        if stringy[k] == stringy[l]:
                            pairs+=1
                            break
                seen.add(stringy[k])
print(pairs)



