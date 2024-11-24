def primosInterval(x, y):
    def is_prime(n):
        if n <= 1:
            return False # 0 e 1 não são primos
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: # se tiver resto 0, não é primo
                return False
        return True # se não tiver resto 0, é primo

    lista = []
    for i in range(x, y+1): 
        if is_prime(i): # puxa a função is_prime para verificar se é primo
            lista.append(i) # adiciona o número primo à lista
    return lista # retorna a lista de números primos


def pedirNum():
    return int(input('Informe um número: ')) # pede um número ao usuário


resultado = primosInterval(pedirNum(), pedirNum()) # 10, 50
print(f'Números primos no intervalo fornecido: {resultado}') # imprime a lista de números primos
