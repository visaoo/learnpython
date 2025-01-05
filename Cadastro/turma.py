def cadastrar_turma(nome, codigo):
    return {
        'nome': nome,
        'codigo': codigo,
        'disciplinas': [],
        'professor': None,
        'alunos': []
    }

def add_disciplina(turma, disciplina):
    turma['disciplinas'].append(disciplina)

def add_professor(turma, professor):
    turma['professor'] = professor

def add_aluno(turma, aluno):
    turma['alunos'].append(aluno)

def remove_aluno(turma, aluno):
    turma['alunos'].remove(aluno) # não implementado;