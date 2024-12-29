from util import solicitar_email, gen_matricula

def cad_professor():
    professor = input('Digite o nome do professor que será cadastrado: ')
    matricula = gen_matricula(3, 5, 2, "P")  # P indica que é um professor
    nascimento = input('Digite a data de nascimento do professor que será cadastrado: ')
    sexo = input('Digite o sexo que será cadastrado: ')
    endereco = input('Digite o endereço que será cadastrado: ')
    telefone = input('Digite o telefone que será cadastrado: ')
    disciplina = input('Digite a disciplina que será cadastrada: ')
    email = solicitar_email()

    return {
        'nome': professor,
        'matricula': matricula,
        'nascimento': nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'disciplina': disciplina,
        'email': email
    }
