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

words_array=["Python","Class","Technology","Language","Coding"]

def random_word(array):
    
    """selects a random word from a List and changes 
                all char in the word with a '*' """
    
    word = random.choice(array) 
     
    for char in word:
        
        encripted_random_word = print(char.replace(char," _ "), end='')
     
    return encripted_random_word

random_word(words_array)