from random import randint
matriz = [[randint(0, 10) for _ in range(3)], [randint(11, 20) for _ in range(3)], [randint(21, 30) for _ in range(3)]]

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


def soma_diagonais(matriz):
    n = len(matriz)
    print(matriz)
    # print(matriz[0][n-0-1])
    # print(matriz[1][n-1-1])
    # print(matriz[2][n-2-1])

    soma_principal = 0
    soma_secundaria = 0

    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n-i-1]

    return soma_principal, soma_secundaria


soma_principal, soma_secundaria = soma_diagonais(matriz)

print(
    f'A soma da diagonal principal é: {soma_principal} e a soma da diagonal secundária é: {soma_secundaria}')
