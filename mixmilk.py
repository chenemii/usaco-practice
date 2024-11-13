N = 3
capacity = [0,0,0]
milk = [0,0,0]
with open("mixmilk.in") as read:
    for i in range(N):
        capacity[i], milk[i] = map(int, read.readline().split())
for i in range(100):
    b1 = i%N
    b2=(i+1)%N
    
    amt = min(milk[b1], capacity[b2]-milk[b2])
    milk[b1]-=amt
    milk[b2]+=amt

with open("mixmilk.out","w") as out:
    for m in milk:
        print(m, file = out)
