# módulo para copiar e mover:
import shutil

# Criando uma função:
def escrever_arquivo(texto):
    diretorio = 'C:/workspace/teste.txt'
    arquivo = open(diretorio, 'w')
    # arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') #r = read
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    # cria uma lista, evitar que pegue palavra por palavra, a quebra será por Enter:
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    # criando uma lista com nome e média
    lista_media = []
    # acessando cada linha:
    for x in aluno_nota:
        # Separando alunos e as notas, pela virgula
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        print(aluno)
        # separando as notas
        lista_notas.pop(0)
        print(lista_notas)
        #convertendo de str para inteiro:
        media = lambda notas: sum([float(i) for i in notas]) / 4
        print(media(lista_notas))
        # criando uma lista com nome e média
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

# copiando um arquivo, a pasta tem que existir:
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/workspace/copia/')
    # shutil.copy(nome_arquivo, 'C:/workspace/copia/notas_alunos.txt')

# movendo um arquivo,
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/workspace/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # media_notas('notas.txt')
    # aluno = '\nRicardo, 3, 8, 6, 6\n'
    # atualizar_arquivo('notas.txt', aluno)

# # Criando uma função:
# def escrever_arquivo(texto):
#     diretorio = 'C:/workspace/teste.txt'
#     arquivo = open(diretorio, 'w')
#     # arquivo = open('teste.txt', 'w')
#     arquivo.write(texto)
#     arquivo.close()
#
# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()
#
# #Ler arquivo:
# def ler_arquivo(nome_arquivo):
#     arquivo = open(nome_arquivo, 'r') #r = read
#     texto = arquivo.read()
#     print(texto)
#
# if __name__ == '__main__':
#     escrever_arquivo('Primeira linha. \n')
#     # atualizar_arquivo('Quarta linha. \n')
#     # ler_arquivo('teste.txt')


# # Criando um arquivo:
# open('teste.txt', 'w')
#
# # Abrindo um arquivo:
# arquivo = open('teste.txt', 'w')
#
# # Escrevendo no arquivo:
# arquivo.write('Minha primeira escrita')
# arquivo.write('\nSegunda escrita')
#
# # Fechando o arquivo
# arquivo.close()
#
# #Atenção: se precisar atualizar o codigo é outro, nao usa o w, e sim o a:
# arquivo = open('teste.txt', 'a')
# arquivo.write('\nTerceira escrita')
# arquivo.write('\nQuarta escrita ')
# arquivo.close()
#