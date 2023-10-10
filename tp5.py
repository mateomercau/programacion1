import math
# 1.	Escribir una función que, dado un número de DNI, 
# retorne True si el número es válido y 
# False si no lo es. Para que un número de DNI sea válido 
# debe tener entre 7 y 8 dígitos
def validate(dni):
    long = len(dni)
    if (long<9 and long>6):
        return True
    else:
        return False
num_dni = input("Ingresar el numero del dni, sin puntos: ")
num_dni
print(validate(num_dni))
# 2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. 
# Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.
def long_last_word(chains):
    chains = chains.strip()
    words = chains.split()
    if not words:
        return 0
    else:
        return len(words[-1])

#Main
chains = input("Ingrese el string: ")
result = long_last_word(chains)
print(result)
#Ejercicio 3
def get_identifier(full_name, dni):
    #Separo el nombre del apellido
    names = full_name.split()
    last_name = names[-1]
    # Obtengo el primero nombre
    first_name = names[0]
    # Obtengo los 3 digitos del dni
    first_three_digits_dni = str(dni)[:3]
    # Creo el identificador
    identifier = f"{first_name.capitalize()}{len(last_name)}{first_three_digits_dni}"
    return identifier

def get_valid_dni():
    while True:
        dni = input("Ingrese el número de DNI (7 u 8 dígitos): ")
        if len(dni) in [7, 8] and dni.isdigit():
            return int(dni)
        else:
            print("El número de DNI debe tener 7 u 8 dígitos. Intente nuevamente.")

while True:
    full_name = input("Ingrese el nombre completo del socio (o dejar vacío para finalizar): ")
    if not full_name:
        break
    dni = get_valid_dni()
    identifier = get_identifier(full_name, dni)
    print(f"ID -> {identifier}")
