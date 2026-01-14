lista=set([1,2,3,4,5,6,6,1,7])
print(lista)
lista2 = {1,2,3,4,5,5,6,10}
print(lista2)



conjunto = {"lucas", "vanessa", "laura","lucas"}
for i, nome in enumerate(conjunto):
    print(i, nome)

conjunto = list(conjunto)
print(conjunto[0])

conjuntoa = set([1,2,3])
conjuntob = set([3,4])
conjuntoa.union(conjuntob)
print(conjuntoa.difference(conjuntob))