"""
from datetime import datetime
import platform

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())
print("Data................................: ", datetime.now())


#######

print(getpass.getuser())
print(getpass.getpass("Digite sua senha: ..."))

######

usuario=input("Digite o usuário: ").upper()
senha= input("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")
"""



import getpass

usuario = input("Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "oi":
    print("Usuário logado")
else:
    print("Login Negado")