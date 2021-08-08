# módulo biblioteca os
# recursos do S.O.
import os 

print('#' * 60)
# variavel e input
ip_ou_host = input('Digite o ip ou host a ser verificado: ')
print('-' * 60)
# comandos módulo biblioteca os
# -n numero de pacotes (6)
os.system('ping -n 6 {}'.format(ip_ou_host))
print('-' * 60)
