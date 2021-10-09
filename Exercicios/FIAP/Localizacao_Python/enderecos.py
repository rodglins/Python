"""
endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('digiteAquigeocodeGoogleCloud').geocode(endereco)
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('keygooglecloud').geocode(endereco).postalcode
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('keygooglecloud').geocode(endereco).country
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('keygooglecloud').geocode(endereco).coordinates
print(resultado)

"""

from pygeocoder import Geocoder

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('keygooglecloud').reverse_geocode(-23.570807, -46.6444668)
print(resultado)

