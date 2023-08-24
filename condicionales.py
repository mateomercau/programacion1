fecha_ing=str(input('ingrse la fecha dia, dd/mm:' ))#lunes, 22/8

fecha = [str( fecha_ing[0:fecha_ing.find(',')]),int(fecha_ing[fecha_ing.find(' ')+1:fecha_ing.find('/')]),int(fecha_ing[fecha_ing.find('/')+1:])]

dias=['lunes','martes','miercoles','jueves','viernes']

if (fecha[1] > 31 or fecha[2] > 12 or not(fecha[0].lower() in dias)):
    print('se produjo un error. ')

# Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
# exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
# que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
# exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
# programa le mostrará el porcentaje de aprobados.
# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
# porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
# que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.


dias_examen = ['lunes','martes','miercoles']

if (fecha[0].lower() in dias_examen):
    isexamen = input('se tomaron examenes? Si/No. ')
    if(isexamen.lower() == 'si'):
        aprobados=int(input('cuantos alumnos aprobaron? '))
        desaprobados=int(input('cuantos alumnos desaprobaron? '))
        total=aprobados + desaprobados
        porc_apr=(aprobados/total)*100
        print(f'el porcentaje de aprobados es: {porc_apr}%')

if (fecha[0] == dias[3]):
    asistencia=float(input('ingrese el porcentaje de asistencia: '))
    if(asistencia > 50.0):
        print('asistio la mayoria')
    else:
        print('no asistio la mayoria')

# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
# mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
# la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
# imprimir el ingreso total en $.

if(fecha[0] == dias[4]):
    if (fecha[1]== 1 and (fecha[2]== 1 or fecha[2]== 7 )):
        print('comienzo de nuevo ciclo')
        cant_alumnos=int(input('ingrese la cantidad de alumnos: '))
        arancel=int(input('ingrese el arancel por alumnos: '))
        ingreso_total = cant_alumnos * arancel
        print(f"El ingreso total es {ingreso_total}$")


 
