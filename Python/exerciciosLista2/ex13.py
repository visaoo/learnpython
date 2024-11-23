def maioresMedia(notas):
    tam = len(notas)
    media = sum(notas) / tam
    arr = []
    
    for x in notas:
        if x > media:
            arr.append(x)
            
    return arr, media

def pedirNota(): 
    return int(input('Informe sua nota: ')) 

notas = []

for _ in range(4): 
    notas.append(pedirNota())


arr, media = maioresMedia(notas)
print(f'Média: {media}, notas maiores que a média: {arr}')