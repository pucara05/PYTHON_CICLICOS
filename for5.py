 #hacer un programa que calcule el promedio de un alumno que tiene
 #7 calificaciones
suma=0
nombre=input("digite su nombre: ")
for i in range(7):
    nota=float(input("digite la nota " + str(i) + ": "))
    suma=suma+nota
promedio=suma/7
print("el promedio del estudiante ", nombre, " es: ", round(promedio,2))
