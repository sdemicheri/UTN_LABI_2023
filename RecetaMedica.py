def recetaMedica (fechaEmision,doctor,nombre,fecha,clinica,medicamento,medicamento2,medicamento3):
    print("________________________________________________________________________________")
    print("|Fecha de emision de la receta🗓️: ", fechaEmision                             )
    print("|Nombre del especialista a cargo👨🏽‍⚕️: ", doctor                                 )
    print("|Nombre Completo del Paciente🗒️: ", nombre                                   )
    print("|Fecha de nacimiento del paciete👶🏽: ", fecha                                  )
    print("|Direccion del establecimiento médico🏥 :", clinica                           )
    print("|Nombre del medicamento recetado💊💊: ", medicamento                         )
    print("|Dosis en la que debe ser consumido el medicamento🤒: ", medicamento2         )
    print("|Intrucciones de uso🗒️💊: ", medicamento3                                     )
    print("|_____________________________________________________________________________")


fechaEmision =(input ("Ingrese la fecha actual:"))
doctor = (input("Ingrese nombre del doctor a cargo:"))
nombre = (input("Ingrese el Nombre y Apellido del paciente:"))
fecha= (input("Ingrese su fecha de nacimiento:"))
clinica = (input("Ingrese la dirección de la clinica:"))
medicamento = (input("Ingrese el nombre del medicamento:"))
medicamento2 = (input("Ingrese la dosis que debe consumir el paciente: "))
medicamento3 = (input("Ingrese las instrucciones de uso del medicamento:"))

print("|________________________________________________________________________________")
print("   Su receta ha sido creada con exito...👩🏽‍💻🙌🎉")

recetaMedica(fechaEmision,doctor,nombre,fecha,clinica,medicamento,medicamento2,medicamento3)


def proximoTurno (fechaEmision,doctor, clinica, nombre, documento, mutual, turno):
    print("________________________________________________________________________________")
    print("|Fecha actual🗓️:                                                                |", fechaEmision)
    print("|Nombre del especialista a cargo👨🏽‍⚕️:                                             |", doctor)
    print("|Direccion del establecimiento medico🏥:                                        |", clinica)
    print("|Nombre completo del paciente🗒️:                                                |", nombre)
    print("|D.N.I del paciente📋:                                                          |", documento)
    print("|Ingrese la obra social del paciente👩🏽‍💻:                                         |", mutual)
    print("|Ingrese la fecha del proximo turno programado🗓️:                               |", turno)
    print("|________________________________________________________________________________")


fechaEmision = (input("Ingrese la fecha actual:"))
doctor = input ("Ingrese el nombre del doctor a cargo👨🏽‍⚕️:")
clinica = (input("Ingrese la dirección de la clinica:"))
nombre = (input("Ingrese el Nombre y Apellido del paciente:"))
documento = (input("Ingrese el DNI del paciente:"))
mutual = (input("Ingrese la obra social del paciente:"))
turno = (input("Ingrese la fecha del proximo turno programado:"))
print("|________________________________________________________________________________")
print("   Su proximo tuno fue registrado con exito...👨🏽‍⚕️🙌💊")

proximoTurno (fechaEmision,doctor,clinica, nombre, documento, mutual, turno)



