"""
import json

#Listando itens do arquivo json
with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    print(dicionario)

#exibindo o json ordenadamente:
import json

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " | " + str(dados))

"""

import json

dicionario = {
  "CHAVES":["CHAVES DO 8", "14/04/2021","RECEP_01"],
  "QUICO": ["QUICO FLORES","24/04/2021","RAIOX_01"],
  "FLORINDA": ["DONA FLORINDA", "15/04/2021","RECEP_03"]
}

with open("bd1.json","w") as json_file:
    json.dump(dicionario,json_file)