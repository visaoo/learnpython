from util import solicitar_email, gen_matricula

def cadastrar_professor(nome, codigo, data_nascimento, sexo, endereco, telefone, email, disciplina):
    return {
        'nome': nome,
        'codigo': codigo, # gen_matricula(3, 5, 2, "P")
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        'disciplina': disciplina # solicitar_email()
    }