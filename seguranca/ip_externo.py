# operações com expressões regulares
import re
# codificação e decodificação JSON
import json
# funções e classes p abrir urls
from urllib.request import urlopen

# url ipinfo
url = 'http://ipinfo.io/json'

# variavel que abre a url e joga a requisição para esta variavel
resposta = urlopen(url)

# o que houver na variavel resposta,
# json carrega o script e insere na variavel dados.
dados = json.load(resposta)

# guarda os dados do ip:
ip = dados['ip']
# guarda os dados da seção org:
org = dados['org']
# guarda dos dados da cidade:
cid = dados['city']
# guarda dos dados do pais:
pais = dados['country']
# guarda os dados da região:
regiao = dados['region']

print('Detalhes do IP externo\n')

# define a ordem das seções que serão visualizadas:
print('IP: {4}\nRegião: {1}\nPaís: {2}\nCidade: {3}\nOrg.: {0}'.format(org,regiao,pais,cid,ip))
