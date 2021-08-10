# biblioteca de validação de numero de telefone:
import phonenumbers
from phonenumbers import geocoder

# inserindo o número:
phone = input('Digite o telefone no formato +551121662020: ')

# passando para a biblioteca que o phone é um telefone,
# ela converte o valor para um numero de telefone
# jogada dentro para a variavel phone_number
phone_number = phonenumbers.parse(phone)

# passa para o geocoder, na linguagem pt
print(geocoder.description_for_number(phone_number, 'pt'))

