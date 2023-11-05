from funciones import *
#ejemplo de uso
print('ejemplo de uso:')
dna1=[]
data_entery(dna1)
print(f"adn={dna1}") 
if is_mutant(dna1):
    print("es mutante")
else:
    print('no es mutante')

#prueba 1
print("prueba 1:")
dna2 = ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG']
print(f"adn={dna2}") 


if is_mutant(dna2):
    print("es mutante")
else:
    print('no es mutante')

#prueba 2
print("prueba 2:")
dna3 = ['ATGCGA', 'CAGTGC', 'TTATTT', 'AGACGG', 'GCGTCA', 'TCACTG']
print(f"adn={dna3}") 


if is_mutant(dna3):
    print("es mutante")
else:
    print('no es mutante')