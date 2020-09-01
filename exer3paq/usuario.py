

"""Modulo de usuario"""


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
        """.format(("%.2f" % threeM), ("%.2f" % sixM), ("%.2f" % twelveM))
    )