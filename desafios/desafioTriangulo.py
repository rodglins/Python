'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

 
Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0

Area = 10.0

6.0 4.0 2.1

Perimetro = 12.1

 '''



x = input().split()
a, b, c =x
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    print('Area = {:.1f}'.format(((a + b) / 2) * c))