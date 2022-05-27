# ejemplo pratico de una bandera tipo string o cadena

contagio_valido="no"
paciente="daniel"

if contagio_valido=="no":
    print("el paciente " + paciente + "aun no se ha realizado su prueba para validar " +
          "si se encuentra contagiado, se recomienda aplicar la prueba pcr")
    print("aplicando prueba...")
    contagio_valido="pendiente"

    if contagio_valido=="pendiente":
        print(paciente + ", por favor valide en su correo el resultado de la prueba")
        contagio_valido="si"

        if contagio_valido=="si":
            print(paciente + ", de acuerdo a su resultado, por favor mantegase alejado de las personas")
            
          
