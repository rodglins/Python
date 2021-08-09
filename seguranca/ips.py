# biblioteca que cria e manipula endereços
import ipaddress

# variável  para receber o ip:
# ip = '192.168.0.1'

# trabalhando com redes:
ip = '192.168.0.0/0'
# se diferente de .0/ usar o strict=False
# redes:
# 192.168.0.0/0
# 192.168.0.0/4
# 192.168.0.0/32
# 192.168.0.0/24

# variavel endereço que transfere o conteudo da variavel ip em um endereço ip
# endereco = ipaddress.ip_address(ip)

rede = ipaddress.ip_network(ip, strict=False)

# # tds ips da rede:
for ip in rede:
    print(ip)

# print(rede)

# print(endereco + 100)
# print(endereco + 256)
# print(endereco + 2000)