from exer3paq import tarjeta, usuario

lista_tarjetas = []
done = False
while (not done):
    card = tarjeta.crear_tarjeta(lista_tarjetas)
    lista_tarjetas.append(card)
    tarjeta.captura_nueva_deuda(card)
    usuario.pago_recurrente(card)
    choose = input("\n ¿Quiere hacer otro pago? \n")
    if choose == "no":
        done = True

tarjeta.imprimir_reportes(lista_tarjetas)

print("\n Hasta Luego \n")