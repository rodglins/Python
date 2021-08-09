
# biblioteca de iterações
import itertools

# inserir palavra para gerar wordlist
string = input('String a ser permutada: ')

# variável que receberá o itertools:
resultado = itertools.permutations(string, len(string))

# gera as combinações possiveis de forma aleatória
for i in resultado:
    print(''.join(i))