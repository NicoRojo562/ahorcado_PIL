import random

print("------BIENVENIDO AL JUEGO DEL AHORCADO-------\n")

nickname = input("Ingrese su Nickname: ")

print(nickname)

print("\n¡Hola " + nickname + "!\n")
print("Este juego tiene 3 Niveles:\n\t1-Easy\n \t2-Medium\n \t3-Hard")



def elegir_nivel():
    nivel = print(int(input("Elije tu nivel para jugar: ")))
    if nivel == 1:
        pass
    elif nivel == 2:
        pass
    elif nivel ==3:
        pass
    else:
        print("Opción incorrecta")
    return nivel

elegir_nivel()




#words_array=["Python","Class","Technology","Language","Coding"]
#
#def random_word():
#    word = random.choice(words_array) 
#    return word 

#random_word()