import pandas as pd
from carga import cargaEstudiantes, cargaCursos

def limpiezaEstudiantes (df_estudiantes): 
    print("Tratamiento de duplicados en el DataFrame de estudiantes:")
    df_estudiantes = df_estudiantes.drop_duplicates(subset="Nombre_completo")
    print("Tratamiento de nulos en el DataFrame de estudiantes:")
    df_estudiantes["Edad"] = df_estudiantes["Edad"].fillna("18")
    df_estudiantes["Genero"] = df_estudiantes["Genero"].fillna("Prefiere no decir")
    df_estudiantes["Correo_electronico"] = df_estudiantes["Correo_electronico"].fillna("sincorreo@correo.com")
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].fillna("0000000000")
    df_estudiantes["Carrera_aplicada"] = df_estudiantes["CarreraAplicada"].fillna("Desconocida")
    df_estudiantes["Estrato_socioeconomico"] = df_estudiantes["Estrato_socioeconomico"].fillna("0")
    df_estudiantes["Fecha_nacimiento"] = df_estudiantes["Fecha_nacimiento"].fillna("1900-01-01")
    print("Espacios en blanco en el DataFrame de estudiantes:")
    df_estudiantes['Nombre_completo'] = df_estudiantes['Nombre_completo'].str.strip().str.title()
    df_estudiantes['Correo_electronico'] = df_estudiantes['Correo_electronico'].str.strip().str.title()
    df_estudiantes["Ciudad_origen"] = df_estudiantes["Ciudad_origen"].str.strip().str.title()
    #LISTA ESTRICTA DE GENEROS VALIDOS PARA EL CAMPO GENERO
    Genero = ["Masculino", "Femenino", "Prefiere no decir"]
    mascara_infractores = ~df_estudiantes["Genero"].isin(Genero)
    errores_genero = df_estudiantes[mascara_infractores]
    traduccion_genero = {"M": "Masculino", "F": "Femenino", "FEMENINO": "Femenino", "masculino": "Masculino", 
                         "N/A": "Prefiere no decir", "Hombre": "Masculino", "mujer": "Femenino"}
    df_estudiantes["Genero"] = df_estudiantes["Genero"].replace(traduccion_genero)
    #LISTA ESTRICTA DE GENEROS VALIDOS PARA EL CAMPO CARRERA APLICADA
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
    df["Telefono"] = df["Telefono"].astype(str).str.replace(r"\D", "", regex=True)
    #CONVERSION DE EDAD A NUMERICO, CON MANEJO DE ERRORES Y FILTRADO DE EDADES INCOHERENTES
    df_estudiantes["Edad"] = pd.to_numeric(df_estudiantes["Edad"], errors="coerce") 
    df_estudiantes.loc[(df_estudiantes["Edad"] < 16) | (df_estudiantes["Edad"] > 80), "Edad"] = None
    #CONVERSION DE FECHA DE NACIMIENTO A FORMATO DE FECHA, CON MANEJO DE ERRORES
    df_estudiantes["Fecha_nacimiento"] = pd.to_datetime(df_estudiantes["Fecha_nacimiento"], errors="coerce", dayfirst=True)

    return df_estudiantes
