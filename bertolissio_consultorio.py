def paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
    direccion = input("Ingrese la dirección de la clínica médica: ")
    texto = "| Nombre del paciente: " + nombre  + " | Fecha de nacimiento: " + fecha_nacimiento + " | Direccion de la clinica: " + direccion
    return texto

def medicamento():
    nombre = input("Ingrese el nombre del medicamento: ")
    dosis = input("Ingrese la dosis del medicamento: ")
    instrucciones = input("Ingrese las instrucciones de uso: ")
    texto = "| Nombre del medicamento: " + nombre + " | Dosis del medicamento: " + dosis + " | Instrucciones del medicamento: " + instrucciones
    return texto


def turno():
    dia_semana = input("Ingrese el día de la semana del proximo turno: ")

    # Validar el día de la semana ingresado
    dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes"]

    if dia_semana.lower() in dias_validos:
        return("| El paciente tiene el proximo turno el día " + dia_semana )
    else:
        print("Día de la semana no válido. Por favor, ingrese un día válido.")


dia_turno = turno()
paciente_datos = paciente()
medicamento_datos = medicamento()

print("─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")
print("| DATOS DEL PACIENTE:")
print(paciente_datos)
print("| INFORMACION DEL MEDICAMENTO:")
print(medicamento_datos)
print("| PROXIMO TURNO:")
print(dia_turno)
print("─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────")

