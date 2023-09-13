
""" 
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
    print('*'*i)"""

#ej7

for j in range(1,11):
    for i in range(1,11):
        print(f'{j} x {i} = {j*i}'end='')


    








    