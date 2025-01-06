def cadastrar_turma(nome, codigo):
    return {
        'nome': nome,
        'codigo': codigo,
        'disciplinas': [],
        'professor': None,
        'alunos': []
    }

def add_disciplina(turma, disciplina): # base disciplina cad/dis
    turma['disciplinas'].append(disciplina)

def add_professor(turma, professor):  # base professor cad/pro
    turma['professor'] = professor

def add_aluno(turma, aluno): # base aluno cad/aluno
    turma['alunos'].append(aluno)

def remove_aluno(turma, aluno): # base aluno cad/aluno ---- aluno[0]['matricula']
    turma['alunos'].remove(aluno) # não implementado; 
    
    
    