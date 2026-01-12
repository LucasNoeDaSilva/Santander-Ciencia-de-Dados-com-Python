nome = "Lucas"
idade = 24
profissao = "Análista de dados"
salario = 2500.0

#com format
print("Ola me chamo {}, tenho {}, sou um {} e atualmente estou recebendo{} ".format(nome,idade,profissao,salario)) 

#%
print("Ola me chamo %s, tenho %d, sou um %s e atualmente estou recebendo %f " %(nome,idade,profissao,salario)) 


#f string
print(f"Ola me chamo {nome}, tenho {idade}, sou um {profissao} e atualmente estou recebendo{salario}")
print(f"Ola me chamo {nome}, tenho {idade}, sou um {profissao} e atualmente estou recebendo{salario: 2.2f}")