from util import solicitar_email, gen_matricula

def cadastrar_disciplina(nome, codigo, carga_horaria, professor):
    return {
        'nome': nome,
        'codigo': codigo, # gen_matricula(3, 5, 2, "D")
        'carga_horaria': carga_horaria,
        'professor': professor
    }
