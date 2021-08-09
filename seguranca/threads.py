# paralelismo, multitarefas, processamentos simultaneos

#importando a classe thread:
from threading import Thread

# função 1
def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro1: ', trajeto)
        trajeto += velocidade

# função 2
def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro2: ', trajeto)
        trajeto += velocidade

# chamando a função com velocidade 10
t_carro1 = Thread(target=carro1, args=[1])
t_carro2 = Thread(target=carro1, args=[1.5])

#start carros
t_carro1.start()
t_carro2.start()