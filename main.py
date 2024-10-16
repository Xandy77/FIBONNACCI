# função para calcular Fibonacci
def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n - 2)
    
#programa principal
if __name__=='__main__':
    n = int(input('Informe o numero de sequencias fibonacci: '))

    # exibe a sequencia
    for x in range(n):
        print(calcular_fibonacci(x))