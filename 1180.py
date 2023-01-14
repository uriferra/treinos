
def func(li: list):
    menorvalor = li[0]
    posicao = 0

    for i in range(1, len(li)):
        if li[i] < menorvalor:
            menorvalor = li[i]
            posicao = i
   
    print(f"Menor valor: {menorvalor}")
    print(f"Posicao: {posicao}")

def main():
    n = int(input())

    li = list(map(int,input().split()))

    func(li)

main()