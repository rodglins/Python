



####Cálculo de média######
#Média de notas com verificação no final:
# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#if a
#     print('media: {}' .format(media))
# else:
#     print('foi informada alguma nota errada')

#Média de notas com verificação em cada input:
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado a nota do primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado a nota do segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado a nota do terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado a nota do quarto bimestre: '))

media = (a + b + c + d) / 4
print('media: {}' .format(media))






######### #Descobrindo se o valor é par ou ímpar:
# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número é par')
# else:
#     print('Número é impar')
#
# #Descobrindo se um número é par entre os digitados:
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# #if resto_a == 0 or resto_b == 0: #Mesmo resultado:
# if resto_a == 0 or not resto_b > 0: #or not = false,
#     print('um dos valores é par')
# else:
#     print('Nenhum número par foi digitado')

# #####################
# #Descobrindo o maior valor entre 2 números:
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
#
# if a > b:
#     print('o maior número é {}' .format(a))
# else:
#     print('o maior numero é {}' .format(b))
#
# print('Adicionando um terceiro valor:')
#
# #Descobrindo o maior valor entre 3 numeros:
# c = int(input('Terceiro valor: '))
# if a > b and a > c:
#     print('o maior número é {}' .format(a))
# elif b > a and b > c:
#     print('o maior numero é {}' .format(b))
# else:
#     print('o maior número é {}' .format(c))
#
# print('final do programa')