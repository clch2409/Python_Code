def conversion(valor_dolar, nombre_moneda):
    dolares = float(input("¿Cuántos dólares tienes? "))
    moneda = dolares * valor_dolar
    moneda = round(moneda, 2)
    moneda = str(moneda)
    print("Tienes " + moneda + nombre_moneda)


menu = """
Bienvenidos al conversor de monedas 😁💰

1 - Soles
2 - Pesos colombianos
3 - Pesos mexicanos
4 - Pesos argentinos 

Elige el cambio de tus dólares:  """


menu= input(menu)
if menu == "1":
    conversion(3.72, " soles")
elif menu == "2":
    conversion(3706, " pesos colombianos")
elif menu == "3":
    conversion(19.93, " pesos mexicanos")
elif menu == "4":
    conversion(93.83, " pesos argentinos")
else:
    print("Elija una opción válida, por favor.")