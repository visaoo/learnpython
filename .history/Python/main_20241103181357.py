# print('----------------MINI GAME ----------------')

name_user = input('Qual o seu nome? ')

print(f'Seja bem vindo {name_user}')

def dificuldade(mode):
    if mode == 1:
        tentativa = 5
        dificuldade = 1
    elif mode == 2:
        tentativa = 4
        dificuldade = 2
    elif mode == 3:
        tentativa = 3
        dificuldade = 3
    else:
        print('A dificuldade selecionada não existe.')
        init_game() # reinicia o game.
        
def init_giveway():
    print()

def init_game(): # type: ignore
    print('[INICIANDO GAME]...') 
    
    
    
    dificult = dificuldade(mode):


# incia o game 
initGame()