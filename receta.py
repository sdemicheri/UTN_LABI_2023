## GUÍA 3 - Sistema que emita recetas médicas y el próximo turno.
## DATOS que debe contener la receta médica: 
## •Nombre del paciente
## •Fecha de nacimiento 
## •Dirección de la clínica 
## •Detalles del medicamento recetado (nombre, dosis e instrucciones de uso)

## El medico/a debe ingresar en el sistema los siguientes datos del paciente: 
def datosPaciente(nombre, fecha, clinica ):
    print("\n- Nombre del paciente -\n")
    print(nombre)
    print("\n- Fecha de nacimiento del paciente -\n")
    print(fecha)
    print("\n- Dirección de la clinica -\n")
    print(clinica)


## Datos del medicamento que aparecerá en la receta
def datosMedicamento(medicamento, dosis, instrucciones ):
    print("\n- Nombre del medicamento recetado -\n")
    print(medicamento)
    print("\n- Dosis del medicamento -\n")
    print(dosis)
    print("\n- Instrucciones de la toma del medicamento -\n")
    print(instrucciones)

print("- Por favor, ingrese los siguientes datos que serán cargados en el sistema - ")
nombre = input("Nombre del paciente: ")
fecha= input("Fecha de nacimiento del paciente: ")
clinica = input("Dirección de la clínica: ")
medicamento = input ("Nombre del medicamento: ")
dosis = input ("Dosis del medicamento: ")
instrucciones = input("Instrucciones del medicamento: ")


## Para generar la receta, la secretaria deberá ingresar el nombre del paciente. Si el nombre ingresado coincide con algun nombre que está cargado en el sistema se mostrara la receta.
print("- RECETA -")
nuevoPaciente = str( input("Ingrese el nombre del paciente que desea generar su receta: "))

if nuevoPaciente == nombre :
    print (datosPaciente(nombre, fecha, clinica))
    print (datosMedicamento(medicamento, dosis, instrucciones))
    turno = str(input("¿Desea sacar un turno? (Ingrese S/N en mayuscula dependiendo de su respuesta)"))
    if    turno == "S":
             print("ingrese la fecha y hora acordada con el paciente para el próximo turno")
             proxTurno = input()
             print ( "\nSu próximo turno es: ", proxTurno, datosMedicamento(medicamento, dosis, instrucciones), "\nMuchas gracias por elegir la clinica. Lo esperamos proximamente, que tenga un buen día")
    elif  turno == "N":
             print("\nMuchas gracias por elegir la clinica. Lo esperamos proximamente, que tenga un buen día")
    else :
        print("\nNo ingresó una opción correcta")

else  :
      print("\nEl nombre del paciente que ingresó no se encuentra cargado en el sistema o se encuentra mal escrito.")
    






