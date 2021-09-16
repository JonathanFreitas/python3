# Exemplo buscar elemento

num = [ 1, 2, 3, 4, 5, 3, 2, 1, 3]

# For com enumerate

for indice, valor in enumerate(num):
    print('Posição: %d valor: %d' %(indice, valor))


# Busca o indice do elemento
print('indice: %d do valor 5' %(num.index(5)))

print('indice: %d do valor 3 entre 4 ate 8' %(num.index(3,4,8)))

# Revisão do Slicing
# list[inicio:fim:passo]
# range[inicio:fim:passo] 
print('######## SLICING ############')
print(num[1:])
print(num[1:7])
print(num[1:7:2])
print(num[:8:2])

# Reverse values
nome = ['jonathan', 'freitas']

nome[0], nome[1] = nome[1], nome[0]

print(nome)

nome.reverse()

print(nome)

# Soma, Maximo, Minimo, Tamanho da lista

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(lista2))
print(max(lista2))
print(min(lista2))
print(len(lista2))
