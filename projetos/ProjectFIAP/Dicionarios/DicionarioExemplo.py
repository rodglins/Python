
#Dicionário vazio
usuarios = {}
print(usuarios)

#Dicionário com dados
usuarios = {
    "chaves" : ["Chaves do 8", "24/12/2021", "Recep_01"],
    "quico" :["Quico das Flores", "20/12/2021", "Raiox_03"]
}
print(usuarios)

#inserindo informações no dicionário

usuarios["florinda"] = ["Dona Florinda", "24/12/2021", "Raiox_01"]
print(usuarios)

#obtendo informações do dicionário

print("####----####")
print(usuarios.get("quico"))