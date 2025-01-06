def cadastrar_professor(nome, codigo, data_nascimento, sexo, endereco, telefone, email, disciplina):
    return {
        'nome': nome,
        'codigo': codigo, # gerar_matricula_unica(3, 5, 2, "P")
        'data_nascimento': data_nascimento,
        'sexo': sexo,
        'endereco': endereco,
        'telefone': telefone,
        'email': email,
        'disciplina': disciplina # solicitar_email()
    }