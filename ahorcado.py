# Proyecto PIL - Juego Ahorcado
# Importamos el modulo random y clases
from tematicas import Tematica
import random


# Cargamos las palabras en la clase "Tematica"
def cargar_clases():
    frutas = ("naranja", "manzana", "banana", "kiwi", "pomelo")
    personas_celebres = ("Shakira", "Messi")
    mundo = ("Jamaica", "Inglaterra", "Argentina")
    provincias = ("San juan", "Jujuy", "Cordoba")
    car = Tematica(frutas, personas_celebres, mundo, provincias)
    
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
    print("-" * 80)
    print(f"1. Fácil" + " |2. Medio" + " |3. Difícil")
    
    opcion = validar_entre(1, 3, "\nIngrese el número de dificultad: ")
    
    return opcion
    


# Elegimos la tematica a utilizar en el juego
def elegir_tematica():
    print("-" * 80)
    print("Elección de Temática")
    print("-" * 80)
    print("Elija entre las siguientes temáticas: ")
    print("1. Frutas\n" + "2. Personas Célebres\n" + "3. Mundo\n" + "4. Provincias\n")
    
    eleccion = validar_entre(1, 4, "Opción elegida: ")
    
    print("\n--> Se registró su elección...")
    
    return eleccion


# Encripta la palabra
def encripted_word(word):
    for char in word:
        encripted_random_word = print(char.replace(char, " * "), end='')
    
    return encripted_random_word


# Función para obtener una palabra al azar según la temática elegida...
def getpalabra(tematica,car):
    palabra = None
    
    if tematica == 1:
        palabra = random.choice(car.frutas)
    elif tematica == 2:
        palabra = random.choice(car.personas_celebres)
    elif tematica == 3:
        palabra = random.choice(car.mundo)
    else:
        palabra = random.choice(car.provincias)

    return palabra


# Función para otorgar la cantidad de vidas que dispondrá el usuario segun la dificultad...
def cantvidas(nivel):
    if nivel == 1:
        vida = 6
               
    elif nivel == 2:
        vida = 5
               
    elif nivel == 3:
        vida = 4

    return vida
    




# Main Principal
def principal():
    print("-" * 80)
    print("------> BIENVENIDO AL JUEGO DEL AHORCADO <-------")
    print("-" * 80)

    # Pedimos al usuario que ingrese su nombre...
    nickname = input("\nIngrese su Nickname: ")

    # Saludamos al usuario con un mensaje simple...
    print("\n🙌 ¡Hola " + nickname + "! 🙌\n")

    # Creamos esta variable para validar luego, si el usuario ingreso en la opcion 1 para poder continuar el juego
    tematica = False
    tematica_elegida = None
    
    # Desarrollamos menu de opciones...
    opcion = -1
    while opcion != 0:
        print("-" * 80)
        print("MENÚ DE OPCIONES")
        print("-" * 80)
        print("1. Elegir temática")
        print("2. Jugar")
        print("0. Salir")
        opcion = int(input("Ingrese la opción elegida: "))

        # En esta opcion se activa la bandera "tematica" para notificar que se eligió una tematica para el ahorcado
        if opcion == 1:
            tematica = True

            # Asignamos a tematica_elegida, el num de tematica que eligió el usuario
            tematica_elegida = elegir_tematica()
        
        # Si elige la opcion 0 antes de comenzar a jugar, printeamos lo siguiente
        elif opcion == 0 and tematica == False:
            print("Saliste del juego " + nickname + "! Esperamos verte pronto!")
            break
        
        # Verificamos si el usuario no ingresó a la opcion 1...
        elif tematica == False:
            print("-" * 80)
            print("Debe ingresar primero la temática en la opcion 1...")

        # En opcion 2, validamos que la opcion sea igual a 2 y que la bandera tematica este prendida (valiendo True)
        # esto nos indicará que el usuario ya elgió una tematica para jugar...
        elif opcion == 2 and tematica:

            # Creamos nuestra clase "Temática" para tener las palabras a utilizar...
            car = cargar_clases()

            # Se elige el nivel de dificultad
            nivel_elegido = elegir_nivel1()

            # Se elige en base a la dificultad, la cant de vidas de las que dispone el usuario...
            vidas = cantvidas(nivel_elegido)
            
            # Obtenemos al azar la palabra de la temática elegida por el usuario
            palabra = getpalabra(tematica_elegida,car)

            # Hacemos toda la palabra en minuscula para que el usuario ingrese solo minusculas y las tome bien.
            palabra = palabra.lower()

            # Asignamos tamaño de la palabra
            yword = len(palabra)

            # Mostramos cant de letras de la palabra
            print("\nSu palabra tiene " + str(yword) + " letras \n")

            # Generamos una variable str vacia...
            palabrauser = ""

            # Verificamos que el usuario siga teniendo vidas para jugar...
            while vidas > 0:
                fallas = 0
                for letra in palabra:
                    if letra in palabrauser:
                        print(letra, end='')
                    else:
                         print(" * ", end='')
                         fallas += 1
                
                if fallas == 0:
                    print()
                    print("-" * 80)
                    print("🎉🎉🎉 Felicitaciones " + str(nickname) + " Ganaste 🎉🎉🎉")
                    break
                
                tuletra = input("\n--> Introduce tu letra:")
                palabrauser += tuletra.lower()
                
                if tuletra not in palabra:
                    vidas -= 1
                    print("-" * 80)
                    print("Has fallado")
                    print("-" * 80)
                    print("-- Te quedan", vidas,"vidas-- \n")
                                
                if vidas == 0:
                    print("-" * 80)
                    print(nickname + "! perdiste todas tus vidas 😔😔\n")
                    print("Gracias por jugar, a continuacion volverás al menú de opciones... \n")
            
        elif opcion == 0:
            print("-" * 80)
            print("🔥 Gracias por jugar con nosotros " + nickname + " nos vemos la próxima 🔥")
        else:
            print("-" * 80)
            print("Opción incorrecta! Vuelva a intentar " + nickname + " por favor!")

  

# Ejecutamos el programa
if __name__ == '__main__':
    principal()
