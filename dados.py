n = int(input())

li = list(map(int,input().split()))

b = []

for i in range(len(li)):
    x = li.count(li[i])
    b.append(x)
       
        

print(b) 

