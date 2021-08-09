# Biblioteca BeautifulSoup extrai dados de arquivos html e xml
from bs4 import BeautifulSoup
# Biblioteca requests - envia solicitações http em python
import requests

# definindo o site a obter informações:
site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

# variavel soup recebe conteúdo de site
soup = BeautifulSoup(site, 'html.parser')

# # transforma html em string e imprime
# print(soup.prettify())

#recuperando a temperatura pelo site. Origem: (<p class="-gray _flex _align-center">)
temperatura = soup.find("span", class_="-gray-light")

# transforma html em string
print(temperatura.string)