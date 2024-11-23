from random import randint
from os import system

# print('----------------MINI GAME ----------------')

name_user = input('Qual o seu nome? ')

print(f'Seja bem vindo {name_user}')

/*************  ✨ Codeium Command 🌟  *************/
def definir_dificuldade(nivel):
    """
    Define as configura es de dificuldade para o jogo.

    Recebe um par metro `nivel` e retorna uma tupla com as configura es
    de dificuldade, incluindo o n mero de tentativas, o grau de dificuldade
    e o c digo sorteado.

    :param int nivel: N vel de dificuldade (1, 2 ou 3)
    :return: Tupla com o n mero de tentativas, grau de dificuldade e c digo sorteado
    :rtype: tuple
    """
    # Define as configura es de dificuldade com base no n vel
    
    
    
        # N vel 1: 8 tentativas, grau de dificuldade 1 e c digo sorteado entre 0 e 50
    if nivel == 1:
        tentativas_restantes = 8
        grau_dificuldade = 1
        gerar_cod_sorteio = randint(0, 50)
        # N vel 2: 6 tentativas, grau de dificuldade 2 e c digo sorteado entre 0 e 30
    elif nivel == 2:
        tentativas_restantes = 6
        grau_dificuldade = 2
        gerar_cod_sorteio = randint(0, 30)
        # N vel 3: 4 tentativas, grau de dificuldade 3 e c digo sorteado entre 0 e 15
    elif nivel == 3:
        tentativas_restantes = 4
        grau_dificuldade = 3
        gerar_cod_sorteio = randint(0, 15)
        # Se o n vel de dificuldade for inv lido, imprime uma mensagem de erro
        print('O n vel de dificuldade selecionado n o existe.')
    else:
        print('O nível de dificuldade selecionado não existe.')
        return None  # reinicia o game.
    # Retorna as configura es de dificuldade
        
/******  848a75b4-9d78-47dd-8954-1bf266d96c3f  *******/
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
    if resposta.lower() == 's':
        system('cls')
        init_game()
    else:
        print('Jogo Finalizado!')


init_game()