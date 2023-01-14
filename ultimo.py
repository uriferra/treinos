m,n = map(int, input().split())
matrix = []
for i in range(m):
    var = list(map(int, input().split()))
    matrix.append(var)

valor = 1
valor2 = n + -2
valor3 = n + -1
for j in range(m):
    for i in range(n):
        if matrix[j][i] == 1:
            matrix[j][i] = 9
# esquerda para a direita
for j in range(m):
    for i in range(n -1):
        if matrix[j][valor] == 9 and matrix[j][i] < 9:
            matrix[j][i] += 1
        valor += 1
    valor = 1
valor = 1
# direita para a esquerda
for j in range(m):
    for i in range(n -1, 0, -1):
        if matrix[j][valor2] == 9 and matrix[j][valor3] < 9:
            matrix[j][valor3] += 1
        valor2 += -1
        valor3 += -1
    valor2 = n + -2
    valor3 = n + -1
# baixo para cima
for j in range(n): #coluna
    for i in range(m -1):  #linha
        if matrix[i + 1][j] == 9 and matrix[i][j] < 9:
            matrix[i][j] += 1

# cima para baixo
for j in range(n): #coluna
    for i in range(m -1):  #linha
        if matrix[i][j] == 9 and matrix[i + 1][j] < 9:
            matrix[i + 1][j] += 1

for i in range(m):
        for j in range(n):       
            print(f"{matrix[i][j]}", end="\n")
        print()


