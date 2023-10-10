"""#ej 10
def aply_discount(shopping_cart, discounts):
    final_price = 0
    for product, price in shopping_cart.items():
        if product in discounts:
            discount=discounts[product]
            price_discount=price - (price * (discount/100))
            final_price+=price_discount
        else:
            final_price+=price
        
    return final_price
    
shopping_cart = {'producto1': 100,'producto2': 50,'producto3': 75, }

discounts = {'producto1': 10, 'producto3':20}
precio_total = aply_discount(shopping_cart, discounts)
print(f'Precio total con descuento: {precio_total}')

#12	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def count_length_word(phrase):
    words = phrase.split()
    result = {}
    for word in words:
        result[word]=len(word)
    return result

phrase =input('ingrese una frase: ')
result=count_length_word(phrase)
print(result)

#13	Escribir una función que calcule el módulo de un vector.
import math
def calculate_module(vector):
    sum=0
    for component in vector:
        sum += component ** 2
    module = math.sqrt(sum)
    return module

vector = [3, 4]  # Un vector [3, 4] tiene una magnitud de 5 (es un triángulo rectángulo)
modulo = calculate_module(vector)
print(f"El módulo del vector {vector} es: {modulo}")

#15	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar,
#  la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

def factorial(number):
    result=1
    for i in range(1,number + 1):
        result*= i
    return result
    

total_numbers = 0
while True:
    numbers=int(input('ingrese numeros o 0 para salir: '))
    if numbers == 0:
        break
    elif numbers<0:
        print("El factoral no esta defenido para numeros negativos")
    else:
        fact=factorial(numbers)
        print(f"El factorial de {numbers} es {fact}")
        total_numbers+=1

print(f"total de numeros ingresados : {total_numbers}")"""

#ej16	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.
def digits(number,digits):
    appearances=number.count(digits)
    return appearances

number=input('ingrese un numero: ')
digit=input('ingrese un digito:')
print(f'el digito {digit} aparece {digits(number,digit)} veces ')








