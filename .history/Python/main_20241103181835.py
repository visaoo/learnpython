# print('----------------MINI GAME ----------------')

name_user = input('Qual o seu nome? ')

print(f'Seja bem vindo {name_user}')

def dificuldade(mode):
    if mode == 1:
        tentativa = 8
        dificuldade = 1
    elif mode == 2:
        tentativa = 6
        dificuldade = 2
    elif mode == 3:
        tentativa = 4 
        dificuldade = 3
    else:
        print('A dificuldade selecionada não existe.')
        return None # reinicia o game.
        
    return tentativa, dificuldade
        
def init_giveway():
    print()

def init_game(): # type: ignore
    print('[INICIANDO GAME]...') 
    
    mode = int(input('Escolha a dificuldade 1 - EASY, 2 - MEDIUM, 3 - HARD'))
    dificult = dificuldade(mode)


# incia o game 
init_game()