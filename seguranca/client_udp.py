import socket

# THREE-WAY HANDSHAKE
# objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso.')

host = 'localhost' # host cliente
porta = 5433 # porta cliente
mensagem = 'Realizando um teste com o servidor' # mensagem para enviar

try:
    print('Cliente: {}'.format(mensagem))
    # enviando a mensagem ao servidor e esperar uma resposta
    # encode codifica e envia um pacote ao servidor
    s.sendto(mensagem.encode(), (host, 5432))

    # recebendo a mensagem do conect do servidor
    dados, servidor = s.recvfrom(4096)
    # desempacotando os dados:
    dados = dados.decode()
    print('Cliente: {}'.format(dados))
finally:
    print('Cliente: Fechando a conexão.')
    # fecha a conexão para encerrar o loop:
    s.close()



