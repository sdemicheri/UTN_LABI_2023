def crear_receta():
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente: ")
    direccion_clinica = input("Ingrese la dirección de la clínica: ")
    nombre_medicamento = input("Ingrese el nombre del medicamento recetado: ")
    dosis = input("Ingrese la dosis del medicamento: ")
    instrucciones = input("Ingrese las instrucciones de uso del medicamento: ")

    receta = {
        "nombre_paciente": nombre_paciente,
        "fecha_nacimiento": fecha_nacimiento,
        "direccion_clinica": direccion_clinica,
        "nombre_medicamento": nombre_medicamento,
        "dosis": dosis,
        "instrucciones": instrucciones
    }
    return receta

def imprimir_receta(receta):
    print("Receta Médica")
    print("==============")
    print("Nombre del paciente:", receta["nombre_paciente"])
    print("Fecha de nacimiento:", receta["fecha_nacimiento"])
    print("Dirección de la clínica:", receta["direccion_clinica"])
    print("\n Medicamento recetado:")
    print("Nombre:", receta["nombre_medicamento"])
    print("Dosis:", receta["dosis"])
    print("Instrucciones:", receta["instrucciones"])

# Crear la receta con los datos ingresados por el usuario
receta = crear_receta()

# Imprimir la receta
imprimir_receta(receta)


