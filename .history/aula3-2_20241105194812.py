from random import randint
#TAREFA
# colocar nivel de dificuldade
#  1 -> 4 tentativas, 0-5   Facil
#  2 -> 3 tentativas, 0-7   Medio
#  3 -> 4 tentativas, 0-10  dificil

#--------------------------------
# TAREFA 2 OPCIONAL
# COLOCAR PONTUACAO NO INICIO O JOGADOR COMECA COM 1000


print("------ Jogo pra corno")
print("---------------------")

nome = input("Digite seu nome: ")
print(f"Chega aí {nome}, vamos jogar um jogo! Preciso que você escolha o nível")
nivel = int(input("Fácil-1      Médio-2     Difícil-3: "))
print("Pronto, vamos jogar!")
print("Estou pensando em um número, qual é?")

acertou = False

# Variáveis do jogo
num_tentativas = 0
dificuldade = 0

# Definição de nível e parâmetros de dificuldade
if nivel == 1:
    dificuldade = 5
    num_tentativas = 4
elif nivel == 2:
    dificuldade = 7
    num_tentativas = 3
elif nivel == 3:
    dificuldade = 10   
    num_tentativas = 4
else:
    print("desculpa Jamal esta incorreto")
    exit()

# Sorteia um número aleatório até o valor da dificuldade
sorteio = randint(0, dificuldade)

# Laço para tentativas do jogador
tentativas = 0
while num_tentativas > 0:
    chute = int(input(f"Em qual número pensei (0-{dificuldade})? ")) 
    acertou = chute == sorteio  # Compara o chute com o número sorteado

    if acertou:
        print(f"Aê, parabéns {nome}, você ganhou!")
        break
    else:
        print("Parabéns, seu jegue, você errou!")
        tentativas += 1
        print(f"Tentativa ({tentativas}/{num_tentativas}) restantes.")
        num_tentativas -= 1  # Decrementa uma tentativa

# Mensagem de fim do jogo -- exibi apenas após o fim do while
if not acertou:
    print(f"Que pena, o número que pensei foi {sorteio}.")