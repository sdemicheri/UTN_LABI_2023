#en esta parte del codigo se encuentran los datos del paciente y de la clinica
def imprimirDatosPaciente(pacienteNombre, pacienteNaciemiento, direccionClinica):
    print("-------👨‍🔬Receta Médica👨‍🔬-------")
    print("                               ")
    print("     Nombre del paciente:")
    print(pacienteNombre)
    print("                               ")
    print("     Fecha de Nacimiento:")
    print(pacienteNaciemiento)
    print("                               ")
    print("  🏥Direccón de la Clínica:")
    print(direccionClinica)
    print("-------------------------------")

#en esta parte del codigo se encuentran los datos del medicamento recetado
def imprimirDatosMedicamento(medicamentoNombre, medicamentoDosis, medicamentoInstrucciones):
    print("   💊Medicamento Recetado:    ")
    print(medicamentoNombre)
    print("                              ")
    print("           💉Dosis:")
    print(medicamentoDosis)
    print("                              ")
    print("    🔵Instrucciones de Uso🔵 ")
    print(medicamentoInstrucciones)
    print("------------------------------")

#en esta parte del codigo se especifica la fecha del siguiente turno del paciente
def imprimirSiguienteTurno(turnoSiguiente):
    print("   📆Fecha del Próximo Turno📆")
    print(turnoSiguiente)
    print("------------------------------")

#en esta parte del codigo se solicitan los datos del paciente y del medicamento
pacienteNombre = input("Ingrese el nombre completo del paciente:")
pacienteNacimiento = input("Ingrese la fecha de nacimiento del paciente:")
direccionClinica = input("Ingrese la direccion de la clinica:")
medicamentoNombre = input("Especifique el nombre del Medicamento:")
medicamentoDosis = input("Especifique la dosis necesaria del Medicamento:")
medicamentoInstrucciones = input("Indique las instrucciones del medicamento:")
turnoSiguiente = input("Introduce la fecha del siguiente turno:")

imprimirDatosPaciente(pacienteNombre, pacienteNacimiento , direccionClinica)
imprimirDatosMedicamento(medicamentoNombre, medicamentoDosis, medicamentoInstrucciones)