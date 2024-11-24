def calcFatRecursivo(n):
    # caso seja 0 ou 1, retorna 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * fatorial de (n-1)
    else:
        return n * calcFatRecursivo(n - 1)

# Solicita ao usuário um número
num = int(input("Digite um número para calcular o fatorial: "))

# Calcula o fatorial usando a função recursiva
resultado = calcFatRecursivo(num)

print(f"O fatorial de {num} é {resultado}")  # Exibir o resultado
