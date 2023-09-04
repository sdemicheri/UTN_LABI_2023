def recetaMedica(fechaEmisión, nombre, fecha, clinica, medicamento, medicamento2, medicamento3, doctor):
    print("---------------------------------------------")
    print("|                       Fecha: ", fechaEmisión)
    print("|Paciente👪: ", nombre)
    print("|Fecha de nacimiento: ", fecha)
    print("|Clinica🏣:", clinica)
    print("|Medicamento💊:", medicamento)
    print("|Dosis del paciente: ", medicamento2)
    print("|Instrucciónes📋: ", medicamento3)
    print("|Doctor👨‍⚕️: ", doctor)
    print("--------------------------------------------")



fechaEmisión = input("Ingrese la fecha actual:")
nombre = input("Ingrese su nombre y apellido:")
fecha = input("Ingrese su fecha de nacimiento:")
clinica = input("Ingrse la dirección del establecimiento médico:")
medicamento = input("Ingrese el nombre del medicamento:")
medicamento2 = input("Ingrese la dosis que debe consumir el paciente:")
medicamento3 = input("Ingrese las instrucciónes de uso del medicamento:")
doctor = input("Ingrese el nombre del doctor a cargo:")

recetaMedica(fechaEmisión, nombre, fecha, clinica, medicamento, medicamento2, medicamento3, doctor)