# fornece tipos de dados compatíveis com linguagem C
# e permite funções de chamada em DLLs ou bibliotecas compartilhadas
import ctypes

pasta = input('Digite o caminho da pasta a ser ocultada')

# passando atributos:
# = hexadecimal
atributo_ocultar = 0x02

# chamando a biblioteca ctypes a
# dll para manipulação de arquivo e se torne oculto
retorno = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else:
    print('Arquivo não foi ocultado')