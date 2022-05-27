 #hacer un programa para realizar el muestreo de 10 personas ´para determinar
 #el promedio de peso de los niños,jovenes,adultos y viejos que existen
 #en su zona hbitacional.
 # se determina las categorias con base en la siguiente tabla:
 #CATEGORIA     EDAD
 #NIÑOS         0-12
 #jovenes       13-29
 #ADULTO        30-59
 #VIEJOS        60 en adelante
 

pesoNiños=0
pesoJovenes=0
pesoAdultos=0
pesoViejos=0
niños=0
jovenes=0
adultos=0
viejos=0

for i in range(10):
    print("digite los datos de la persona: ", str(i))
    edad=int(input("digite su edad: "))
    peso=int(input("digite su peso: "))
    if edad<=12:
        pesoNiños=pesoNiños+peso
        niños=niños+1
    elif edad<=29:
            pesoJovenes=pesoJovenes+peso
            jovenes=jovenes+1
    elif edad<=59:
            pesoAdultos=pesoAdultos+peso
            adultos=adultos+1
    else:
            pesoViejos=pesoViejos+peso
            viejos=viejos+1
            
promedioNiños=pesoNiños/niños
promedioJovenes=pesoJovenes/jovenes
promedioAdultos=pesoAdultos/adultos
promedioViejos=pesoViejos/viejos

print("el promedio del peso de los niños es: ", promedioNiños)
print("el promedio del peso de los jovenes es: ", promedioJovenes)
print("el promedio del peso de los adultos es: ", promedioAdultos)
print("el promedio del peso de los viejos es: ", promedioViejos)
