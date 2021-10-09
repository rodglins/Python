"""
from pygeocoder import Geocoder
endereco = '1222, Lins de Vasconcelos, Sao Paulo, SP'
print(Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).coordinates)


resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).country
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).coordinates
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').geocode(endereco).state
"""

from pygeocoder import Geocoder

endereco = 'avenida paulista, 100, Sao Paulo'
resultado = Geocoder('AIzaSyCKifeG7c5OiA_6A1UITwRkHJIqocTCKV8').reverse_geocode(-23.570807, -46.6444668)
print(resultado)

