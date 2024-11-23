# calc
dic = {
    '+': 'Adicão',
    '-': 'Subtração',
    '/': 'Divisão',
    '*': 'Multiplicação',
}

def calculadora():
    expressao = input(
        'Qual tipo de calculo você deseja fazer (+, -, / ou *)  ')
    # verifico se expressao não esta no dic, se não estiver retorna;
    if expressao not in dic:
        print("Operação inválida!")
        return
    
    valor1 = int(input(f'Qual será o primeiro valor da {dic[expressao]}: '))
    valor2 = int(input(
        f'Qual será o segundo valor da {dic[expressao]} entre {valor1}{expressao}__'))
    
    expressao_completa = f'{valor1} {expressao} {valor2}'
    resultado = eval(expressao_completa)
    return resultado

r = calculadora()
if r is not None:
    print(f'Resultado final: {r}')