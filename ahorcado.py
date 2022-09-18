# Proyecto PIL - Juego Ahorcado
# Importamos el modulo random y clases
import tematicas
import random


# Cargamos las palabras en las clases
def cargar_clases():
    frutas = ("naranja", "manzana", "banana", "kiwi", "pomelo")
    personas_celebres = ("Shakira", "Messi")
    mundo = ("Jamaica", "Inglaterra", "Argentina")
    provincias = ("San juan", "Jujuy", "Cordoba")
    car = tematicas.Tematica(frutas, personas_celebres, mundo, provincias)
    return car


# Función de validación
def validar_entre(inf, sup, mensaje):
    opcion = int(input(mensaje))
    while opcion < inf or opcion > sup:
        print("Error! Debe elegir un valor que valido...")
        opcion = int(input(mensaje))
    return opcion


# Funcion que elige el nivel
def elegir_nivel1():
    print("-" * 80)
    print("Elección de Dificultad")
    print(f"1. Facil" + " |2. Medio" + " |3. Dificil")
    opcion = validar_entre(1, 3, "Ingrese el numero de dificultad: ")
    return opcion
    

def elegir_nivel():
    nivel = int(input("Elije tu nivel para jugar: "))
    if nivel == 1:
        pass
    elif nivel == 2:
        pass
    elif nivel == 3:
        pass
    else:
        print("Opción incorrecta")
    return nivel


# Elegimos la tematica a utilizar en el juego
def elegir_tematica():
    print("Elección de Tematica")
    print("Elija entre las siguientes temáticas: ")
    print("1. Frutas\n" + "2. Personas Celebres\n" + "3. Mundo\n" + "4. Provincias\n")
    eleccion = validar_entre(1, 4, "Opcion elegida: ")
    return eleccion


# Encripta la palabra
def encripted_word(word):
    for char in word:
        encripted_random_word = print(char.replace(char, " * "), end='')

    return encripted_random_word


# Main Principal
def principal():
    print("-" * 80)
    print("------> BIENVENIDO AL JUEGO DEL AHORCADO <-------")
    print("-" * 80)

    # Pedimos al usuario que ingrese su nombre...
    nickname = input("Ingrese su Nickname: ")

    # Saludamos al usuario con un mensaje simple...
    print("\n¡Hola " + nickname + "!\n")

    # Creamos esta variable para validar luego, si el usuario ingreso en la opcion 1 para poder continuar el juego
    tematica = False
    tematica_elegida = None

    # Desarrollamos menu de opciones...
    opcion = -1
    while opcion != 0:
        print("MENÚ DE OPCIONES")
        print("1. Elegir tematica")
        print("2. Jugar")
        print("0. Salir")
        opcion = int(input("Ingrese la opcion elegida: "))

        # En esta opcion se activa la bandera "tematica" para notificar que se eligió una tematica para el ahorcado
        if opcion == 1:
            tematica = True

            # En esta opcion pensaba hacer elegir la tematica para usar luego en la opcion 2...
            tematica_elegida = elegir_tematica()

        elif tematica == False:
            print("-" * 80)
            print("Debe ingresar primero la temática en la opcion 1...")

        # En opcion 2, validamos que la opcion sea igual a 2 y que la bandera tematica este prendida (valiendo True)
        # esto nos indicará que el usuario ya elgió una tematica para jugar...
        elif opcion == 2 and tematica:
            nivel_elegido = elegir_nivel1()
            if nivel_elegido == 1:
                # jugamos nivel facil
                pass
            elif nivel_elegido == 2:
                # jugamos nivel medio
                pass
            elif nivel_elegido == 3:
                # jugamos nivel dificil
                pass
        elif opcion == 0:
            print("Gracias por jugar con nosotros " + nickname + " nos vemos la próxima!")
        else:
            print("Opción incorrecta! Vuelva a intentar " + nickname + " por favor!")

    words_array = ["Python", "Class", "Technology", "Language", "Coding"]

    word = random.choice(words_array)

    yword = str(len(word))

    print("su palabra tiene " + yword + " letras")

    encripted_word(word)


# Ejecutamos el programa
if __name__ == '__main__':
    principal()
