 # hacer un programa que calcule el promedio de un alumno que tiene
 #3 calificaciones de quices, 4 calificaciones de trabajos y 2 calificaciones
 #de parciales


quices=0
trabajos=0
parciales=0
nombre=input("digite su nombre: ")

for i in range(0,3):
    nota=float(input("digite la nota de quiz " + str(i) + ": "))
    quices=quices+nota
for j in range(4):
    nota=float(input("digite la nota de trabajo " + str(j) + ": "))
    trabajos=trabajos+nota
for z in range(2):
    nota=float(input("digite la nota de parcial " + str(z) + ": "))
    parciales=parciales+nota
promQuices=quices/3
promTrabajos=trabajos/4
promParciales=parciales/2

promedio=(promQuices+promTrabajos+promParciales)/3
print("el promedio del estudiante es: ", nombre, " es: ", round(promedio,2))

    
    
