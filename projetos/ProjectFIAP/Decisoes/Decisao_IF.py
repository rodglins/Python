responsavel=input("Digite o nome do responsável: ")
funcionario=input("Digite o nome do funcionário: ")
evento=input("Digite o nome do evento: ")
valor=float(input("Digite o valor que será ressarcido: "))

print("Declaro para o senhor " + responsavel + ", que o senhor " + funcionario + " esteve presente no evento " + evento + " e gastou o valor de R$ " + str(valor) + " com a entrada.")


"""
nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para sala AMARELA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala AMARELA - SEM prioridade")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - COM prioridade")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala BRANCA - SEM prioridade")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
"""
