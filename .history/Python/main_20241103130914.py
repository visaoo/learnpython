name = 'visao'
age = 18
number = '(67) 00111-0101'
country = 'brazil'

print(f'Usuário {name.capitalize()} tem {age} anos. Numero {number} do {country}')

status = 'Jovem' if age < 18 else 'Adulto jovem' if 18 <= age < 30 else 'Adulto' if 30 <= age < 60 else 'Idoso'
print(status)  # Saída: Adulto jovem