nome = ["lucas","pedro","noah"]
nome2= list("pedro")
nome3 =list(range(10))
print(nome)
print(nome2)
print(nome3)

matriz = [
    [1,2,3],
    [4,5,6]
]
print(matriz[1][2])

nome4 = ["l","u","c","a","s"]
print(nome4[2:])

for name in nome:
    print(name)

for indice, name in enumerate(nome):
    print(indice, name)

numeros =[1,2,3,4,5,6,7,8,9,10]
pares= []
for numero in numeros:
    if numero %2 ==0:
        pares.append(numero)

print(pares)

pares2= [numero for numero in numeros if numero % 2 == 0]
print(pares2)

quadrado = [numero **2 for numero in numeros ]
print(quadrado)