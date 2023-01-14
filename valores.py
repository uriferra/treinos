def func(produtos, matrix, peso):

    temp1 = 0
    temp2 = 0





    res = 0

    ma = []
    me = []
    for j in range(produtos):
        temp = matrix[temp1][temp2]
        for i in range(produtos):
            if temp != matrix[0][i]:
                res = temp + matrix[0][i]
                ma.append(res)
        temp2 += 1   

    temp1 = 1
    temp2 = 0    

    for j in range(produtos):
        temp = matrix[temp1][temp2]
        for i in range(produtos):
            if temp != matrix[1][i]:
                res = temp + matrix[1][i]
                me.append(res)
        temp2 += 1   

    maior = 0


    for i in range(len(ma)):
        if ma[i] > maior and me[i] <=peso:
            maior = ma[i]

    print(maior)

def main():
    produtos = int(input())
    matrix = []
    for i in range(2):
        var = list(map(int, input().split()))
        matrix.append(var)

    peso = int(input())
    func(produtos, matrix, peso)

main()