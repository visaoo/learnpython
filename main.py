from Cadastro import Alunos, Disciplinas, Professores, Turmas
from Consulta.consultas import *
from Utils.matricula import gerar_matricula_unica
from Test.gerar_all import gerar_tudo
import os

# "banco de dados" globais
alunos = []
professores = []
disciplinas = []
turmas = []

def menu():
    os.system('cls')
    while True:
        input("\nPressione Enter para continuar...")

        print("\nMenu:")
        print("1. Matricular Aluno em Turma")
        print("2. Alocar Professor em Disciplina")
        print("3. Alocar Disciplina em Turma")
        print("4. Filtrar Professores por Disciplina")
        print("5. Consultar Alunos em Turma")
        print("6. Consultar Professores por Disciplina")
        print("7. Consultar Disciplinas em Turma")
        print("8. Cadastrar Aluno")
        print("9. Cadastrar Professor")
        print("10. Cadastrar Turma")
        print("11. Ver Todos os Alunos")
        print("12. Ver Todos os Professores")
        print("13. Ver Todas as Disciplinas")
        print("14. Ver Todas as Turmas")
        print("15. Sair")
        
        opcao = input("Escolha uma opção: ")
        os.system('cls')
        
        if opcao == '1':
            matricula_aluno = input("Digite a matrícula do aluno: ")
            codigo_turma = input("Digite o código da turma: ")
            aluno = encontrar_aluno(matricula_aluno, alunos)
            turma = encontrar_turma(codigo_turma, turmas)
            if aluno and turma:
                Turmas.add_aluno(turma, aluno)
                print(f'Aluno {aluno["nome"]} matriculado na turma {turma["nome"]}')
            else:
                print("Aluno ou turma não encontrados.")
        elif opcao == '2':
            codigo_professor = input("Digite o código do professor: ")
            codigo_disciplina = input("Digite o código da disciplina: ")
            professor = encontrar_professor(codigo_professor, professores)
            disciplina = encontrar_disciplina(codigo_disciplina, disciplinas)
            if professor and disciplina:
                disciplina['professor'] = professor
                print(f'Professor {professor["nome"]} alocado na disciplina {disciplina["nome"]}')
            else:
                print("Professor ou disciplina não encontrados.")
        elif opcao == '3':
            codigo_turma = input("Digite o código da turma: ")
            codigo_disciplina = input("Digite o código da disciplina: ")
            turma = encontrar_turma(codigo_turma, turmas)
            disciplina = encontrar_disciplina(codigo_disciplina, disciplinas)
            if turma and disciplina:
                Turmas.add_disciplina(turma, disciplina)
                print(f'Disciplina {disciplina["nome"]} alocada na turma {turma["nome"]}')
            else:
                print("Turma ou disciplina não encontrados.")
        elif opcao == '4':
            disciplina_nome = input("Digite o nome da disciplina: ")
            resultado = filtrar_professores_por_disciplina(professores, disciplina_nome)
            print(f'Professores de {disciplina_nome}: {resultado}')
        elif opcao == '5':
            codigo_turma = input("Digite o código da turma: ")
            turma = encontrar_turma(codigo_turma, turmas)
            if turma:
                resultado = consultar_alunos_em_turma(turma)
                print(f'Alunos na {turma["nome"]}: {resultado}')
            else:
                print("Turma não encontrada.")
        elif opcao == '6':
            resultado = consultar_professores_por_disciplina(disciplinas)
            print(f'Disciplinas e seus professores: {resultado}')
        elif opcao == '7':
            codigo_turma = input("Digite o código da turma: ")
            turma = encontrar_turma(codigo_turma, turmas)
            if turma:
                resultado = consultar_disciplinas_em_turma(turma)
                print(f'Disciplinas na {turma["nome"]}: {resultado}')
            else:
                print("Turma não encontrada.")
        elif opcao == '8':
            nome = input("Digite o nome do aluno: ")
            matricula = gerar_matricula_unica(3, 5, 2, 'A')
            data_nascimento = input("Digite a data de nascimento do aluno: ")
            sexo = input("Digite o sexo do aluno: ")
            endereco = input("Digite o endereço do aluno: ")
            telefone = input("Digite o telefone do aluno: ")
            email = input("Digite o e-mail do aluno: ")
            novo_aluno = Alunos.cadastrar_aluno(nome, matricula, data_nascimento, sexo, endereco, telefone, email)
            alunos.append(novo_aluno)
            print(f'Aluno {nome} cadastrado com sucesso.')
        elif opcao == '9':
            nome = input("Digite o nome do professor: ")
            codigo = gerar_matricula_unica(2, 5, 3, 'P')
            data_nascimento = input("Digite a data de nascimento do professor: ")
            sexo = input("Digite o sexo do professor: ")
            endereco = input("Digite o endereço do professor: ")
            telefone = input("Digite o telefone do professor: ")
            email = input("Digite o e-mail do professor: ")
            disciplina_professor = input("Digite a disciplina do professor: ")
            novo_professor = Professores.cadastrar_professor(nome, codigo, data_nascimento, sexo, endereco, telefone, email, disciplina_professor)
            professores.append(novo_professor)
            print(f'Professor {nome} cadastrado com sucesso.')
        elif opcao == '10':
            nome = input("Digite o nome da turma: ")
            codigo = gerar_matricula_unica(3, 5, 3, 'T')
            nova_turma = Turmas.cadastrar_turma(nome, codigo)
            turmas.append(nova_turma)
            print(f'Turma {nome} cadastrada com sucesso.')
        elif opcao == '11':
            ver_todos_alunos(alunos)
        elif opcao == '12':
            ver_todos_professores(professores)
        elif opcao == '13':
            ver_todas_disciplinas(disciplinas)
        elif opcao == '14':
            ver_todas_turmas(turmas)
        elif opcao == '15':
            print("Saindo...")
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    # Exemplos
    gerar_tudo(alunos, professores, disciplinas, turmas)
    # gerar_dados_teste()
    menu()
