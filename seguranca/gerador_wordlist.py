
# biblioteca de iterações
import itertools

# variável que receberá o itertools:
resultado = itertools.permutations('abcdefmopr', 4)

# gera as combinações possiveis de forma aleatória
for i in resultado:
    print(''.join(i))