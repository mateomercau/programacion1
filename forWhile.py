
"""Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación."""

"""for n in range(0,5):
    print(n)
"""


"""2- Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""

total_pares=0
total_inpares=0
while True:
    pares=0
    inpares=0
    n = int(input('ingrese un numero positivo entero: '))
    if n == 0:
        break

    digitos_pares=0
    digitos_inpares=0
    n2=n
    while n2 > 0 :
        digito= n2%10
        if digito%2 == 0 :
            digitos_pares+=1
        else:
            digitos_inpares+=1
        n2//=10
    pares+=digitos_pares
    inpares+=digitos_inpares
    print(f'digitos pares: {pares}')
    print(f'digitos inpares: {inpares}')
    total_pares+=pares
    total_inpares+=inpares

print(f'total de digitos pares: {total_pares}')
print(f'total de digitos inpares: {total_inpares}')







    




