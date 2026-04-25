import pandas as pd
from carga import cargaEstudiantes, cargaCursos

def limpiezaEstudiantes (df_estudiantes): 
    print("Limpieza de datos en el DataFrame de estudiantes:")
    #duplicados
    df_estudiantes = df_estudiantes.drop_duplicates()
    #valores nulos
    df_estudiantes["Edad"] = df_estudiantes["Edad"].fillna("16")
    df_estudiantes["Genero"] = df_estudiantes["Genero"].replace("", np.nan)
    df_estudiantes["Genero"] = df_estudiantes["Genero"].fillna("Prefiere no decir")
    df_estudiantes["Correo_electronico"] = df_estudiantes["Correo_electronico"].replace("", np.nan)
    df_estudiantes["Correo_electronico"] = df_estudiantes["Correo_electronico"].fillna("sincorreo@correo.com")
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].replace("", np.nan)
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].fillna("0000000000")
    df_estudiantes["Carreer_aplicada"] = df_estudiantes["CarreraAplicada"].replace("", np.nan)
    df_estudiantes["Carrera_aplicada"] = df_estudiantes["CarreraAplicada"].fillna("Desconocida")
    df_estudiantes["Estrato_socioeconomico"] = df_estudiantes["Estrato_socioeconomico"].fillna("0")
    df_estudiantes["Fecha_nacimiento"] = df_estudiantes["Fecha_nacimiento"].fillna("1900-01-01")
    #estandarizacion de texto, eliminacion de espacios y conversion a formato title case
    df_estudiantes['Nombre_completo'] = df_estudiantes['Nombre_completo'].str.strip().str.title()
    df_estudiantes["Nombre_completo"] = df_estudiantes["Nombre_completo"].str.title()
    df_estudiantes["Genero"] = df_estudiantes["Genero"].str.strip().str.title()
    df_estudiantes['Correo_electronico'] = df_estudiantes['Correo_electronico'].str.strip().str.title()
    df_estudiantes["Correo_electronico"] = df_estudiantes["Correo_electronico"].str.lower()
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].str.strip()
    df_estudiantes["Carrera_aplicada"] = df_estudiantes["Carrera_aplicada"].str.strip().str.title()
    df_estudiantes["Ciudad_origen"] = df_estudiantes["Ciudad_origen"].str.strip().str.title()
    df_estudiantes["Ciudad_origen"] = df_estudiantes["Ciudad_origen"].str.title()
    df_estudiantes["Fecha_nacimiento"] = df_estudiantes["Fecha_nacimiento"].str.strip() 
    #Genero
    traduccion_genero = {"M": "Masculino", "m": "Masculino", "F": "Femenino", "FEMENINO": "Femenino", "masculino": "Masculino", 
                         "N/A": "Prefiere no decir", "Hombre": "Masculino", "mujer": "Femenino","f": "Femenino"}
    df_estudiantes["Genero"] = df_estudiantes["Genero"].replace(traduccion_genero)
    generos_validos = ["Masculino", "Femenino", "Prefiere no decir"]
    df_estudiantes.loc[~df_estudiantes["Genero"].isin(generos_validos), "Genero"] = "Prefiere no decir"
    #Carrera aplicada
    Carrera_aplicada = ["Ingeniería Civil", "Contaduría Pública", "Administración de Empresas", "Arquitectura", "Medicina", 
                         "ingeniería industrial", "Ingeniería de Sistemas", "Diseño Gráfico", "Derecho", "Psicología", "Desconocida"]
    mascara_infractores_carrera = ~df_estudiantes["Carrera_aplicada"].isin(Carrera_aplicada)
    errores_carrera = df_estudiantes[mascara_infractores_carrera]
    traduccion_carrera = {"ingeniería civil": "Ingeniería Civil", "CONTADURÍA": "Contaduría Pública", "administración de empresas": "Administración de Empresas", 
                         "Arquitectura": "Arquitectura", "MEDICINA": "Medicina", "ingeniería industrial": "Ingeniería Industrial", 
                         "Ingeniería de Sistemas": "Ingeniería de Sistemas", "Diseño Gráfico": "Diseño Gráfico", 
                         "Derecho": "Derecho", "PSICOLOGIA": "Psicología", "DECONOCIDA ": "Desconocida "}
    df_estudiantes["Carrera_aplicada"] = df_estudiantes["Carrera_aplicada"].replace(traduccion_carrera)
    #MANEJO DE ERRORES EN EL CAMPO TELEFONO, ELIMINACION DE CARACTERES NO NUMERICOS Y CONVERSION A STRING
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].astype(str).str.replace(r"\D", "", regex=True)
    df_estudiantes.loc[df_estudiantes["Telefono"].str.len()<10, "Telefono"] = "0000000000"
    #CONVERSION DE EDAD A NUMERICO, CON MANEJO DE ERRORES Y FILTRADO DE EDADES INCOHERENTES
    df_estudiantes["Edad"] = pd.to_numeric(df_estudiantes["Edad"], errors="coerce") 
    df_estudiantes.loc[(df_estudiantes["Edad"] < 16) | (df_estudiantes["Edad"] > 80), "Edad"] = None
    #CONVERSION DE FECHA DE NACIMIENTO A FORMATO DE FECHA, CON MANEJO DE ERRORES
    df_estudiantes["Fecha_nacimiento"] = pd.to_datetime(df_estudiantes["Fecha_nacimiento"], errors="coerce", dayfirst=True)
    #estrato
    traduccion_estrato = {"uno": 1, "DOS": 2, "N/A": 0}
    df_estudiantes["Estrato_socioeconomico"] = df_estudiantes["Estrato_socioeconomico"].replace(traduccion_estrato)
    df_estudiantes["Estrato_socioeconomico"] = pd.to_numeric(df_estudiantes["Estrato_socioeconomico"], errors="coerce")
    df_estudiantes["Estrato_socioeconomico"] = df_estudiantes["Estrato_socioeconomico"].fillna(0)
    return df_estudiantes

