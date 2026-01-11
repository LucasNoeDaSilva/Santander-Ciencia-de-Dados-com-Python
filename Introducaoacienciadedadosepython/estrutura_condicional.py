valor_produto =3500.0
saldo = 5500.0

if(saldo>valor_produto):
    print("Vc concluiu a compra")
    
else:
    print("compra nao realizada")    
    if(saldo < 5000):
        print("valor insuficiente")

#if ternario
verificacao = "saque realizado" if(saldo > valor_produto) else "Não foi possivel realizar a compra"
print(verificacao)