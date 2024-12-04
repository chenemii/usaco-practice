# Code is wrong!!!
# https://usaco.org/index.php?page=viewproblem2&cpid=1228
# 4:25 - 4:40
# 4:40-5 
# 5 - 5:10


# find the largest overlapping range of Gs and Ls
# sort all Gs and Ls
# largest L and smallest G
# second largest L and see if greater than smallest, then second smallest G
# second smallest G and see if greater than largest L, then second largest L
# if yes, keep
# if no, add to count

# actual logic: simulate each position of each cow - find liars at each position, take min liars, do for left and right

n = int(input().strip())
greater = []
less = []
for i in range(n):
    a, b = input().strip().split()
    if str(a) == "G":
        greater.append(int(b))
    else:
        less.append(int(b))

greater.sort()
less.sort(reverse=True)

liars = []
half = n//2

for i in range(int(half)):
    l = less[len(less)-1-i]
    g = greater[len(greater)-1-i]
    print(l,g)
    for j in range(len(greater)):
        if l<greater[len(greater)-1-j]:
            liars.append(l)
            break

print(len(liars))
            

        






