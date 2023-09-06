class RecetaMedica:
    def __init__(self, nombre_paciente, fecha_nacimiento, clinica, medicamento, dosis, instrucciones, fecha_turno):
        self.nombre_paciente = nombre_paciente
        self.fecha_nacimiento = fecha_nacimiento
        self.clinica = clinica
        self.medicamento = medicamento
        self.dosis = dosis
        self.instrucciones = instrucciones
        self.fecha_turno = fecha_turno

    def generar_receta(self):
        print("----- Receta Médica -----")
        print(f"Nombre del Paciente: {self.nombre_paciente}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Dirección de la Clínica: {self.clinica}")
        print("\nDetalles del Medicamento:")
        print(f"Nombre del Medicamento: {self.medicamento}")
        print(f"Dosis: {self.dosis}")
        print(f"Instrucciones: {self.instrucciones}")
        print("\nFecha y Hora del Turno Médico:")
        print(f"Fecha: {self.fecha_turno}")
        print("--------------------------")


nombre = input("Nombre completo del paciente: ")
fecha_nac = input("Fecha de nacimiento (DD/MM/AAAA): ")
clinica = input("Dirección de la Clínica Médica: ")
medicamento = input("Nombre del medicamento: ")
dosis = input("Dosis del medicamento: ")
instrucciones = input("Instrucciones de uso: ")
fecha_turno = input("Fecha y hora del turno médico: ")

receta = RecetaMedica(nombre, fecha_nac, clinica, medicamento, dosis, instrucciones, fecha_turno)
receta.generar_receta()
