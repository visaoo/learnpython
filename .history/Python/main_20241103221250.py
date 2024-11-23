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
        numero_escolhido = int(input('Qual será o numéro escolhido?'))
        acertou = numero_escolhido == cod_sorteio


        if acertou:
            print(f'Parabéns {name_user}, você ganhou o sorteio!')
            pontos = points_gen(nivel, tentativas_rest)
            return pontos
        elif tentativas_rest >= 1:
            tentativas_rest -= 1
            print(cod_sorteio)
            chute_alto_baixo = 'O numero é menor' if numero_escolhido > cod_sorteio else 'O numero é maior'
            print(f'Tente novamente! {tentativas_rest}/{tentativas}: Informação adicional: {chute_alto_baixo}')
        else:
            print(f'Infelizmente você errou, o numero erá {cod_sorteio}')
            
    # resposta = input('Deseja jogar novamnete?')
    # if resposta != 'y':
    #     print('Jogo Finalizado!')
        
       

            
    
# incia o game 
init_game()