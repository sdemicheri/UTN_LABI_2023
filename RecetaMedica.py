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
nombre = input("Ingrese nombre y apellido del paciente:")
fecha = input("Ingrese su fecha de nacimiento:")
clinica = input("Ingrse la dirección del establecimiento médico:")
medicamento = input("Ingrese el nombre del medicamento:")
medicamento2 = input("Ingrese la dosis que debe consumir el paciente:")
medicamento3 = input("Ingrese las instrucciónes de uso del medicamento:")
doctor = input("Ingrese el nombre del doctor a cargo:")

recetaMedica(fechaEmisión, nombre, fecha, clinica, medicamento, medicamento2, medicamento3, doctor)

def proximoTurno(clinica, fechaEmision, nombre, documento, mutual, turno, doctor):
    print("--------------------------------------------")
    print("            PROXIMO TURNO                   ")
    print("|Fecha Actual: ", fechaEmision)
    print("|Clinica🏣: ", clinica)
    print("|Paciente👪: ", nombre)
    print("|D.N.I: ", documento)
    print("|Mutual: ", mutual)
    print("|Turno📆: ", turno)
    print("|Doctor👨‍⚕️: ", doctor)
    print("--------------------------------------------")


clinica = input("Ingrse la dirección del establecimiento médico:")
fechaEmision = input("Ingrese la fecha actual:")
nombre = input("Ingrese nombre y apellido del paciente:")
documento = input("Ingrese el D.N.I del paciente:")
mutual = input("Ingrese la obra social del paciente:")
turno = input("Ingrese la fecha del proximo turno programado:")
doctor = input("Ingrese el nombre del doctor a cargo:")

proximoTurno(clinica, fechaEmision, nombre, documento, mutual, turno, doctor)