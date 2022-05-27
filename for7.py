#obtener el promedio de calificaciones de un grupo de n estudiantes
#utiliza el for
estudiantes=0
notas=0
for i in range(estudiantes+1):
    estudiantes=int(input("digite el numero de estudiantes: "))
    nota=float(input("digite la nota del estudiantes: "))
    notas=notas+nota
    promedio=nota/estudiantes
print("su promedio es: ", promedio)
