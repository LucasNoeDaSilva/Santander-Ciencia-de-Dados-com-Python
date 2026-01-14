
contatos = {
    "lucasgmail": {"nome": "lucas", "idade": 24},
    "vitoriagmail": {"nome": "vitoria", "idade": 15},
    "mariagmail": {"nome": "maria", "idade": 50}
}
contatos2 = contatos.copy()
contatos.fromkeys(["telefone"])
print(contatos.keys())
print(contatos)
#contatos.clear()
print(contatos2.get("lucasgmail",{}))
contatos.pop("lucasgmail",{})
print(contatos)