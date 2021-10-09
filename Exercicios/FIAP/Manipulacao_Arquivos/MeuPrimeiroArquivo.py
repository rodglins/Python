"""
Criando arquivo txt:

arquivo = open("primeiro_arquivo.txt", "w")
arquivo.write("Meu primeiro arquivo!")
arquivo.close()

# Adicionando dados ao arquivo:

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\nTeste")

 """

# Listando o arquivo individualmente

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)
