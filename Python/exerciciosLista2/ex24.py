def verificar_anagrama(palavra1, palavra2):
    # remove os espaços e transforma tudo em minúsculo
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    tam1 = len(palavra1)  # tamanho da palavra1
    tam2 = len(palavra2)  # tamanho da palavra2

    if tam1 != tam2:  # se não tiver o mesmo tamanho, não é anagrama
        return 'Não é anagrama'

    for char in palavra1:  # loop para verificar se todos os caracteres da primeira palavra estão na segunda palavra
        if char not in palavra2:
            return 'Não é anagrama'

    return 'É anagrama'  # se passar por todos os testes, é anagrama


print(verificar_anagrama('aorma', 'amora'))
