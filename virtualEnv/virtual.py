#ambiente virtual
import requests

response = requests.get('https://viacep.com.br/ws/{}/json/'.format(22041001))
print(response.status_code)
