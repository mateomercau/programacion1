

word=input('ingrese una palabra: ')

for i in range(10):
    print(word) 

#ej2 

age=int(input('ingrese su edad: '))

for i in range(age):
    print(i+1)

#ej3 

num=int(input('ingrse un numero  entero positivo: '))
 

for i in range(1, num + 1, 2):
    if i < num:
        print(f'{i}, ', end='')
    else:
        print(i)
print('')

#ej4

num=int(input('ingrse un numero positivo: '))

for i in range(num,0,-1):
    if i > 1:
        print(f'{i}, ', end='')
    else:
        print(i)


#ej5

amount=int(input('ingrese cantiadad a invertir: '))
interest=float(input('ingrese el interes anual: '))
years=int(input('ingrese la cantidad de años: '))

for i in range(1,years+1):
    amount=amount+(amount*(interest/100))
    print(f'el ano {i} se gano: {amount}')

#ej6

num=int(input('ingrese la altura del truangulo: '))

for i in range(1,num+1):
    print('*'*i)

#ej7

for j in range(1,11):
    for i in range(1,11):
        print(f'{j} x {i} = {j*i}')

#ej8 HACER!!!!!!!!!!!!!!!!!!!!!!!

num = int(input("Ingrese un numero entero: "))
val = 1


for i in range(1, num + 1, 2):
 
    for j in range(i, 0, -2):
        print(j, end=' ')
        val = j
  

#ej9

pasword=input("cree una contraseña: ")
pasword_entered=""
while(pasword_entered != pasword):
    pasword_entered=input('ingrese la contraseña: ')
    if pasword_entered != pasword:
        print('contraseña incorrecta')
        

#ej10

num=int(input('ingrese un numero entero: '))
if num <= 1:
    prime = False
else:
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime=False
            break

if prime:
    print(f'el numero {num} es primo')
else:
    print(f'el numero {num} no es primo')

#11
word=input('ingrese una palabara: ')
long=len(word)
for i in range(long,0,-1):
    print(word[i-1])

#12

phrase=input('ingrese una frase: ')
letter=input('ingrese una letra: ')
long=len(phrase)
counter=0
for i in range(0,long,1):
    if (letter == phrase[i]):
        counter+=1
print(f'la letra {letter} aparece {counter} veces')

#ej13
word=""
while word!="salir":
    word=input('ingrese una palabra o ingrese "salir" : ')
    if word!="salir":
        print(word)
    else:
        break

#ej14
num1=int(input("Ingrese el primer numero entero: "))
num2=int(input("Ingrese el segundo numero entero: "))


for i in range(num1,num2+1):
    if (i%2==0 or i == 0):
        print(f'{i} es par')
    else:
        print(f'{i} es inpar')

#ej15

num=int(input("Ingrese un numero entero mayor que cero: "))

if num > 0:
    print(f'los divisores de {num} son: ')
    for i in range(1,num+1):
        if num%i==0:
            print(i)

#ej16

numbers=int(input('ingrese la cantidad de numeros a ingresar: '))
negative_numbers=0
for i in range(1,numbers+1):
    num=int(input(f'ingrese el numero {i}: '))
    if num<0:
        negative_numbers+=1
print(f'se introdujeron {negative_numbers} numeros negativos')

#ej17

phrase=input('ingrese una frase').lower()

vowels='aeiou'
vowels_select= set()

for i in phrase:
    if i in vowels and i not in vowels_select:
        vowels_select.add(i)

print(f"las vocales de la frase son: {vowels_select}")

#ej18
fib=[0,1]

for i in range(2,10):
    next_num= fib[i-1] + fib[i-2]
    fib.append(next_num)
for i in fib:
    print(i)

#ej19 ***

#Ej 19
tope = int(input("Ingrese la cantidad a la que quiere lograr ahorrar: "))
fondo = 0
while fondo<tope:
    deposito = int(input("Ingrese la cantidad que quiere depositar"))
    if deposito<0:
        print("El monto ingresado no puede ser menor que 0")
    else:
        fondo = fondo + deposito
print(f"Los fondos depositados fueron de: {fondo}")

#Ej 20
num = 1
acumulador = 0
while num!= 0:
    num = int(input("Ingrese un numero entero: "))
    acumulador =  num + acumulador
print(f"La sumatoria de los numeros es: {acumulador}")


#Ej 21
mayor = 0
num = 1
while num != 0:
    num = int(input("Ingrese un numero positivo: "))
    if num<0:
        print("El numero ingresado no es positivo")
    else:
        if num>mayor:
            mayor = num
print(f"El numero mayor ingresado es: {mayor}")

#Ej 22
numeros_pares = 0
while True:
    numero = int(input("Ingrese el numero entero positivo(-1 para finalizar el programa)"))
    if numero == -1:
        break
    if numero<=0:
        print("Por favor ingrese un numero positivo")
        continue
    suma = 0
    numtemp = numero
    while numtemp>0:
        suma += numtemp%10
        numtemp //= 10
    print(f"La sumatoria de los digitos del numero {numero} es: {suma}")
    if numero%2 == 0:
        numeros_pares += 1
print(f"La cantidad de numeros pares ingresados es de: {numeros_pares}")
#Ej 23 y 24
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra(0 para salir)"))
    if monto == 0:
        break
    if monto<=0:
        print("Por favor ingrese un monto positivo")
        continue
    total = total + monto
if total > 1000:
    total = total - (total * 0.1)
print(f"El total del monto de las compras es de: {total}")

#Ej 25
facto = int(input("Ingrese el numero que quiere obtener su factorial: "))
factorial=0
if facto == 0:
    factorial = 1
elif facto< 0:
    print("Ingrese un numero positivo")
else:
    factorial = 1
    for i in range(1, facto+1):
        factorial *= i
print(f"El resultado es: {factorial}")


    








    