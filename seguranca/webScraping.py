# Biblioteca BeautifulSoup extrai dados de arquivos html e xml
from bs4 import BeautifulSoup
# Biblioteca requests - envia solicitações http em python
import requests

# definindo o site a obter informações:
site = requests.get("https://www.climatempo.com.br/").content

# variavel soup recebe conteúdo de site
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string e imprime
print(soup.prettify())