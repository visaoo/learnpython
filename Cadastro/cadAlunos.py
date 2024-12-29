from util import solicitar_email, gen_matricula

def cad_alunos():
    aluno = input('Digite o nome do aluno que será cadastrado')
    matricula = gen_matricula(3, 5, 2, "A")  # A indica que é um ALUNO
    nascimento = input(
        'Digite a data de nascimento do aluno que será cadastrado')
    sexo = input('Digite o sexo que será cadastrado')
    endereco = input('Digite o endereco que será cadastrado')
    telefone = input('Digite o telefone que será cadastrado')
    email = solicitar_email()
    
    return {
        'nome': aluno,
        'matricula': matricula,
        'nascimento': nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email
    }