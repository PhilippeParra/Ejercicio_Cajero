
TB1 = 0
TB2 = 0
TB3 = 0

print("-----------------------------------------------")
print("Recuerde que el cheque debe ser multiplo de 100")
print("-----------------------------------------------")
CH = int(input("Digite el valor de su cheque: "))
print("----------------------------------------")

while CH != 0:
    B1 = int(CH / 10000)
    R = CH - (B1 * 10000)
    B2 = int(R / 2000)
    R = R - (B2 * 2000)
    B3 = int(R / 100)
    TB1 = TB1 + B1
    TB2 = TB2 + B2
    TB3 = TB3 + B3


    print("Valor del cheque=" , CH)
    print("----------------------------")
    print("-Cantidad de Billetes-")
    print("Billetes de 10000$:" , B1)
    print("Billetes de 2000$: " , B2)
    print("Billetes de 100$:" , B3)

    print("----------------------------------------")
    CH = int(input("Digite el valor de su cheque: "))
    print("----------------------------------------")

print("----------------------------------------")
print("Total de Billetes entregados en el dia")
print("Billetes de 10000$:" , TB1)
print("Billetes de 2000$:" , TB2)
print("Billetes de 100$:" , TB3)