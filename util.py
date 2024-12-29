from random import randint
def validar_email(email):
    if "@" in email and "." in email.split("@")[1]:
        return True
    return False

def solicitar_email():
    while True:
        email = input('Qual seu email? ')
        if validar_email(email):
            print("Email válido")
            return email
        else:
            print("Email inválido. Por favor, tente novamente.")

def gen_matricula(inicial, mid, final, letter):
    matricula = ''
    for _ in range(inicial):
        matricula += str(randint(0, inicial))
    matricula += '-'
    for _ in range(mid):
        matricula += str(randint(0, mid))
    matricula += '-'
    for _ in range(final):
        matricula += str(randint(0, final))
    matricula += f'/{letter}'

    return matricula