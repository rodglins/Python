# biblioteca hashlib
import hashlib

# Inserindo o texto
string = input('Digite o texto para gerar a hash: ')

# escolhendo o codificador:
menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a gerar: '''))

# Informações do menu
if menu == 1:
    # variavel resultado que recebe hashlib
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O hash MD5 da sring é: ', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O hash SHA1 da sring é: ', string, 'é: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O hash SHA256 da sring é: ', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O hash SHA512 da sring é: ', string, 'é: ', resultado.hexdigest())
else:
    print('Algo está errado, tente novamente')