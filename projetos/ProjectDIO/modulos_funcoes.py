from metodos_funcoes_classes_televisao import Televisao
from metodos_funcoes_classes_calculadora1 import Calculadora
from contador_letras import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(5, 10)
    print(calculadora.soma())
    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {}' .format(total_letras))
    print(teste()) #importanto função é necessário ()
