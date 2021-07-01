# def run():
#     greetings = "Hola mundo"
#     print(greetings)

# def run():
#     nombre = input("Escribe tu nombre, por favor: ")
#     print("Hola " + nombre + ". ¿Cómo estás?")

# def run():
#     operacion = ((3 + 2) / (2 * 5)) ** 2
#     print(operacion)

# def run():
#     time_work = float(input("Escribe la cantidad de horas que trabajas: "))
#     time_price = float(input("Escribe el costo por hora de tu trabajo: "))
#     print("Esta es la cantidad de dinero que cobras al finalizar tu jornada laboral diaria: " + str(time_work * time_price) + " soles")

# def run():
#     welcome = """ 
#     Hola, en este progama te mostrare la suma del 1 al valor que tú dispongas a introducir.
#     Por lo que te invito a probarlo, si deseas saber qué hice, usa esta fórmula para comparar el resultado:
#         n(n+1)/2
# """
#     numero = int(input(welcome))
#     operacion = (numero * (numero + 1)) / 2
#     print("El resultado de su suma de términos es: " + str(operacion))

# def imc(a, b):
#     operacion = a / (b ** 2)
#     operacion = round(operacion, 2)
#     print("Su Índice de masa corporal es: " + str(operacion))


# def run():
#     welcome = """ 
#         Hola, de nuevo. En este programa te mostraré tu Índice de masa corporal.
#         Además de eso, te indicaré si te encuentras en buena forma física o tienes algún problema de posible obesidad o insuficiencia ponderal.
#         Igualmente, te dejo la fórmula para que lo puedas hacer por ti mism@
#             peso(kg) / altura(m)^2
#     """
#     print(welcome)
#     peso = float(input("Escriba su peso en kilogramos, por favor: "))
#     altura = float(input("Escriba su altura en metro, por favor: "))
#     imc(peso, altura)

# def peso(clown, doll):
#     w_clown = int(clown) * 112
#     w_doll = int(doll) * 75
#     print("El peso total de su pedido es: " + str(w_clown + w_doll) + " gramos")


# def run():

#     welcome = """
#         Buenas, necesito que me proporcione la cantidad de payasos y muñeca.
#         Para que de esta manera se le pueda mostrar el peso del pedido y más adelante poder cobrarle.
#         Gracias :) 
#     """
#     print(welcome)
#     payaso = input("Indique la cantidad de payasos que desea: ")
#     muneca = input("Indique la cantidad de muñecas que desea: ")
#     peso(payaso, muneca)

# def cuenta_ahorro(dinero, time):
#     interes = 4 / 100
#     dinero_total = dinero * ((1 + interes) ** time)
#     dinero_total = round(dinero_total, 2)

#     if time == 1:
#         print("Su ahorro en un año es :" + str(dinero_total))
#     elif time == 2:
#         print("Sus ahorros en dos año son :" + str(dinero_total))
#     elif time == 3:
#         print("Sus ahorros en tres años son :" + str(dinero_total))
#     else:
#         print("Elija una opción válida, por favor.")

# def run():

#     welcome = """
#         Bienvenido a su cuenta de ahorro en Python. 
#         En este programa le solicitaré el dinero a depositar y al final conocerá el monto que usted desee.
#         Es decir, si desea ver el monto ahorrado en un año, dos o tres.
#     """
#     print(welcome)
#     money = float(input("Ingrese la cantidad a depositar: "))
#     years = int(input("¿Desea ver el ahorro en uno, dos o tres años (escoja 1, 2 o 3): "))
#     cuenta_ahorro(money, years)
    

if __name__ == "__main__":
    run()