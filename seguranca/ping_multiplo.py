# percorrer o arquivo para verificar quais hosts serão pingados

# biblioteca
import os
# biblioteca tempo de execução
import time

# abrindo o arquivo
with open('hosts.txt') as file:
    dump = file.read()
    # split, consertar a orientação do texto:
    dump = dump.splitlines()

    # executando o ping nos ips da lista
    for ip in dump:
        print('Verificando o ip: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {} '.format(ip))
        print('-' * 60)
        # pausa entre os processos
        time.sleep(5)

