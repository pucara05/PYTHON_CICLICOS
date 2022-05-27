# hacer un programa que determine cuantos hombres y mujereses se encuentran en un grupo de
#n personas

personas=int(input("digite el numero de personas a evaluar: "))
hombres=0
mujeres=0
for i in range(personas):
    sexo=input("digite 1 para hombre y 2 para mujer: ")
    if sexo=="1":
        hombres=hombres+1
    elif sexo=="2":
            mujeres=mujeres+1
else:
    print("has digitado un numero diferente a 1 o 2 ")
print("la cantida de hombres es: ", hombres)
print("la cantida de mujeres es: ", mujeres)
  
            
    
