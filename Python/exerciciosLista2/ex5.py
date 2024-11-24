def gerar_tabuada():
    tabuada = int(input('Informe o número da tabuada: ')) # input da tabuada a ser gerada
    for i in range(1, 11): # 1-10 
        print(f'{tabuada} x {i} = {tabuada * i}')

gerar_tabuada()
