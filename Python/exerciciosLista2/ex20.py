def seq_fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

num = int(input("Quantos números da sequência de Fibonacci deseja gerar? "))
resultado = seq_fibonacci(num)
print(f"Sequência de Fibonacci com {num} números: {resultado}")
