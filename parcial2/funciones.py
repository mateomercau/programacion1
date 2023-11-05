"""Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.

Te ha contratado a ti para que desarrolles un programa que detecte si un humano es mutante basándose en su secuencia de ADN.

Para eso te ha pedido crear un programa con un método o función booleana, llamada is_mutant(dna), que recibe como parámetro un arreglo de Strings que representan cada fila de una matriz 6x6 con la secuencia de ADN.

Las letras de los Strings solo pueden ser: A,T,C,G; las cuales representan cada base nitrogenada del ADN.

Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras iguales, estas pueden aparecer de forma oblicua, horizontal o vertical.
En el caso de la matriz de la derecha,

adn = [‘ATGCGA’,’CAGTGC’,’TTATGT’,’AGAAGG’,’CCCCTA’,’TCACTG’]

la función devolverá True.

Desarrolla el algoritmo de forma más eficiente posible.

El ingreso de los valores de la matriz debe ser pedido por teclado. Ten en cuenta casos para que sea mutante y casos en los que no lo sea.

Una vez cargada correctamente la misma (esto debe verificarse), aplique la función que verifica si hay presencia de genes mutantes o no y mostrar el resultado por pantalla al usuario.

Subir a Github el proyecto con los casos de prueba."""
#funcion para saber si es mutante
def is_mutant(dna):
    if find_horizontal(dna,'AAAA')or find_horizontal(dna,'GGGG') or find_horizontal(dna,'CCCC')or find_horizontal(dna,'TTTT'):
        return True
    elif find_vertical(dna,'AAAA')or find_vertical(dna,'GGGG') or find_vertical(dna,'CCCC')or find_vertical(dna,'TTTT'): 
        return True
    elif find_diagonal(dna,'AAAA')or find_diagonal(dna,'GGGG') or find_diagonal(dna,'CCCC')or find_diagonal(dna,'TTTT'): 
        return True
    else:
        return False
    
#funcion que compara palabras en horizontal

def find_horizontal(array, word):
    appearances = 0
    for row in array:
        appearances += row.count(word)

    if appearances >= 1:
        return True
    else:
        return False

#funcion que compara palabras en vertical

def find_vertical(array,word):
    appearances = 0
    for col in range(len(array[0])):
        column_aux="".join(row[col]for row in array)
        appearances+= column_aux.count(word)

    if appearances >= 1:
        return True
    else:
        return False
    
#funcion que compara palabras en diagonal
        
def find_diagonal(array,word):
    appearances = 0
    #de izquierda  a derecha
    
    for i in range(len(array)-1):
        diagonal_aux="".join(array[j][i+j]for j in range(len(array) - i))
        appearances+= diagonal_aux.count(word)

    #de derecha a izquierda
    for i in range(len(array)-1):
        diagonal_aux="".join(array[j][len(array[0])-i-j-1]for j in range(len(array) - i))
        appearances+= diagonal_aux.count(word)


    if appearances >= 1:
        return True
    else:
        return False


#funcion llenar arreglo y valida si es correcto
def data_entery(array):
    while len(array)<6:
        row=input("ingrese una fila de la matriz, debe ser 6 letras y solo puede ingresar las letras A,T,C,G: ").upper()
        if len(row) == 6 and all(i in "ATCG" for i in row):
            array.append(row)
        else:
            print("ingreso invalido")
    return array

#ejemplo de uso
print('ejemplo de uso:')
dna1=[]
data_entery(dna1)
print(f"adn={dna1}") 
if is_mutant(dna1):
    print("es mutante")
else:
    print('no es mutante')

#prueba1
print("prueba 1:")
dna2 = ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
print(f"adn={dna2}") 


if is_mutant(dna2):
    print("es mutante")
else:
    print('no es mutante')

print("prueba 2:")
dna3 = ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG']
print(f"adn={dna3}") 


if is_mutant(dna3):
    print("es mutante")
else:
    print('no es mutante')











    




    



    

