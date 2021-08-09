# comparador de hashes para comparar arquivos no projeto
import hashlib

# adicionando arquivos para comparar
arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# objeto hash, recebe do hashlib new com o algoritmo de hash
hash1 = hashlib.new('ripemd160')
# especificar os arquivos que serão utilizados
# rb leitura / binário:
hash1.update(open(arquivo1, 'rb').read())

# arquivo a comparar:
hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

# fazendo a comparação:
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())