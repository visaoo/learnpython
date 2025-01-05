def filtrar_professores_por_disciplina(professores, disciplina_nome):
    return [professor for professor in professores if professor['disciplina'] == disciplina_nome]

def consultar_alunos_em_turma(turma): # puxa todos os alunos de x turma
    return turma['alunos']

def consultar_professores_por_disciplina(disciplinas):
    return {disciplina['nome']: disciplina['professor'] for disciplina in disciplinas}

def consultar_disciplinas_em_turma(turma):
    return turma['disciplinas']

def consultar_turmas_por_aluno(aluno, turmas):
    return [turma for turma in turmas if aluno in turma['alunos']]

def consultar_turmas_por_professor(professor, turmas):
    return [turma for turma in turmas if turma['professor'] == professor]
