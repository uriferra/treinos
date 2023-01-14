

    
def main():
    abobora = [1,2,3,4,5,6,7,8,9,10]
    vector(abobora)

def vector(y):
    for i in range (len(y)):
        y[i] = int(input())
        if y[i] <= 0:
            y[i] = 1
            
        print (f"X[{i}] = {y[i]}")


main()
    