def add_digits(number):
    add=0
    while number!=0:
        digit = number%10
        add+=digit
        number//=10
    return add
num = int(input('numero a procesar: '))
while num!=0:
    print(f'suma: {add_digits(num)}')
    num = int(input('numero a procesar: '))

#ej1

#Definicon de finciomes

def most(a,b):
    if(a>b):
        return a
    else:
        return b

def  least(a,b):
    if (a<b):
        return a
    else:
        return b

x=int(input('Un numero: '))
y=int(input('otro numero: '))
print(most(x-3,least(x+2,y-5)))


    

