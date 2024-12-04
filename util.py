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
