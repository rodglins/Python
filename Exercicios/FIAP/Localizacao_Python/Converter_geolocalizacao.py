

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.geocode("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))

from geopy.geocoders import Nominatim
from Listas_Funcoes.Funcoes_JSON import ler_arquivo,gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")
dicionario=ler_arquivo("entrada.json")
lista=dicionario["endereco"]
endereco=lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida={"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida,"saida.json")







