print("Información necesaria para la receta")
print("Información del paciente")
paciente = input("Nombre y apellido del paciente:")
nacimiento = input("Fecha de nacimiento del paciente:")
direccion = input("dirección de la clínica:")
print("información del medicamento")
nombrem = input("nombre del medicamento:")
dosis = input("Dosis del medicamento:")
uso = input("Instrucciones de uso:")
turno = input("Fecha de los próximos turnos: ")

print("RECETA")
print("nombre del paciente:",paciente,)
print("fecha de nacimiento del paciente:",nacimiento,)
print("Debe tomar",dosis, "dosis del medicamento",nombrem,"siguiendo estas instrucciones:",uso,)
print("Fecha del próximo turno:",turno,)