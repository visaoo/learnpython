from random import randint

def gerar_matricula(inicial, mid, final, letter):
    matricula = ''
    for _ in range(inicial):
        matricula += str(randint(0, inicial))
    matricula += '-'
    for _ in range(mid):
        matricula += str(randint(0, mid))
    matricula += '-'
    for _ in range(final):
        matricula += str(randint(0, final))
    matricula += f'/{letter}'

    return matricula

matriculas_existentes = set()  # set não permite itens iguais

def matricula_existe(matricula):
    return matricula in matriculas_existentes

def adicionar_matricula(matricula):
    if matricula_existe(matricula):
        return False
    matriculas_existentes.add(matricula)
    return True

def gerar_matricula_unica(inicial, mid, final, letter):
    while True:
        nova_matricula = gerar_matricula(inicial, mid, final, letter)
        if adicionar_matricula(nova_matricula):
            return nova_matricula
