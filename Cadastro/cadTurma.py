def cadastrar_turma(turmas):
    nome = input('Nome da turma: ')
    codigo = input('Codiguin: ')
    disciplinas = input(
        'Disciplinas (códigos separados por vírgula): ').split(',')
    professor = input('Professor (Codiguin): ')
    
    return {
        'nome': nome,
        'codigo': codigo,
        'disciplinas': disciplinas,
        'professor': professor,
        'alunos': []
    }