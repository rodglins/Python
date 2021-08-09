# biblioteca hashlib
import hashlib

# variavel resultado que recebe hashlib
resultado = hashlib.md5(b'Python Security')

print('O hash md5 da sring é: ', resultado.hexdigest())