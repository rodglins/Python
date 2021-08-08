import socket

# objeto de conexão
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso')

# host do servidor
host = 'localhost'
#porta do servidor
port = 5432

# bind faz a ligação entre cliente e servidor atraves do host e da porta
s.bind((host, port))
# mensagem do servidor
mensagem = '\nServidor: Olá, em que posso ajudar?'

# se houver ligação, True,
while 1:
    # cria variáveis:
    dados, end = s.recvfrom(4096)

# se houver ligação, dados, executa:
    if dados:
        print('Servidor enviando mensagem ...')
        # enviando a mensagem via pacotes udp:
        s.sendto(dados + (mensagem.encode()), end)