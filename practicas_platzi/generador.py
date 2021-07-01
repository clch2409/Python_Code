import random 


def generar_password():
    mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    simbolos = ["(", ")", "/", "&", "~", "#", "$", "!", "¡", "¿", "?", "-", "{", "}"]

    caracteres = mayusculas + minusculas + numeros + simbolos

    password = []

    for i in range(15):
        caracter_aleatorio = random.choice(caracteres)
        password.append(caracter_aleatorio)
    password = "".join(password)
    return password
        
def run():
    password = generar_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()