from random import randint

# print('----------------MINI GAME ----------------')

name_user = input('Qual o seu nome? ')

print(f'Seja bem vindo {name_user}')

def definir_dificuldade(nivel):
    
    
    if nivel == 1:
        tentativas_restantes = 8
        grau_dificuldade = 1
        gerar_cod_sorteio = randint(0, 30)
    elif nivel == 2:
        tentativas_restantes = 6
        grau_dificuldade = 2
        gerar_cod_sorteio = randint(0, 30)
    elif nivel == 3:
        tentativas_restantes = 4
        grau_dificuldade = 3
        gerar_cod_sorteio = randint(0, 30)
    else:
        print('O nível de dificuldade selecionado não existe.')
        return None  # reinicia o game.
        
    return tentativas_restantes, grau_dificuldade, gerar_cod_sorteio
        
def points_gen(nivel, tentativas):
    pontos = pontos = 0 if tentativas <= 0 else 100 - (tentativas * 5) - (nivel * 10)
    return pontos

def init_game(): # type: ignore
    print('[INICIANDO GAME]...') 
    
    nivel = int(input('Escolha a dificuldade 1 - EASY, 2 - MEDIUM, 3 - HARD'))
    tentativas_rest, dificuldade, cod_sorteio = definir_dificuldade(nivel)
    # tentativas é a quantidade total de tentativas_rest
    tentativas = tentativas_rest
    
    while tentativas_rest > 0: # Enquanto tentativas for maior que 0 o loop continuará.
        numero_escolhido = int(input('Qual será o número escolhido? '))
        acertou = numero_escolhido == cod_sorteio

        if acertou:
            pontos = points_gen(nivel, tentativas_rest)
            print(f'Parabéns {name_user}, você ganhou o sorteio! Você recebeu {pontos} pontos.')
            break
        else:
            tentativas_rest -= 1
            dicas_chutes = 'O número é menor' if numero_escolhido > cod_sorteio else 'O número é maior'
            print(f'Tente novamente! {tentativas_rest}/{tentativas}: Informação adicional: {dicas_chutes}')
        
        if tentativas_rest == 0:
            print(f'Você perdeu! O número era {cod_sorteio}.')
    
    resposta = input('Deseja jogar novamente? (s/n): ')
    if resposta.lower() != 's':
        print('Jogo Finalizado!')
    init_game()