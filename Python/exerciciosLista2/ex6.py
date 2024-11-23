def mediaAritmetica(notas):
    return sum(notas)/len(notas)

r1 = int(input('Informe sua primeira nota.'))
r2 = int(input('Informe sua segunda nota.'))
r3 = int(input('Informe sua terceira nota.'))

x = (r1,r2,r3)
print(mediaAritmetica(x))
