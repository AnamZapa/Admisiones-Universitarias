import pandas as pd

def cargaEstudiantes ():
    df_estudiantes = pd.read_csv('../data/estudiantes.csv')
    return df_estudiantes

def cargaCursos ():
    df_cursos = pd.read_csv('../data/cursos.csv')
    return df_cursos