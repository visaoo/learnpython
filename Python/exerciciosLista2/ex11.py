def palavrasUnicas(frase):
    return set(frase)
    
i = input('Informe uma frase.')
tam = len(palavrasUnicas(i.split()))
print(tam)