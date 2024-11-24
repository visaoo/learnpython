def par_or_impar(v): # função que verifica se o número é par ou impar
    if v % 2 == 0:
        return f'{v} é Par'
    else:
        return f'{v} é Impar'
    
r = int(input('Informe um número e descubra se é par ou impar.') )
print(par_or_impar(r))