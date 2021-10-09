import requests

# json e python
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    # print(response.text)
    # print(type(response.text))
    print(response.json())
    # print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

# json e python 2:
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

# busca em urls
def retorna_response(url):
    response = requests.get(url)
    return response.text
# é possível buscar um texto pela raspagem de página,  Scraping com urllib.request e BeautifulSoup.

if __name__ == '__main__':
    response = retorna_response('https://www.uol.com.br')
    print(response)
    # # retorna_dados_cep('22041001')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])



