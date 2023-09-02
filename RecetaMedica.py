
DIRECCION_DE_LA_CLINICA = "Gral. Paz 365"

nombreDelPaciente = input("Ingrese el nombre completo del paciente: ")
fechaDeNacimientoDelPaciente = input("Ingrese fecha de nacimiento del paciente(dd/mm/aaaa): ")

nombreDelMedicamento = input("Ingrese el nombre del medicamento: ")
dosisDelMedicamento = input("Ingrese la dosis del medicamento(mg): ")
consumoDiarioEnHoras = input("Ingrese cada cuantas horas tiene que volver a consumir el medicamento: ")
diasDeConsumo = input("Ingrese cuantos días máximo debe consumir el paciente el medicamento: ")
requisitosAntesDeConsumir = input("Ingrese que es recomendable hacer antes de consumir el medicamento:")

centerText = "\t\t\t\t"


def imprimir_receta_medica():
    print("¬" * 50)
    print(centerText, "🩺Receta médica: \n")
    print("El paciente {nombre} nacido el {fecha}\n".format(nombre=nombreDelPaciente, fecha=fechaDeNacimientoDelPaciente))
    print(centerText, "Proscripción: \n"
          "\ntomar '{nombre}' cada {horas}hs. x{dias} días"
          .format(nombre=nombreDelMedicamento, horas=consumoDiarioEnHoras, dias=diasDeConsumo))
    print("Antes de consumir: ", requisitosAntesDeConsumir)
    print("¬" * 50)


imprimir_receta_medica()
