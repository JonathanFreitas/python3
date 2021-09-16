# Deep copy
print('Exemplo de DEEP COPY')
lista = [ 1, 2, 3 ]

nova = lista.copy()

nova.append(4)

print(lista)
print(nova)

# COPY
print('Exemplo de COPY')

lista2 = [ 3, 2, 1 ]

nova2 = lista2

nova2.append(0)

print(lista2)
print(nova2)
