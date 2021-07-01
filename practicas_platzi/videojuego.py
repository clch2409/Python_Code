import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_escogido = int(input("Escribe un número del 1 al 100: "))
    while numero_escogido != numero_aleatorio:
        if numero_escogido < numero_aleatorio:
            print("Busca un número mayor")
        else:
            print("Busca un número menor")
        numero_escogido = int(input("Escribe otro número: "))
    print("¡Ganaste!")


if __name__ == "__main__":
    run()