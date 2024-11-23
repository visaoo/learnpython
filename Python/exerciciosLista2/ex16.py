def calcFat(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

num = int(input("Digite um número para calcular o fatorial: "))
resultado = calcFat(num)
print(f"O fatorial de {num} é {resultado}")