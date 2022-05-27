#hacer un programa para un supermercado en donde el cajero captura los precios de los
#articulos que los clientes compran e indica a cada cliente cual es el monto de lo que
#deben pagar. al final del dia le indica a su supervisor cuanto fue lo que cobro
#en total a los 5 clientes que pasaron por la caja.
Totalclientes=0
for i in range(5):
    articulos=int(input("digite cantida de  articulos a comprar: "))
    sumaprecio=0
    for j in range(articulos):
          precio=float(input("ingrese el precio del articulo, para el cliente: " + str(i) + ": " ))
          sumaprecio=sumaprecio+precio
          print("el valor a pagar del cliente " + str(i) + " es: " + str(sumaprecio))
          Totalclientes=Totalclientes+sumaprecio
print("**************")
print("el valor que pago todos los clientes fue: ", Totalclientes)
