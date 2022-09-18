import random


#Funcion q elige el nivel
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


#encripta la palabra

def encripted_word(word):
    for char in word:
        
        encripted_random_word = print(char.replace(char," * "), end='')
     
    return encripted_random_word



#main 
print("------BIENVENIDO AL JUEGO DEL AHORCADO-------\n")

nickname = input("Ingrese su Nickname: ")

print(nickname)

print("\n¡Hola " + nickname + "!\n")
print("Este juego tiene 3 Niveles:\n\t1-Easy\n \t2-Medium\n \t3-Hard")

elegir_nivel()

words_array=["Python","Class","Technology","Language","Coding"]

word= random.choice(words_array)

yword=str(len(word))

print("su palabra tiene " + yword +" letras")

encripted_word(word)

