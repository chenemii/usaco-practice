# https://usaco.org/index.php?page=viewproblem2&cpid=664
# loop through all letters
    # loop through all words
    # if front word has letter, add to count
    # if back word has letter, add to count
    # if front word and back word has letter, do not add to count

n = int(input().strip())
front = []
back = []
for i in range(n):
    a, b = input().strip().split()
    front.append(a)
    back.append(b)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
count = [0]*26
freq1 = 0
freq2 = 0
for i in range(26): # each letter
    for j in range(n): # each word
        for k in front[j]: # each letter inside front word
            if k == letters[i]:
                freq1+=1
        for l in back[j]: #each letter inside back word
            if l == letters[i]:
                freq2+=1
        count[i]+=max(freq1,freq2)
        freq1=0
        freq2=0
        
print(count)


