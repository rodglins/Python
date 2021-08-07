
# Exceções customizadas
# erro de divisão tratado
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    # print('fechando arquivo')
    # arquivo.close()
    # x = a

# except ZeroDivisionError:
except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por zero')

# tmb podemos utilizar:
except ArithmeticError:
    print('Não é possivel realizar a operação aritimética')

# # tratamento de erro genérico
# except:
#     print('Erro desconhecido')

# erro de busca por item desconhecido na lista
except IndexError:
    print('Erro ao acessar um indice inválido da lista')

# # base de todas as excecoes, tratar excecao que não previu:
# # ver Exception hierarchy docs.python.org
# except BaseException as ex:
#     print('erro desconhecido. Erro: {}'.format(ex))
# # tmb podemos usar o Exception:
except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))

else:
    print('Executa quando nao ocorre exceção')
    print('Instalação efetuada com sucesso')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()


