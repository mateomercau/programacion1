# 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
# Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
list_numbers=[]
while True:
    number=int(input("ingrese un numero o 0 para terminar: "))
    if number == 0:
        break
    list_numbers.append(number)

print(list_numbers)

# 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

if len(list_numbers)>0:
    number=int(input("ingrese un numero para eliminarlo de la lista: "))
    if number in list_numbers:
        list_numbers.remove(number)
        print(f'se elimino la primera ocurrencia de {number}')
    else:
        print(f"el numero {number} no esta en la lista")
print(list_numbers)

#3.	Imprimir la sumatoria de todos los números de la lista.
sum_numbers=sum(list_numbers)
print(f"la suma de los numeros es: {sum_numbers}")

# 4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original,
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

number=int(input("ingrese un numero: "))
list_numbers_min=[]
for element in list_numbers:
    if element < number:
        list_numbers_min.append(element)

for element in list_numbers_min:
    print(element,",")

#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un
#  número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original 
# es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]
frequency_list =[(num,list_numbers.count(num))for num in set(list_numbers)]
print("Lista de tuplas (elemento, frecuencia):")
print(frequency_list)
    


