'''
    Como criar uma listas
    Manipular listas
    Realizar operações com listas
    O que é uma tuplas
    Como interagir com tuplas
    Conversões lista em tuplas e vice versa
'''
#lista pode ter numero e string, mas não é uma boa prática [1, 'gato', 3]
lista = [1, 3, 5, 7]
lista_animal = ['cachorro' , 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla)) # traz quantos elementos tem na tupla
print(len(lista)) # tras quantos elemento tem na lista

# converte lista em tupla
tupla_animal = tuple(lista_animal)
print(tupla_animal)

# converter tupla em lista
lista_numerica = list(tupla)
print(lista_numerica)



# na lista você pode alterar objetos, utiliza colchetes '[]'
# na tupla não pode alterar objeto, utiliza parentese '()'

# nova_lista = lista_animal * 3
# print(nova_lista)

# ordenar lista
#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)

# inverte a lista
#lista_animal.reverse()
#print(lista_animal)

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Não exist lobo na lista')
#     lista_animal.append('lobo') # inclui dentro de lista_animal
# print(lista_animal)

# lista_animal.pop(2) # tira o terceiro da lista que será o elefante
# lista_animal.pop() # tira o ultimo da lista

# lista_animal.remove('elefante') # utilizado quando eu sei qual objeto irei tirar
# print(lista_animal)

# print(sum(lista)) # traz a soma de todos os objetos de lista
# print(max(lista)) # traz o maior numero de todos os objetos de lista
# print(min(lista)) # traz o menor numero de todos os objetos de lista
# print(sum(lista_animal)) # traz o ultimo em ordem alfabetica de todos os objetos de lista
# soma = 0
# for x in lista:
#     print(x) # traz a lista
#     soma += x # traz a soma de todos os objetos de lista
# print(soma)

# print(lista_animal[1]) # irá trazer o animal na posição 1

#for x in lista_animal:# Tráz a lista_animal
#    print(x)