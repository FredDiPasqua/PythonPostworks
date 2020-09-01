"""Modulo de tarjeta"""

def crear_tarjeta(tarjetas):
    """Permite ingresar una nueva tarjeta"""
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
    """Aplica el pago y calcula la nueva deuda"""
    interesPorcentual = tarjeta["interes"]/100
    monthlyInteres = interesPorcentual/12
    recalculatedDebt = (tarjeta["debt"] - tarjeta["pay"])*(1 + monthlyInteres)
    newDebt = recalculatedDebt + tarjeta["newCharges"]
    tarjeta["monthlyInteres"] = monthlyInteres
    tarjeta["newDebt"] = newDebt
    generar_reporte(tarjeta)

def generar_reporte(tarjeta):
    """Imprime el reporte de la tarjeta"""
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
    """Imprime los reportes de todas las tarjetas ingresadas"""
    for tarjeta in tarjetas:
        generar_reporte(tarjeta)



        

 








