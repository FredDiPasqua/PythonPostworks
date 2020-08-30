
def crear_tarjeta():
    ok = False
    while not ok: 
        tarjeta = {
            "cardName" : input("\nFavor de ingresar el nombre de la tarjeta: \n"),
            "interes" : float(input("Tasa de interes: \n")),
            "debt" : float(input("¿Cual es la deuda actual en su tarjeta? \n")),
            "newCharges" : float(input("¿Cuanto suman los nuevos cargos? \n")),
            "pay" : float(input("¿Por cuanto será el pago a realizar? \n"))
        }
        ok = True
        for tarj in tarjetas:
            if tarjeta["cardName"] == tarj["cardName"]:
                print("\n *-   INVALIDO   -* \n  Ya existe una tarjeta con ese nombre")
                ok = False
    WrongAmount = True
    while WrongAmount:
        if (tarjeta["pay"] > tarjeta["debt"]):
            print("  *-  No es posible realizar un pago mayor al de su deuda actual  -*  \n")
            tarjeta["pay"] = int(input("¿Por cuanto será el pago a realizar? \n"))
        else:
            WrongAmount = False
    return tarjeta

def captura_nueva_deuda(tarjeta):
    interesPorcentual = tarjeta["interes"]/100
    monthlyInteres = interesPorcentual/12
    recalculatedDebt = (tarjeta["debt"] - tarjeta["pay"])*(1 + monthlyInteres)
    newDebt = recalculatedDebt + tarjeta["newCharges"]
    tarjeta["monthlyInteres"] = monthlyInteres
    tarjeta["newDebt"] = newDebt
    generar_reporte(tarjeta)

def generar_reporte(tarjeta):
    print(
        """
        Reporte de tarjeta {}. \n
        \n
        Su tasa de interes es de {}% anual \n
        Saldo previo: ${} \n
        Nuevos cargos generados al corte: ${} \n
        Pago realizado: ${} \n
        Saldo actual a pagar: ${} \n
        """.format(tarjeta["cardName"], tarjeta["interes"], tarjeta["debt"], tarjeta["newCharges"], tarjeta["pay"], ("%.2f" % tarjeta["newDebt"]))
    )

def imprimir_reportes(tarjetas):
    for tarjeta in tarjetas:
        generar_reporte(tarjeta)

def pago_recurrente(tarjeta):
    threeM = tarjeta["debt"] / ( ( 1 - ( (1 + tarjeta["monthlyInteres"])**-3 ) ) / tarjeta["monthlyInteres"] )
    sixM = tarjeta["debt"] / ( ( 1 - ( (1 + tarjeta["monthlyInteres"])**-6 ) ) / tarjeta["monthlyInteres"] )
    twelveM = tarjeta["debt"] / ( ( 1 - ( (1 + tarjeta["monthlyInteres"])**-12 ) ) / tarjeta["monthlyInteres"] )
    print(
        """
        En este punto, si no tuviera nuevos cargos su pago recurrente sería: \n 
        a 3 meses: ${},
        a 6 meses ${},
        a 12 meses ${}
        """.format(threeM, sixM, twelveM)
    )

        

tarjetas = []
done = False
while (not done):
    card = crear_tarjeta()
    tarjetas.append(card)
    captura_nueva_deuda(card)
    pago_recurrente(card)
    choose = input("\n ¿Quiere hacer otro pago? \n")
    if choose == "no":
        done = True

imprimir_reportes(tarjetas)

print("\n Hasta Luego \n") 






# def payment():
#     WrongAmount = True
#     while WrongAmount:
#         pay = int(input("¿Por cuanto será el pago a realizar? \n"))
#         if (pay > debt):
#             print("No es posible realizar un pago mayor al de su deuda actual  \n")
#         else:
#             WrongAmount = False
#     interesPorcentual = interes/100
#     monthlyInteres = interesPorcentual/12
#     recalculatedDebt = (debt - pay)*(1 + monthlyInteres)
#     newDebt = recalculatedDebt + newCharges

#     print("Muchas Gracias por su pago. \n  El monto a quedar debiendo es de ${}".format(newDebt))


# cardName = input("Favor de ingresar el nombre de la tarjeta: ")
# interes = float(input("Tasa de interes: "))
# debt = int(input("¿Cual es la deuda actual en su tarjeta? "))
# newCharges = int(input("¿Cuanto suman los nuevos cargos? "))


# print(" \n Nombre de la tarjeta: {} \n Interes: {} anual \n Su deuda actual es de: ${} \n".format(cardName, interes, debt))

# transaction = input("Desea hacer el pago ahora?  ")

# if (transaction == "si"):
#     payment()
# elif (transaction == "no"):
#     print("Hasta Luego")
# else:
#     print("Opción invalida")


