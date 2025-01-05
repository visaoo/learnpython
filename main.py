from Cadastro import aluno, disciplina, professor, turma
from Consulta.consultas import *

turmax = turma.cadastrar_turma('avc', '1234')
alunosx = turma.add_aluno(turmax, {
        'nome': 'fillype',
        'matricula': 'matricula', # gen_matricula(3, 5, 2, "A")
        'data_nascimento': 'data_nascimento',
        'sexo': 'sexo',
        'endereco': 'endereco',
        'telefone': 'telefone',
        'email': 'email' # solicitar_email()
    })

print(consultar_alunos_em_turma(turmax))
