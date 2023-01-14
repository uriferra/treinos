


entrada = list(map(float, input().split()))
valor = float(input())

cont = -1
cont2 = 1

valorentrada = entrada[cont] 
expoente = len(entrada) - cont2

    

if expoente > 1:
    for i in range(expoente > 1):
        x1 = valorentrada * valor ** expoente
        cont -= 1
        cont2 -= 1

valorentrada = entrada[cont] 

for j in range(1):
    x2 = valorentrada * valor
    cont -= 1
    
valorentrada = entrada[cont] 

res = x1 + x2 + valorentrada
print("%3.4f"% res)