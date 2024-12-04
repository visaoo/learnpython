from random import randint
from util import solicitar_email

# base 
alunos = [
    {
        "nome": 'Bruno', "matricula": "999-67890-20/A",
        "about": {
            "nascimento": "",
            "sexo": "Masculino",
            "endereco": "",
            "telefone": "",
            "email": "@gmail",
        }
    }
]

professores = [
    {
        "nome": 'Leticia', "matricula": "12345-123-12/P", "disciplina": [],
        "about": {
                "nascimento": "",
                "sexo": "Masculino",
                "endereco": "",
                "telefone": "",
                "email": "@gmail",  # colocar uma verificação se é ou não email
        }
    }
]


def gen_matricula(inicial, mid, final, letter):
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


def cad_alunos():
    aluno = input('Digite o nome do aluno que será cadastrado')
    matricula = gen_matricula(3, 5, 2, "A")  # A indica que é um ALUNO
    nascimento = input(
        'Digite a data de nascimento do aluno que será cadastrado')
    sexo = input('Digite o sexo que será cadastrado')
    endereco = input('Digite o endereco que será cadastrado')
    telefone = input('Digite o telefone que será cadastrado')
    email = solicitar_email()


cad_alunos()
