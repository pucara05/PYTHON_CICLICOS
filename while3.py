 # obtener el promedio de calificaciones de un grupo de n estudiantes
#variable notas es variable acumuladora
notas=0
#variable estudiantes  variable contador
estudiantes=0
continuar="s"

while continuar.lower()=="s":
    nota=float(input("digite la nota del estudiante: "))
    notas=notas+nota
    estudiantes=estudiantes+1

    continuar=input("digta s si quiere continuar agregando notas de estudiantes: , o " " cualquier caracter para finalizar: ")

    promedio=notas/estudiantes
    print("el promedio de los ", estudiantes, " estudiantes es: ", promedio)
    
