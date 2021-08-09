# biblioteca random: implementa geradores de senhas alfanuméricas
import random
# biblioteca string: operações para strings
import string

# tamanho da senha:
tamanho = int(input('Digite o tamanho da senha que deseja: '))
# estrutura da senha: letras maiusculas e minusculas + numeros + simbolos especiais
chars = string.ascii_letters + string.digits + '!@#$%¨&*(){}[];:,><?/\|~^=-'

# objeto chamado rnd, chama funcao SystemRamdom, classe Urandom, gera numeros aleatorios a apartir de pre definicoes
rnd = random.SystemRandom()

# random retorna uma lista com caracteres randomicos, gerado no chars, gera uma nota letra, simbolo ou numero aleatório.
print(''.join(rnd.choice(chars) for i in range(tamanho)))

