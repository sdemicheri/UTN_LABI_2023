def crear_receta():
    # Solicitar datos de la clínica
    nomClinica = input("Ingrese el nombre de la clínica: ")
    dirClinica = input("Ingrese la dirección de la clínica: ")
    telClinica = input("Ingrese el número de teléfono de la clínica: ")

    # Solicitar datos del medicamento e instrucciones de dosificacion
    nomMedicamento = input("Ingrese el nombre del medicamento: ")
    dosisMedicamento = input("Ingrese la dosis del medicamento: ")
    frecMedicamento = input("Ingrese la frecuencia del medicamento: ")
    instMedicamento = input("Ingrese las instrucciones de dosificación: ")

    # Solicitar datos del paciente
    nomPaciente = input("Ingrese el nombre del paciente: ")
    edadPaciente = input("Ingrese la edad del paciente: ")
    diagPaciente = input("Ingrese el diagnóstico del paciente: ")

    # Solicitar fecha nuevo turno
    fechaNuevoTurno = input("Ingrese fecha de proximo turno: ")

    # Crear la receta
    receta = f"""
    Receta Médica

    Clínica: {nomClinica}
    Dirección: {dirClinica}
    Teléfono: {telClinica}

    Medicamento: {nomMedicamento}
    Dosis: {dosisMedicamento}
    Frecuencia: {frecMedicamento}
    Instrucciones de Dosificación: {instMedicamento}

    Datos del Paciente:
    Nombre: {nomPaciente}
    Edad: {edadPaciente} años
    Diagnóstico: {diagPaciente}
    Próximo Turno: {fechaNuevoTurno}

    Por favor, siga las instrucciones de dosificación detenidamente.
    Si experimenta efectos secundarios o tiene preguntas, consulte a su médico.

    ¡Cuídate y recupérate pronto!🤗
    """

    return receta