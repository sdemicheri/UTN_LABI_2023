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
nombre = (input("Ingrese su Nombre y Apellido:"))
fecha= (input("Ingrese su fecha de nacimiento:"))
clinica = (input("Ingrese la dirección de la clinica:"))
medicamento = (input("Ingrese el nombre del medicamento:"))
medicamento2 = (input("Ingrese la dosis que debe consumir el paciente: "))
medicamento3 = (input("Ingrese las instrucciones de uso del medicamento:"))


print("Su receta ha sido creada con exito...👩🏽‍💻🙌🎉")

recetaMedica(fechaEmision,doctor,nombre,fecha,clinica,medicamento,medicamento2,medicamento3)



