import random
#
#  Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el
# programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un
# signo de interrogación al final. El programa mostrará después la frase final.


while True:
    phrase=input('ingrese una palabra o frase: ')
    long=len(phrase)
    aux_phrase=phrase.replace(" ","")
    if not aux_phrase.isalpha():
        print('ingrese solo letras no numeros')
        continue
    else:
        if long == 4:
            phrase=phrase +'!'
        else:
            phrase=phrase +'?'
        break
        

print(phrase)


# Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra
# por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego.

words=["perro","gato","pez","pollo"]

random=random.randint(1,4)
word=words[random]
long=len(word)
while True:

    
    


