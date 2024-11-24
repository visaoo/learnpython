# palíndromos test: reviver, radar, arara, ana, ada, aia, oto, ala
def is_palin(palavra, palavra_invertida):
    return 'é um palíndromo' if palavra == palavra_invertida else 'não é um palíndromo'

palavra = input('Qual será a palavra?').lower() # input da palavra
palavra_invertida = palavra[::-1]  #[ini:mid:end]

r = is_palin(palavra, palavra_invertida)

print(f'Palavra: {palavra} {r}')
