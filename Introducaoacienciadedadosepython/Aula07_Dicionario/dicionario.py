pessoa = {"nome":"lucas","idade":24}
pesssoa2 = dict(name="lucas", idade=24)
print(pesssoa2)
pesssoa2["telefone"] = 11946756784567
print(pesssoa2)
print(pessoa["nome"])

contatos = {
    "lucasgmail": {"nome": "lucas", "idade": 24},
    "vitoriagmail": {"nome": "vitoria", "idade": 15},
    "mariagmail": {"nome": "maria", "idade": 50}
}

for chave, valor in contatos.items():
    print(chave, valor)