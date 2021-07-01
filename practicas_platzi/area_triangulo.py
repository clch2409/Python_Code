from math import trunc

def calcular_area(a, b, c):
    if a == 0 or b == 0 or c == 0:
        print("Su triángulo no existe.")
    elif a == 1 or b == 1 or c == 1:
        print("Su triángulo no existe.")
    else:
        perimetro = a + b + c
        semiperimetro = perimetro / 2
        semiperimetro = trunc(semiperimetro)
        area = trunc((semiperimetro * (semiperimetro - a) * (semiperimetro - b) * (semiperimetro - c)) ** 0.5)
        print("El área de su triángulo es: " + str(area))
        print("Además, el perímetro de su triángulo es " + str(perimetro))

def tipo_triangulo(uno, dos, tres):
    if uno == dos and dos == tres:
        print("Tu triangulo es equilátero")
    elif uno == dos and dos != tres:
        print("Tu triángulo es isósceles")
    elif uno != dos and uno == tres:
        print("")
    elif uno == 0 or dos == 0 or tres == 0:
        print("")
    elif uno == 1 or dos == 1 or tres == 1:
        print("Su triángulo no existe.")
    else:
        print("Tu triángulo es escaleno")

def run():
    bienvenida = """ 
    Hola, bienvenidos al primer programa de python que hago por mi mismo.
    Es, básicamente, un calculador de áreas de triángulos jeje
    """

    print(bienvenida)

    primero = int(input("Escriba el primer lado de su triángulo: "))
    segundo = int(input("Escriba el segundo lado de su triángulo: "))
    tercero = int(input("Escriba el tercer lado de su triangulo: "))
    calcular_area(primero, segundo, tercero)
    tipo_triangulo(primero, segundo, tercero)

if __name__ == "__main__":
    run()