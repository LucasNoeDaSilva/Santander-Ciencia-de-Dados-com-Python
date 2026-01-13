nome = str(input("digite seu nome"))
verificacao = "AEIOU"

for letra in nome:
    if letra.upper() in verificacao:
        print(letra)

#funcao range parametros: começo, fim, e de quantos em quantos
for numero in range(0, 100,10):
    print(numero)

opcao = 3

while opcao != 0:
    opcao = int(input("[1]sacar \n [2]extrato \n [0]sair"))

    if(opcao == 1):
        print("sacando")
    elif(opcao ==2):
        print("mostra extrato")    
    elif(opcao == 0):
        break;
