import pandas as pd
from carga import cargaEstudiantes, cargaCursos

def limpiezaEstudiantes (df_estudiantes): 
    print("Tratamiento de nulos en el DataFrame de estudiantes:")
    df_estudiantes["Edad"] = df_estudiantes["Edad"].fillna("Desconocida")
    df_estudiantes["Genero"] = df_estudiantes["Genero"].fillna("Prefiere no decir")
    df_estudiantes["Correo_electronico"] = df_estudiantes["Correo_electronico"].fillna("sincorreo@correo.com")
    df_estudiantes["Telefono"] = df_estudiantes["Telefono"].fillna("0000000000")
    df_estudiantes["Carrera_aplicada"] = df_estudiantes["CarreraAplicada"].fillna("Desconocida")
    df_estudiantes["Estrato_socioeconomico"] = df_estudiantes["Estrato_socioeconomico"].fillna("0")
    df_estudiantes["Fecha_nacimiento"] = df_estudiantes["Fecha_nacimiento"].fillna("1900-01-01")
    print("Espacios en blanco en el DataFrame de estudiantes:")
    df_estudiantes['nombre'] = df_estudiantes['nombre'].str.strip().str.title()
    df_estudiantes['Correo_electronico'] = df_estudiantes['Correo_electronico'].str.strip().str.title()
    df_estudiantes["Ciudad_origen"] = df_estudiantes["Ciudad_origen"].str.strip().str.title()

    return df_estudiantes