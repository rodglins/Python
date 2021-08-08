"""
endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco)
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).postalcode
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).country
print(resultado)

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).coordinates
print(resultado)

"""

from pygeocoder import Geocoder

endereco = "avenida paulista, 100 sao paulo"
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').reverse_geocode(-23.570807, -46.6444668)
print(resultado)

