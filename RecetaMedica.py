def guion():
    print("_"*50)


def paciente(name, date):
    guion()
    print("Receta médica a nombre de:", name)
    print("Fecha de nacimiento del paciente:", date)


def medicamento(med, dose, instructions):
    print("MEDICAMENTO:", med)
    print("Dosis recomendada:", dose)
    print("Instrucciones de uso:", instructions)


def clinica(address):
    print("Por reclamos y consultas acudir a", address, "🔎")


name = input("Ingrese el nombre completo del paciente: ")
date = input("Ingrese la fecha de nacimiento del paciente: ")
address = input("Ingrese la dirección de la clínica médica: ")
med = input("Ingrese el nombre del medicamento a recetar: ")
dose = input("Ingrese la dosis recomendada del medicamento: ")
instructions = input("Ingrese las instrucciones de uso del medicamento: ")

paciente(name, date)
medicamento(med, dose, instructions)
clinica(address)
guion()
