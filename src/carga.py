import pandas as pd

def cargaEstudiantes ():
    df_estudiantes = pd.read_csv('../data/estudiantes.csv', sep=';')
    return df_estudiantes

def cargaCursos ():
    df_cursos = pd.read_csv('../data/cursos.csv', sep=';')
    return df_cursos