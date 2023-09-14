#ej 1 english
x = 1
print("resultado")
while x < 30:
    if x == 4 or x == 6 or x == 10:
        print('Se salto el valor de ' + str(x) + ' de x')
        x += 1
        continue
    
    if x == 15:
        print('Se rompio la ejecucion del bucle cuando valia ' + str(x))
        break
    
    print(str(x))
    x += 1
#ej 1
lines = []


while True:
    line = input("Ingrese una línea (deje en blanco para finalizar): ")
    
  
    if not line:
        break
    

    lines.append(line)


for line in lines:
    print(line.upper())
#ej 2
auxnum=0
auxtotal=0
total=0
while True:
    auxtotal=0
    auxnum=input("Ingrese un valor de deposito o retiro, utilizando el metodo D para deposito y R para retiro: D 100 o R 50 example")
    if(auxnum==""):
        break
    long=len(auxnum)
    if(auxnum[0]=="D" or auxnum[0]=="d"):
        for i in range(2,long,1):
            auxtotal=str(auxtotal)+str(auxnum[i])
            print(auxtotal)
        total=int(total)
        total=int(total)+int(auxtotal)
    if(auxnum[0]=="R" or auxnum[0]=="r"):
        for i in range(2,long,1):
            auxtotal=str(auxtotal)+str(auxnum[i])
            print(auxtotal)
        total=int(total)
        total=int(total)-int(auxtotal)

print(total)
#ej 3
number_count=0
condi=True
def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True
while True :
    number=int(input("Ingrese un numero para saber si es primo e ingrese 0 para finalizar el programa"))
    if (number==0):
        break
    elif(number>1):
        condi=is_prime(number)
        if(condi==True):
            number_count=number_count+1

print(number_count)
#ej 4
number1=int(input("Ingrese el primer año: "))
number2=int(input("Ingrese el segundo año: "))
if (number1>number2):
    bigger=number1
    minus=number2
else:
    bigger=number2
    minus=number1

for i in range (minus,bigger,1):
    if(i % 10 != 0):
        continue
    if (((i % 4 == 0 and i % 100 != 0) or i % 400 == 0)): 
        print(i)

#ej 5
for i in range(0,21,1):
    if(i % 2 != 0):
        continue
    print(i)
#ej 6
numbers=list(range(1, 101))
search=int(input("Ingrese un numero a buscar del 1 al 100"))
for i in numbers:
    if(i==search):
        print("Se encontro!")
        break
#ej 7
while True:
    number=int(input("En que menu desea ingresar? 1 2 o 3, ingrese 0 para salir: "))
    if(number==1):
        print("MENU UNO")
    elif(number==2):
        print("MENU DOS")
    elif(number==3):
        print("MENU TREIS")
    elif(number==0):
        break







        


            
            
            
    