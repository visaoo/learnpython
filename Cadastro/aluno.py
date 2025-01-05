from util import solicitar_email, gen_matricula

def cadastrar_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email):
    return {
        'nome': nome,
        'matricula': matricula, # gen_matricula(3, 5, 2, "A")
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email # solicitar_email()
    }