 
numeroPaquetes=int(input())
for i in range(numeroPaquetes):
    costoTotal=0
  
   
alto=float(input( ))
ancho=float(input( ))
profundo=float(input( ))

volumen=alto*ancho*profundo
costo=volumen*5
if alto>30:
    volumenPaquete=costo+2000
else:
     if costo>10000:
      costoEnvio=(costo+2000)*0.19
      print(volumen)
      print(costo)

costoTotal=costoTotal+numeroPaquetes
print(costoTotal)


