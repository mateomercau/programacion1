#ej 1 y 2
anos=int(input('escriba los años de la computadora: '))
if (anos < 0):
    print('dato ingresado invalido')
elif (anos<= 2):
    print('computador es nuevo')
else:
     print('computador es viejo')

# #ej 3
nombre1=(str(input('ingrse el primer nombre: ')))
nombre2=(str(input('ingrse el segundo  nombre: ')))

if (nombre1[0].lower() == nombre2[0].lower()):
    print('coincidencia')
else:
    print('no hay coincidencia')

# #ej4
candidatos=['a','b','c']
voto=input('vote por un partido a:partido rojo,b:partido verdad,c:partido azul: ')
if (voto.lower()== candidatos[0]):
    print('Usted ha votado por el partido rojo')
elif (voto.lower()== candidatos[1]):
    print('Usted ha votado por el partido verde')
elif (voto.lower()== candidatos[2]):
    print('Usted ha votado por el partido azul')
else:
    print('valor incorrecto')
    

#ej5

letra=str(input('escriba una letra: '))
if (len(letra) > 1):
    print('no se puede ingresar el dato')

vocales=['a', 'e', 'i','o','u']

if (letra.lower() in vocales):
    print('es vocal')

#ej6
ano=int(input('ingrse el año: '))
if (ano %4 ==0 ):
    print('es bisiesto')
else:
    print ('no es bisiesto')

#ej7

#solicita tres numeros 

a=int(input('ingrse el primer numero: '))
b=int(input('ingrse el primer numero: '))
c=int(input('ingrse el primer numero: '))
#saca el menor numero
if a <= b and a <= c:
    menor_numero = a
elif b <= a and b <= c:
    menor_numero = b
else:
    menor_numero = c

print (f'El menor numero es {menor_numero}')


#ej8

#pide nombre y contraseña

nombre=str(input('ingrse el nombre de usuario: '))
contrasena=str(input('ingrese la contraseña: '))
#si el usuario y contraseña son correctos accede 
if (nombre == 'Gwenevere' and contrasena == 'excalibur' ):
    print('Usuario y contraseña correctos. Puede ingresar a Camelot')
else:
    print('Acceso denegado')

#ej9
#ingreso de datos 
nombre = input('Ingrese su nombre: ')
sexo = input('Ingrese su sexo (M/F): ').upper()

if ((sexo.lower() == 'f' and nombre.lower() < 'm' ) or (sexo.lower() == 'm' and nombre[0].lower() > 'n' )):
    print('calse A')
else: 
    print('calse B')


#ej10

edad=int(input('ingrese su edad: '))
if (edad < 4):
    print('entrada gratiz')
elif (edad < 18):
    print ('debe pagar 500$')
else:
    print ('debe pagar 1000$')

#ej11

piza=str(input('desea pizza vegetariana? S/N: ')).upper()

if (piza == 'S'):
    print('ingredientes: ')
    print ('1. pimiento ')
    print('2. tofu')
    ingrediente=int(input('su respuesta (1/2): '))
    if (ingrediente == 1):
        ing ='pimiento'
    elif (ingrediente == 2 ):
        ing ='tofu'
    else:
        print ('ingrediente invalido')
    print(f'a elegido una piza vegetariana')
elif(piza == 'N'):
    print('ingredientes: ')
    print ('1. peperoni ')
    print('2. jamon')
    print('3. salmon')
    ingrediente=int(input('su respuesta (1/2/3): '))
    if (ingrediente == 1):
        ing ='peperoni'
    elif (ingrediente == 2 ):
        ing ='jamon'
    elif (ingrediente == 3):
        ing = 'salmon'
    else:
        print ('ingrediente invalido')
    print(f'a elegido una piza no vegetariana')



print(f'sus ingredientes son: mozxarella, tomate y {ing}')

#ej12

ano_act=int(input('ingrse el año actual: '))
ano_cual=int(input('ingrse un año cualquiera '))

if (ano_act > ano_cual):
    diferencia = ano_act - ano_cual
    print(f'han pasado {diferencia} años desde {ano_cual}')
else:
    diferencia = ano_cual - ano_act
    print(f'faltan {diferencia} años para {ano_cual}')

#ej13

num1=int(input('ingrese el primer numero: '))
num2=int(input('ingrese el segundo numero: '))

if (num1 <= 0 or num2 <= 0):
    print('ingrse un valor positivo no nulo')
else:
    if (num1 > num2):
        mayor = num1
        menor = num2 
    else:
        mayor = num2
        menor = num1
    if (mayor % menor == 0):
        print(f'el numero {mayor} es multiplo de {menor}')
    else:
        print(f'el numero {mayor} no es multiplo de {menor}')

#ej14
 
print("ingrese los valores de la siguiente ecuacion: a x + b = 0")
a = int(input('ingrse el  valor de a: '))
b = int(input('ingrse el valor de b: '))


if (a == 0):
    if (b == 0):
        print('tiene soluciones infinitas')
    else:
        print('no tiene solucion')
else:
    resultado=((-b)/a)
    if (resultado == -0.0):
        print('el resultado es 0')
    else:
        print (f'el resultado es {resultado}')

#ej15

opcion = input('desea calcular el area de un triangulo o de un circulo T/C: ').upper()

if (opcion == 'T'):
    base = int(input('ingrese la base del triangulo: '))
    altura = int(input('ingrese la altura del triangulo: '))
    area=((base * altura)/2)
    print(f'el area del triangulo es: {area}')
elif (opcion == 'C'):
    radio = int(input('ingrese el radio del circulo: '))
    area= math.pi * radio**2
    print(f'el area del triangulo es: {area}')

#ej16

a=int(input('ingrese el primer valor: '))
b=int(input('ingrse el segundo valor: '))
print('operaciones:')
print('1.suma')
print('2.multiplicacion')
print('3.resta')
print('4.division')

operacion=int(input('ingrse operacion: '))

if (operacion == 1):
    resultado = a + b
elif (operacion == 2):
    resultado = a * b
elif (operacion == 3):
    resultado = a - b
elif (operacion == 4):

    resultado = a/b
else:
    print('ingrese una operacion valida')

print(f'rl resultado es {resultado}')

#ej17

dia=input('ingrese un dia de la semana: ').lower()

if (dia == 'lunes'):
    print('hoy es lunes')
elif (dia == 'viernes'):
    print('hoy es viernes')
elif ( dia == 'sabado' or dia == 'domingo'):
    print('hoy es sabado o domingo')
else:
    print('no es ni lunes ni viernes ni sabado o domingo')

#ej18

horas=int(input('ingrese horas trabajadas en el mes: '))
salario=int(input('ingrese el salario por hora: '))


if (horas > 48):
    extra = horas - 48
    total=(48*salario) + (((salario*0.10)+salario)*extra)
else:
    total=(salario * horas)

print(f'el salario total es: {total}')

#ej19

lap=int(input('ingrese la cantidad de lapices: '))
if (lap >= 1000):
    descuento= 60 - (60*0.7)
    total= lap*descuento
else:
    total=lap*60
print(f'el precio final es {total}')

#ej20

nota1=int(input('ingrse la nota numero 1: '))
nota2=int(input('ingrse la nota numero 2: '))
nota3=int(input('ingrse la nota numero 3: '))
nota4=int(input('ingrse la nota numero 4: '))

promedio = (nota1+nota2+nota3+nota4)/4

if (promedio >= 6 ):
    print('aprobado')
else:
    print('desaprobado')




    








    
        






    