def limpiezaInscripciones (df_inscripciones):
    print("Tratamiento de duplicados en el DataFrame de inscripciones:")
    df_inscripciones = df_inscripciones.drop_duplicates(subset=["ID_estudiante", "ID_curso"])
    #espacios en blanco y estandarizacion de texto
    df_inscripciones["ID_estudiante"] = df_inscripciones["ID_estudiante"].str.strip()
    df_inscripciones["ID_curso"] = df_inscripciones["ID_curso"].str.strip() 
    df_inscripciones["Tipo_documento"] = df_inscripciones["Tipo_documento"].str.strip().str.title()
    df_inscripciones["Numero_documento"] = df_inscripciones["Numero_documento"].str.strip()
    df_inscripciones["Programa_inscrito"] = df_inscripciones["Programa_inscrito"].str.strip().str.title()
    df_inscripciones["Sede"] = df_inscripciones["Sede"].str.strip().str.title()
    df_inscripciones["Periodo_academico"] = df_inscripciones["Periodo_academico"].str.strip()
    df_inscripciones["Estado_inscripcion"] = df_inscripciones["Estado_inscripcion"].str.strip().str.title()
    df_inscripciones["Medio_pago"] = df_inscripciones["Medio_pago"].str.strip().str.title()
    df_inscripciones["Asesor_asignado"] = df_inscripciones["Asesor_asignado"].str.strip().str.title()
    #mayusculas y minusculas
    df_inscripciones["Programa_inscrito"] = df_inscripciones["Programa_inscrito"].str.title()
    df_inscripciones["Sede"] = df_inscripciones["Sede"].str.title()
    df_inscripciones["Asesor_asignado"] = df_inscripciones["Asesor_asignado"].str.title()
    #estandarizacion de texto en el campo Tipo_documento
    traduccion_tipo_documento = {"cc": "CC", "ti": "TI","T.I": "TI", "ce": "CE", "Pasaporte": "PASAPORTE", 
                                 "c.c.": "CC","C.C.": "CC",}
    df_inscripciones["Tipo_documento"] = df_inscripciones["Tipo_documento"].replace(traduccion_tipo_documento)
    df_inscripciones["Tipo_documento"] = df_inscripciones["Tipo_documento"].str.upper()
    #estandarización en numero de documento
    df_inscripciones["Numero_documento"] = df_inscripciones["Numero_documento"].str.replace(r"\D", "", regex=True)
    #estandarizacion de texto en el campo Programa_inscrito
    traduccion_programa = {"ingeniería civil": "Ingeniería Civil", "CONTADURÍA": "Contaduría Pública", "administración de empresas": "Administración de Empresas", 
                         "Arquitectura": "Arquitectura", "MEDICINA": "Medicina", "ingeniería industrial": "Ingeniería Industrial", 
                         "Ingeniería de Sistemas": "Ingeniería de Sistemas", "Diseño Gráfico": "Diseño Gráfico", 
                         "Derecho": "Derecho", "PSICOLOGIA": "Psicología", "DECONOCIDA ": "Desconocida "}
    df_inscripciones["Programa_inscrito"] = df_inscripciones["Programa_inscrito"].replace(traduccion_programa)
    #estandarizacion de texto en el campo estado de inscripcion
    traduccion_estado_inscripcion = {   "pendiente": "Pendiente", "PENDIENTE": "Pendiente", "aprobada": "Aprobada", "APROBADA": "Aprobada", "rechazada": "Rechazada", 
                                     "RECHAZADA": "Rechazada", "En revisión": "En revisión"}
    df_inscripciones["Estado_inscripcion"] = df_inscripciones["Estado_inscripcion"].replace(traduccion_estado_inscripcion)
    #estandarizacion de texto en el campo medio de pago
    traduccion_medio_pago = { "EFECTIVO": "Efectivo", "efectivo": "Efectivo", "Transferencia": "Transferencia", "transferencia": "Transferencia", "TARJETA CREDITO": "Tarjeta Crédito", 
                             "tarjeta crédito": "Tarjeta Crédito", "Tarjeta Crédito": "Tarjeta Crédito", "BECA": "Beca", "Beca": "Beca"}
    df_inscripciones["Medio_pago"] = df_inscripciones["Medio_pago"].replace(traduccion_medio_pago)
    #valor matricula, conversion a numerico y manejo de errores
    df_inscripciones["Valor_matricula"] = (df_inscripciones["Valor_matricula"].replace(r"[\$,]", "", regex=True)).astype(str)
    #creditos del programa, conversion a numerico y manejo de errores
    df_inscripciones["Creditos_programa"] = pd.to_numeric(df_inscripciones["Creditos_programa"], errors="coerce")
    #semestre de inscripcion, conversion a numerico y manejo de errores
    traduccion_semestre = {"primero": "1", "SEGUNDO": "2", "II": "2",}
    df_inscripciones["Semestre_inscripcion"] = df_inscripciones["Semestre_inscripcion"].replace(traduccion_semestre)
    df_inscripciones["Semestre_inscripcion"] = pd.to_numeric(df_inscripciones["Semestre_inscripcion"], errors="coerce")
    #fecha de inscripcion, conversion a formato de fecha y manejo de errores
    df_inscripciones["Fecha_inscripcion"] = pd.to_datetime(df_inscripciones["Fecha_inscripcion"], errors="coerce", dayfirst=True)
    #nulos
    df_inscripciones["Asesor_asignado"] = df_inscripciones["Asesor_asignado"].replace("", "Sin Asesor")
    df_inscripciones["Asesor_asignado"] = df_inscripciones["Asesor_asignado"].fillna("Sin Asesor")
    df_inscripciones["Valor_matricula"] = df_inscripciones["Valor_matricula"].fillna(df_inscripciones["Valor_matricula"].median())
    df_inscripciones["Creditos_programa"] = df_inscripciones["Creditos_programa"].fillna(df_inscripciones["Creditos_programa"].median())
    df_inscripciones["Semestre_inscripcion"] = df_inscripciones["Semestre_inscripcion"].fillna(df_inscripciones["Semestre_inscripcion"].median())
    return df_inscripciones
