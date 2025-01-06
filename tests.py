# def gerar_dados_teste():
#     # Adicionar alunos
#     for i in range(12):
#         nome = f'Aluno {i+1}'
#         matricula = gerar_matricula_unica(3, 5, 2, 'A')
#         data_nascimento = f'01/01/200{i+1}'
#         sexo = 'M' if i % 2 == 0 else 'F'
#         endereco = f'Rua {i+1}'
#         telefone = f'12345{i+1}'
#         email = f'aluno{i+1}@teste.com'
#         novo_aluno = Alunos.cadastrar_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
#         alunos.append(novo_aluno)
    
#     # Adicionar professores
#     for i in range(12):
#         nome = f'Professor {i+1}'
#         codigo = gerar_matricula_unica(2, 5, 3, 'P')
#         data_nascimento = f'10/10/197{i+1}'
#         sexo = 'M' if i % 2 == 0 else 'F'
#         endereco = f'Avenida {i+1}'
#         telefone = f'54321{i+1}'
#         email = f'professor{i+1}@teste.com'
#         disciplina_professor = f'Disciplina {i+1}'
#         novo_professor = Professores.cadastrar_professor(nome, codigo, data_nascimento, sexo, endereco, telefone, email, disciplina_professor)
#         professores.append(novo_professor)

#     # Adicionar disciplinas
#     for i in range(12):
#         nome = f'Disciplina {i+1}'
#         codigo = gerar_matricula_unica(2, 5, 3, 'D')
#         carga_horaria = (i + 1) * 20
#         professor = professores[i]
#         nova_disciplina = Disciplinas.cadastrar_disciplina(nome, codigo, carga_horaria, professor)
#         disciplinas.append(nova_disciplina)

#     # Adicionar turmas
#     for i in range(12):
#         nome = f'Turma {i+1}'
#         codigo = gerar_matricula_unica(2, 5, 3, 'T')
#         nova_turma = Turmas.cadastrar_turma(nome, codigo)
#         turmas.append(nova_turma)

#     # Matricular alunos nas turmas
#     for turma in turmas:
#         for aluno in alunos:
#             Turmas.add_aluno(turma, aluno)

#     # Alocar disciplinas nas turmas
#     for turma in turmas:
#         for disciplina in disciplinas:
#             Turmas.add_disciplina(turma, disciplina)