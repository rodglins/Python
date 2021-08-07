print('##########Calculadora############')

#Atribuindo as variáveis:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

#Realizando os cálculos:
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
resto = num1 % num2

#Imprimindo os resultados:
print('O valor da soma é: ', soma)
print('O valor da soma é: ' + str(soma))
print('soma: {}' .format(soma))
print('O valor da subtração é: ', subtracao , 'o tipo é: ', type(subtracao))
print('O valor da multiplicação é: ', multiplicacao)
print('O valor da divisão é: ', divisao)
print('O valor do resto é: ', resto)

#Atribuindo um tipo de dado:
x = '1'
soma2 = int(x) + 1
print(soma2)

#forma correta de transformar uma string em int, para evitar erros:
print('Soma: {}' .format(soma))

#Usando um alias:
print('Soma: {sum}' .format(sum=soma))

#Adicionando demais elementos da impressão:
print('Soma: {}. Subtração: {}' .format(soma, subtracao))

#Adicionando todos os elementos da calculadora
print('Soma: {sum}'
	'\nSubtração: {sub}'
	'\nMultiplicação: {mult}'
	'\nDivisão: {divi}' 
	'\nResto: {res}' .format(sum=soma,
                             sub=subtracao,
                             mult=multiplicacao,
                             divi=divisao,
                             res=resto))

#Mesmo resultado atribuindo uma variável:
resultado = ('Soma: {sum} '
             '\nSubtração: {sub} '
             '\nMultiplicação: {mult} '
             '\nDivisão: {divi} '
             '\nResto: {res}'
                .format(sum=soma,
                        sub=subtracao,
                        mult=multiplicacao,
                        divi=divisao,
                        res=resto))
print(resultado)