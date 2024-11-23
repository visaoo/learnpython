def verificaIdade(i):
    return 'Menor de idade' if i < 18 else 'Maior de idade'
    
i = int(input('Informe sua idade: '))

print(verificaIdade(i))