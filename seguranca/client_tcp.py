# biblioteca relacionamento placa de rede com s.o.
# chama api de abertura de conexões
import socket

# biblioteca sys, fornece acesso a variaveis e funções com o interpretador
import sys

# tentando uma conexão tcp/ip:
def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # tratando erros
    except socket.error as e:
        print('A conexão falhou!')
        print('Erro: {}'.format(e))
        # fechando o programa
        sys.exit()

    print('Socket criado com sucesso!')

    HostAlvo = input('Digite o host ou IP a ser conectado: ')
    PortaAlvo = input('Digite a porta a ser conectada: ')

    # Testando a conexão
    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Cliente TCP conectado com sucesso no host: {}'.format(HostAlvo), ' e na porta: {}'.format(PortaAlvo))
        # fechando a conexão para não ficar em loop
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar ao host: {}'.format(HostAlvo), ' e na porta: {}'.format(PortaAlvo))
        print('Erro: {}'.format(e))
        # sai da aplicação em caso de erro
        sys.exit()

if __name__ == '__main__':
    main()