#Ejercicio 4
def is_multiple(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if is_multiple(num1, num2):
    print(f"Uno de los números es múltiplo del otro.")
else:
    print("Ninguno de los números es múltiplo del otro.")
#Ejercicio 5
def calculate_daily_average(max_temp, min_temp):
    return (max_temp + min_temp) / 2

def get_average_temperature():
    num_days = int(input("Enter the number of days: "))
    for day in range(1, num_days + 1):
        max_temp = float(input(f"Ingrese la temperatura máxima del día {day}: "))
        min_temp = float(input(f"Ingrese la temperatura mínima del día {day}: "))

        daily_average = calculate_daily_average(max_temp, min_temp)
        print(f"La temperatura media del día {day} es: {daily_average}°C")

get_average_temperature()

#Ejercicio 6
def add_spaces(text):
    text_with_spaces = ' '.join(text)
    return text_with_spaces

user_input = input("Ingrese un texto: ")

resulting_text = add_spaces(user_input)

print(f"Texto con espacios adicionales: {resulting_text}")

#Ejercicio 7
def get_max_min(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    return max_value, min_value

def main():
    num_list = []
    num_count = int(input("Ingrese cuántos números desea agregar a la lista: "))
    for i in range(num_count):
        num = float(input(f"Ingrese el número {i+1}: "))
        num_list.append(num)
    max_value, min_value = get_max_min(num_list)
    print(f"El valor máximo es: {max_value}")
    print(f"El valor mínimo es: {min_value}")

if __name__ == "__main__":
    main()

#Ejercicio 8

def calculate_area_perimeter(radius):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return area, perimeter
def main():
    radius = float(input("Ingrese el radio de la circunferencia: "))
    area, perimeter = calculate_area_perimeter(radius)
    print(f"El área de la circunferencia es: {area}")
    print(f"El perímetro de la circunferencia es: {perimeter}")

if __name__ == "__main__":
    main()

#Ejercicio 9
def login(username, password, attempts):
    if username == "usuario1" and password == "asdasd":
        return True, attempts
    else:
        attempts += 1
        return False, attempts

def main():
    attempts = 0
    while attempts < 3:
        username = input("Ingrese nombre de usuario: ")
        password = input("Ingrese contraseña: ")
        success, attempts = login(username, password, attempts)
        if success:
            print("¡Inicio de sesión exitoso!")
            break
        else:
            print("Credenciales incorrectas. Inténtelo nuevamente.")
            
    if attempts == 3:
        print("Se han agotado los intentos. Por favor, inténtelo más tarde.")

if __name__ == "__main__":
    main()

#Ejercicio 10
def apply_discounts(cart, discounts):
    final_price = 0

    for product, price in cart.items():
        if product in discounts:
            discounted_price = price * (1 - discounts[product] / 100)
            final_price += discounted_price
        else:
            final_price += price
    return final_price
# Definimos un diccionario con los productos y su precio
cart = {
    "product1": 100,
    "product2": 50,
    "product3": 75
}
# Definimos un diccionario con los descuentos por producto
discounts = {
    "product1": 10,
    "product3": 20
}

# Aplicamos los descuentos al carrito y obtenemos el precio final
final_price = apply_discounts(cart, discounts)

print(f"The final price of the purchase is: {final_price}")

#Ejercicio 11
def apply_function_to_list(func, lst):
    # Aplica la función dada a cada elemento de la lista y retorna una nueva lista con los resultados.
    return [func(element) for element in lst]

# Define una función que suma 10 a un número
def suma_10(numero):
    return numero + 10

# Crea una lista de números
numeros = [11, 22, 33, 44, 55]
# Aplica la función suma_10 a cada elemento de la lista
resultados = apply_function_to_list(suma_10, numeros)
print(resultados)

#Ejercicio 12
def word_lengths(sentence):

    words = sentence.split()
    length_dict = {word: len(word) for word in words}
    return length_dict


frase_ejemplo = input("Ingrese una frase: ")
resultado = word_lengths(frase_ejemplo)
print(resultado)

#Ejercicio 13
def calculate_modulus(vector):
    modulus = math.sqrt(sum(component**2 for component in vector))
    return modulus
vector_example = [3, 4]

modulus = calculate_modulus(vector_example)

print(f"El módulo del vector {vector_example} es: {modulus}")

#Ejercicio 14

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
# Pedir al usuario que ingrese un número
user_input = int(input("Ingrese un número entero: "))
# Verificar si es primo usando la función is_prime
if is_prime(user_input):
    print(f"El número {user_input} es primo.")
else:
    print(f"El número {user_input} no es primo.")

#Ejercicio 15
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

def main():
    total_numeros = 0
    while True:
        user_input = input("Ingrese un número (o 'q' para salir): ")
        if user_input == 'q':
            break
        if user_input.isdigit():
            num = int(user_input)
            total_numeros += 1
            if num < 0:
                print("No se puede calcular el factorial de un número negativo.")
            else:
                print(f"El factorial de {num} es: {factorial(num)}")
        else:
            print("Entrada no válida. Ingrese un número entero positivo o 'q' para salir.")
    print(f"Total de números ingresados: {total_numeros}")
if __name__ == "__main__":
    main()


#Ejercicio 16
def calculate_frequency(number, digit):
    return str(number).count(str(digit))

def main():
    number = int(input("Ingrese un numero entero: "))
    digit = int(input("Ingrese un digito: "))

    frequency = calculate_frequency(number, digit)

    print(f"El digito {digit} aparece {frequency} veces en el numero  {number}.")

if __name__ == "__main__":
    main()

#Ejercicio 17

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_digits(number):
    
    return sum(int(digit) for digit in str(number))

def digit_frequency(number, digit):
    
    return str(number).count(str(digit))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

largest_prime = float('-inf')

while True:
    user_input = input("Ingrese un número primo (o cualquier valor no numérico para terminar): ")

    if not user_input.isdigit():
        break

    number = int(user_input)

    if is_prime(number):
        largest_prime = max(largest_prime, number)

        digit_sum = sum_digits(number)

        user_digit = int(input("Ingrese un dígito para contar su frecuencia: "))
        frequency = digit_frequency(number, user_digit)

        print(f"La suma de los dígitos es: {digit_sum}")
        print(f"La frecuencia de {user_digit} en el número es: {frequency}")
    else:
        print("El número ingresado no es primo.")
if largest_prime > 1:
    print(f"El factorial del mayor número ingresado ({largest_prime}) es: {factorial(largest_prime)}")
else:
    print("No se ingresaron números primos o no se ingresó ningún número mayor que 1.")
