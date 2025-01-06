def cadastrar_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email):
    return {
        'nome': nome,
        'matricula': matricula, # gerar_matricula_unica(3, 5, 2, "A")
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email # solicitar_email()
    }