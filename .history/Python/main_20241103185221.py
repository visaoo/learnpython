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
        
def init_giveway():
    print()

def init_game(): # type: ignore
    print('[INICIANDO GAME]...') 
    
    mode = int(input('Escolha a dificuldade 1 - EASY, 2 - MEDIUM, 3 - HARD'))
    tentativas_rest, dificuldade, cod_sorteio = definir_dificuldade(mode)
    
    tentativas = tentativas_rest
    
    while tentativas_rest > 0: # Enquanto tentativas for maior que 0 o loop continuará.
        numero_escolhido = int(input('Qual será o numéro escolhido?'))
        acertou = numero_escolhido == cod_sorteio


        if acertou:
            print(f'Parabéns {name_user}, você ganhou o sorteio!')
        elif tentativas_rest >= 1:
            tentativas_rest -= 1
            chute_alto_baixo = 'O numero é maior' if numero_escolhido > cod_sorteio else 'O numero é menor'
            print(f'Tente novamente! {tentativas_rest}/{tentativas}: ')
        else:
            print(f'Infelizmente você errou, o numero erá {cod_sorteio}')

            
    
# incia o game 
init_game()