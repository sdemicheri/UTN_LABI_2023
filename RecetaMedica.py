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
    guion()


def proximoturno(nextTurn, doc, info, tel, name):
    print("Paciente:", name)
    print("Turno agendado con el Dr.", doc, "para el", nextTurn)
    print("Motivo de la consulta:", info)
    print("En caso de no poder asistir avise con anterioridad \nal número telefónico de referencia")
    print("\t\t\t\t\t", tel)
    guion()


name = input("Ingrese el nombre completo del paciente: ")
date = input("Ingrese la fecha de nacimiento del paciente: ")
address = input("Ingrese la dirección de la clínica médica: ")
med = input("Ingrese el nombre del medicamento a recetar: ")
dose = input("Ingrese la dosis recomendada del medicamento: ")
instructions = input("Ingrese las instrucciones de uso del medicamento: ")
nextTurn = input("Ingrese la fecha y hora del próximo turno del paciente: ")
doc = input("Ingrese el nombre del médico de cabecera del paciente: ")
info = input("Ingrese el motivo de la próxima consulta del paciente: ")
tel = input("Ingrese el número telefónico de la clínica: ")

paciente(name, date)
medicamento(med, dose, instructions)
clinica(address)
proximoturno(nextTurn, doc, info, tel, name)
