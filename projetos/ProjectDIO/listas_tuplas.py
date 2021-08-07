###LISTAS###

lista = [1, 3, 5, 7,]
#lista = [1, 3, 5, 7, 'gato'] #não é recomendado colocar str em lista de int
lista_animal = ['cachorro', 'gato', 'elefante']

# #ordenando as listas:
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# print(lista)
# print(type(lista))
# print(lista_animal)
# print(lista_animal[1])

# for x in lista_animal:
#     print(x)

# #percorrendo a lista de inteiros, fazendo a somatória com os numeros anteriores da lista:
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
#     print(soma)

# #somando todos os numeros da lista:
# print(sum(lista))
#
# #maior valor da lista
# print(max(lista))
# print(max(lista_animal))
#
# #menor valor da lista
# print(min(lista))
# print(min(lista_animal))

# #multiplicando uma lista
# nova_lista = lista_animal * 2
# print(nova_lista)
#
#
# #verificando se há um elemento da lista:
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('Não existe um lobo na lista')

# #verificando se há um elemento da lista:
# animal = str(input('Digite o animal que procura: '))
# if animal in lista_animal:
#     print('existe um ',animal,' na lista')
# else:
#     print('Não existe um',animal, 'na lista mas foi adicionado')
#     lista_animal.append(animal)
#     print('Lista atualizada: ', lista_animal)
#
# #Removendo o último animal da lista:
# lista_animal.pop()
# #Removendo um item específico
# #lista_animal.pop(0)


# #Apagando um animal digitado:
# print('Lista atualizada: ', lista_animal)
# animal = str(input('Digite o nome do animal a remover: '))
# if animal in lista_animal:
#     lista_animal.remove(animal)
#     print('Lista atualizada: ', lista_animal)
# else:
#     print('Não existe um',animal, 'na lista.')

####TUPLAS#########

tupla = (1, 3, 5, 7)
print(tupla)

#obtendo um item da tupla:
print(tupla[2])

#otendo o tamanho da tupla
print(len(tupla))

#convertendo de lista para tupla:
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))

#convertendo de tupla para lista:
lista_numerica = list(tupla)
print(type(lista_numerica))


