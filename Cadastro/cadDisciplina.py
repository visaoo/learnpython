from util import solicitar_email, gen_matricula

def cad_disciplina():
    disciplina = input('Digite o nome da disciplina que será cadastrada: ')
    codigo = input('Codiguin: ')
    cargaHoraria = int(input('Digite a carga horaria total de disciplina: '))
    professor = input('Digite o nome do professor que será inserido na disciplina: ')

    return {
        'disciplina': disciplina,
        'codigo': codigo,
        'carga_total': cargaHoraria,
        'professor': professor
    }
