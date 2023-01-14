def func(matrix, n):
    for i in range(n):
        temp = matrix[i]
        del matrix[i]
        res2 = []
        for j in range(len(matrix)):
            temp2 = matrix[j]
            res = ((temp2[0] - temp[0])**2  + (temp2[1] - temp[1])**2  + (temp2[2] - temp[2])**2)
            raiz = res ** 0.5
            res2.append(raiz)
        menor = res2[0]
        for l in range(1, len(res2)):
            if menor > res2[l]:
                menor = res2[l]
        if menor <= 20:
            print("Alta")
        elif menor > 20 and menor <= 50:
            print("Media")
        else:
            print("Baixa")
        matrix.insert(i, temp)
def main():
    n = int(input())
    matrix = []
    for i in range(n):
        var = list(map(int, input().split()))
        matrix.append(var)
    func(matrix, n)
main()