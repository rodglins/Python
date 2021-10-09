
#classe para evitar numeros inválidos:
#classe error não executa, mas precisa existir
class Error(Exception):
    pass
class InputError(Error):
    def __init__(self, message):
        self.message = message

# while: executa enquanto não digitado corretamente
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10:'))
        print(x)
        #verificando numeros inválidos:
        if x > 10:
            raise InputError('Nota não pode ser maior que dez')
        elif x < 0:
            raise InputError('Nota não pode ser menor que zero')
        break #parada do loop while
    #tratamento para valores inválidos como letras
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    #Tratando o erro de numeros inválidos:
    except InputError as ex:
        print(ex)