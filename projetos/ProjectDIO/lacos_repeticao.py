#Laços de repetição

# #imprimir 100 primeiros numeros:
# for x in range(100):
#     print(x)

# #imprimir intervalo de numeros:
# for x in range(90, 100):
#     print(x)

# #Usando o FOR
# #descobrindo se é numero primo:
# a = int(input('Entre com o número: '))
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1 # é igual a div = div + 1
# if div == 2:
#     print('número {} é primo'. format(a))
# else:
#     print('número {} não é primo'. format(a))

# #Usando o FOR in FOR:
# #imprimindo os numeros primos do 0 ao 100:
# for num in range(101):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1 # é igual a div = div + 1
#     if div == 2:
#         print(num)

# #imprimindo os numeros primos do 0 até o número digitado:
# a = int(input('Entre com um número: '))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x, resto)
#         if resto == 0:
#             div += 1 # é igual a div = div + 1
#     if div == 2:
#         print(num)

# #Uso do WHILE:
# #laco de repetição até alcançar o objetivo
# a = 0
# while a<= 10:
#     print(a)
#     a += 1

# #Cálculo de média usando o WHILE:
# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))


a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado a nota do primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado a nota do segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado a nota do terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado a nota do quarto bimestre: '))

media = (a + b + c + d) / 4
print('media: {}' .format(media))











