 #hacer un programa que imprima los numeros pares hasta de un numero digitado por el usuari
num=int(input("digite un numero: "))

for num in range(num):
    if num%2==0:
        print("el numero ", num, "es par")
else:
    print("no es par ")
        
        
