basedados = []

#importando dados e limpando:

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))

#base completa em forma de lista:
print(basedados)
#obtendo o primeiro item da linha 0:
print(basedados[0][0])
#Somanda valores numéricos da lista pela ordem:
print(float(basedados[0][0]) + float(basedados[0][1]))
