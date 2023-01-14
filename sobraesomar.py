u = list(map(int, input().split()))
v = list(map(int, input().split()))


u.reverse()
v.reverse()

var = []
sobra = 0
count = 0
for i in range(len(u)):
    res = u[i] + v[i] + sobra
    count += 1
    while res > 9:
        sobra = res % 10
        res = res // 10
        
        if count == len(u):
            var.append(res)
        
        
        
    var.append(res)
        
var.reverse()

print(*var)
        






    

    
    
