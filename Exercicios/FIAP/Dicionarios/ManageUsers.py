"""
#Modo errodo , repetitivo, sem a funcao FuncoesDic.py

usuarios={}opcao=input("O que deseja realizar?\n" +
                       "<I> -Para Inserir um usuário\n"+
                       "<P> -Para Pesquisar um usuário\n"+
                       "<E> -Para Excluir um usuário\n"+
                       "<L> -Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?\n" +
                  "<I> -Para Inserir um usuário\n" +
                  "<P> -Para Pesquisar um usuário\n" +
                  "<E> -Para Excluir um usuário\n" +
                  "<L> -Para Listar um usuário: ").upper(
"""

#Modo correto com funcao FuncoesDic.py:

"""
from Dicionarios.FuncoesDic import *

usuarios={}
opcao= perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = perguntar()

"""

#Outra forma de otimizar o codigo anterior:

#Modo correto com funcao FuncoesDic.py:
"""
from Capitulo4_Dicionarios.Funcoes import *
usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()
"""


#Adicionando as variaveis pesquisar, excluir, listar:

from Dicionarios.FuncoesDic import *

usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? ").upper())
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? ").upper())
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()