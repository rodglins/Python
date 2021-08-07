texto = "Eu amo futebol"
        #01234567890123
print(texto.find("a"))
print(texto.find("o"))
#a partir do primeiro "o" +1
print(texto[texto.find("o")+1:].find("o"))
#Tira os espaços do texto
print(texto.split(" "))