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

def crear_proximo_turno():
    fecha_turno = input("Ingrese la fecha del próximo turno (DD/MM/AAAA): ")
    hora_turno = input("Ingrese la hora del próximo turno: ")
    lugar_turno = input("Ingrese el lugar del próximo turno: ")

    proximo_turno = {
        "fecha_turno": fecha_turno,
        "hora_turno": hora_turno,
        "lugar_turno": lugar_turno
    }
    return proximo_turno

def imprimir_receta_y_turno(receta, turno):
    print("Receta Médica y Próximo Turno")
    print("================================")
    print("Nombre del paciente:", receta["nombre_paciente"])
    print("Fecha de nacimiento:", receta["fecha_nacimiento"])
    print("Dirección de la clínica:", receta["direccion_clinica"])
    print("\nMedicamento recetado:")
    print("Nombre:", receta["nombre_medicamento"])
    print("Dosis:", receta["dosis"])
    print("Instrucciones:", receta["instrucciones"])
    print("\nPróximo Turno:")
    print("Fecha:", turno["fecha_turno"])
    print("Hora:", turno["hora_turno"])
    print("Lugar:", turno["lugar_turno"])

# Crear la receta y el próximo turno con los datos ingresados por el usuario
receta = crear_receta()
turno = crear_proximo_turno()

# Imprimir la receta y el próximo turno
imprimir_receta_y_turno(receta, turno)
