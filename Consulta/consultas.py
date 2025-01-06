def filtrar_professores_por_disciplina(professores, disciplina_nome):
    return [f'Nome: {professor["nome"]}, Código: {professor["codigo"]}' for professor in professores if professor['disciplina'] == disciplina_nome]

def consultar_alunos_em_turma(turma):
    return [f'Nome: {aluno["nome"]}, Matrícula: {aluno["matricula"]}' for aluno in turma['alunos']]

def consultar_professores_por_disciplina(disciplinas):
    return {disciplina['nome']: f'Nome: {disciplina["professor"]["nome"]}, Código: {disciplina["professor"]["codigo"]}' for disciplina in disciplinas if disciplina["professor"]}

def consultar_disciplinas_em_turma(turma):
    return [f'Nome: {disciplina["nome"]}, Código: {disciplina["codigo"]}' for disciplina in turma['disciplinas']]

def consultar_turmas_por_aluno(aluno, turmas):
    return [turma for turma in turmas if aluno in turma['alunos']]

def consultar_turmas_por_professor(professor, turmas):
    return [turma for turma in turmas if turma['professor'] == professor]


# pesquisas

def encontrar_aluno(matricula, alunos):
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None

def encontrar_professor(codigo, professores):
    for professor in professores:
        if professor['codigo'] == codigo:
            return professor
    return None

def encontrar_disciplina(codigo, disciplinas):
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            return disciplina
    return None

def encontrar_turma(codigo, turmas):
    for turma in turmas:
        if turma['codigo'] == codigo:
            return turma
    return None

# listagem

def ver_todos_alunos(alunos):
    for aluno in alunos:
        print(f'Nome: {aluno["nome"]}, Matrícula: {aluno["matricula"]}, Data de Nascimento: {aluno["data_nascimento"]}, Sexo: {aluno["sexo"]}, Endereço: {aluno["endereco"]}, Telefone: {aluno["telefone"]}, E-mail: {aluno["email"]}')

def ver_todos_professores(professores):
    for professor in professores:
        print(f'Nome: {professor["nome"]}, Código: {professor["codigo"]}, Data de Nascimento: {professor["data_nascimento"]}, Sexo: {professor["sexo"]}, Endereço: {professor["endereco"]}, Telefone: {professor["telefone"]}, E-mail: {professor["email"]}, Disciplina: {professor["disciplina"]}')

def ver_todas_disciplinas(disciplinas):
    for disciplina in disciplinas:
        print(f'Nome: {disciplina["nome"]}, Código: {disciplina["codigo"]}, Carga Horária: {disciplina["carga_horaria"]}, Professor: {disciplina["professor"]["nome"] if disciplina["professor"] else "Não alocado"}')

def ver_todas_turmas(turmas):
    for turma in turmas:
        print(f'Nome: {turma["nome"]}, Código: {turma["codigo"]}')