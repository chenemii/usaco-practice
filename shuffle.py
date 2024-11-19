# https://usaco.org/index.php?page=viewproblem2&cpid=760
# make a list of size n with cow IDs at end
# list of shuffle 
# for each cow, take cow's current position and find shuffle number with that position as the value
# move cow to the position of the value in shuffle list
# do for every cow
# repeat 3 times

with open("shuffle.in") as read:
    n = int(read.readline().strip())
    shuffle = []
    shuffle = [int(i)-1 for i in read.readline().strip().split()]
    thirdcow = []
    thirdcow = [int(i) for i in read.readline().strip().split()]
   
secondcow = [0]*n
firstcow = [0]*n
beginningcow =[0]*n


for i in range(n):
    for j in range(n):
        if shuffle[j] == i:
            secondcow[j] = thirdcow[i]

for i in range(n):
    for j in range(n):
        if shuffle[j] == i:
            firstcow[j] = secondcow[i]

for i in range(n):
    for j in range(n):
        if shuffle[j] == i:
            beginningcow[j] = firstcow[i]

with open("shuffle.out", 'w') as out:
    print(beginningcow, file = out)

