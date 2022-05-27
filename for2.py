 #hacer un programa que pida la cantidad de numeros a sumar
suma=0
numero=int(input("digite el numero al cual  le queremos obtener la sumatoria: "))
i=1
for i in range(numero+1):
    suma=suma+i
print()
print("el resultado de la sumatoria es: ", suma)
