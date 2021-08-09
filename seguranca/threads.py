# paralelismo, multitarefas, processamentos simultaneos

#importando a classe thread:
from threading import Thread
import time

# função carros:
def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))

# # função 2
# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro2: ', trajeto)
#         trajeto += velocidade

# chamando a função
t_carro1 = Thread(target=carro, args=[1, 'Rodrigo'])
t_carro2 = Thread(target=carro, args=[2, 'Python'])

# start carros
t_carro1.start()
t_carro2.start()