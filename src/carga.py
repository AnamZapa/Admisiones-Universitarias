import pandas as pd

def cargaEstudiantes ():
    df_estudiantes = pd.read_csv('../data/raw/estudiantes_sucio.csv', sep=';')
    return df_estudiantes

def cargaInscripciones ():
    df_inscripciones = pd.read_csv('../data/raw/inscripciones_sucio.csv', sep=';')
    return df_inscripciones