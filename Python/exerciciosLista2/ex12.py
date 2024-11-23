def primosInterval(x, y):
    lista = []
    for i in range(x, y+1):
        print(i)
        if i % 2 == 0:
            lista.append(i)
            print(i)
    return lista
            
x = primosInterval(10, 50)
print(x)
