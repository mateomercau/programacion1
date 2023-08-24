"""# #ej 1 y 2
# anos=int(input('escriba los años de la computadora: '))
# if (anos < 0):
#     print('dato ingresado invalido')
# elif (anos<= 2):
#     print('computador es nuevo')
# else:
#      print('computador es viejo')

# #ej 3
# nombre1=(str(input('ingrse el primer nombre: ')))
# nombre2=(str(input('ingrse el segundo  nombre: ')))

# if (nombre1[0].lower() == nombre2[0].lower()):
#     print('coincidencia')
# else:
#     print('no hay coincidencia')

# #ej4
# candidatos=[a,b,c]
# voto=input('vote por un partido a:partido rojo,b:partido verdad,c:partido azul')
# if (voto.lower()== candidatos[0]):
#     print('Usted ha votado por el partido rojo')
# elif (voto.lower()== candidatos[1]):
#     print('Usted ha votado por el partido verde')
# elif (voto.lower()== candidatos[2]):
#     print('Usted ha votado por el partido azul')
# else:
#     print('valor incorrecto')
    

#ej5

# letra=str(input('escriba una letra: '))
# if (len(letra) > 1):
#     print('no se puede ingresar el dato')

# vocales=['a', 'e', 'i','o','u']

# if (letra.lower() in vocales):
#     print('es vocal')

#ej6
# ano=int(input('ingrse el año: '))
# if (ano %4 ==0 ):
#     print('es bisiesto')
# else:
#     print ('no es bisiesto')

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
sexo = input('Ingrese su sexo (M/F): ')

if ((sexo.lower == 'F' and nombre[0].lower() < 'm' ) or (sexo.lower == 'm' and nombre[0].lower() > 'n' )):
    print('calse A')
else: 
    print('calse B')"""

#ej10




    
