def payment():
    WrongAmount = True
    while WrongAmount:
        pay = int(input("¿Por cuanto será el pago a realizar? \n"))
        if (pay > debt):
            print("No es posible realizar un pago mayor al de su deuda actual  \n")
        else:
            WrongAmount = False
    interesPorcentual = interes/100
    monthlyInteres = interesPorcentual/12
    recalculatedDebt = (debt - pay)*(1 + monthlyInteres)
    newDebt = recalculatedDebt + newCharges

    print("Muchas Gracias por su pago. \n  El monto a quedar debiendo es de ${}".format(newDebt))


cardName = input("Favor de ingresar el nombre de la tarjeta: ")
interes = float(input("Tasa de interes: "))
debt = int(input("¿Cual es la deuda actual en su tarjeta? "))
newCharges = int(input("¿Cuanto suman los nuevos cargos? "))


print(" \n Nombre de la tarjeta: {} \n Interes: {} anual \n Su deuda actual es de: ${} \n".format(cardName, interes, debt))

transaction = input("Desea hacer el pago ahora?  ")

if (transaction == "si"):
    payment()
elif (transaction == "no"):
    print("Hasta Luego")
else:
    print("Opción invalida")


