"""

from socket import *

servidor="127.0.0.1" #localhost 192.168.0.1 ou 10.0.0.1
porta=43210

msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket=socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor,porta))
obj_socket.send(msg)
resposta=obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()

"""

from socket import *

servidor="127.0.0.1"
porta=43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    resposta=obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper()=="FIM":
        break
obj_socket.close()