def ola_mundo ():
    print("hello word")

def digite_nome ():
    nome = input("DIGITE SEU NOME")
    return nome

def ixibir_nome(nome):
    print(f"seu nome é {nome}")

ola_mundo()
nome =digite_nome()
ixibir_nome(nome)

#função nomeada
 
def salva_carro(marca,modelo,ano):  
    print(f"carro salvo com sucesso {marca},{modelo},{ano}")

def salva_carro2(marca,/,modelo,ano):  
    print(f"carro salvo com sucesso {marca},{modelo},{ano}")


salva_carro(marca="chevrolet",modelo="onix",ano=2026)
salva_carro2("chevrolet",modelo="onix",ano=2026)