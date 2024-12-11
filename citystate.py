# https://usaco.org/index.php?page=viewproblem2&cpid=667#
# 7:55 - 8
# 8- 8:05 - too slow

'''
take first 2 of every city
go thru every state and find pair
    if pair found, then go back and check if first 2 of state = first 2 of 2nd city
'''
n = int(input().strip())
count = 0
seen = {}

# Use dict to keep track of instances of combinations, when reverse combination is found add to count
for i in range(n):
    city, state = input().strip().split()
    city_prefix = city[:2]
    
    # Only process if city prefix isn't same as its state
    if city_prefix != state:
        # Check if there's a matching pair
        if (state + city_prefix) in seen:
            count += seen[state + city_prefix]
            
        # Add current pair to seen
        curr = seen.get(city_prefix + state, 0)
        new = curr + 1
        seen[city_prefix + state] = new

print(count)

'''
too slow
n = int(input().strip())
cities = []
states = []
for i in range(n):
    a, b = [str(x) for x in input().strip().split()]
    cities.append(str(a))
    states.append(str(b))

count = 0
for i in range(n):
    stringy = cities[i][0:2]
    for j in range(n):
        if states[j] == stringy and states[i] == cities[j][0:2] and states[j]!=states[i]:
            count+=0.5
print(int(count))
'''
