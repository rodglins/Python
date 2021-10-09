# #Conjuntos aritméticos:
# conjunto1 = {1, 2, 3, 4, 5}
# conjunto2 = {5, 6, 7, 8}
#
# #adicionando ao conjunto
# conjunto.add(5)
#
# #removendo do conjunto
# conjunto.discard(2)
# print(type(conjunto))
#
# #união
# conjunto_uniao = conjunto1.union(conjunto2)
# print('União: {}'.format(conjunto_uniao))
#
# #interseccão:
# conjunto_interseccao = conjunto1.intersection(conjunto2)
# print('Intersecção: {}'.format(conjunto_interseccao))
#
# #conjunto diferença:
# conjunto_diferenca1 = conjunto1.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto1)
# print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
# print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))
#
# #diferença de conjuntos:
# conjunto_diferenca1 = conjunto1.difference(conjunto2)
# conjunto_diferenca2 = conjunto2.difference(conjunto1)
# print('Conjunto diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
# print('Conjunto diferença 2 e 1: {}'.format(conjunto_diferenca2))
#
# #conjunto diferença simétrica
# conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
# print('Diferença simétrica: {}' .format(conjunto_diff_simetrica))
#
# #pertinência
# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5}
#
# #conjunto a é subconjunto de b?
# conjunto_subset = conjunto_a.issubset(conjunto_b)
# print('A pertence a B: {}' .format(conjunto_subset))
# #Resposta true
#
# #conjunto b é subconjunto de a?
# conjunto_subset = conjunto_b.issubset(conjunto_a)
# print('B pertence a A: {}' .format(conjunto_subset))
# #Resposta false
#
# #conjunto a é superconjunto de b?
# conjunto_superset = conjunto_a.issuperset(conjunto_b)
# print('A é superconjunto de B: {}' .format(conjunto_superset))
# #Resposta false
#
# #conjunto b é superconjunto de a?
# conjunto_superset = conjunto_b.issuperset(conjunto_a)
# print('B é superconjunto de A: {}' .format(conjunto_superset))
# #Resposta true

#Retirando duplicidade em lista:
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) #usa a conversão para conjunto
print(conjunto_animais)

#Convertendo lista para conjuntos para recuperar a duplicidade:
conjunto_animais = list(lista) #usa a conversão para lista
print(conjunto_animais)



