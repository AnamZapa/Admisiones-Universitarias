import pandas as pd

def cargaEstudiantes ():
    df = pd.read_csv('../data/estudiantes.csv')
    return df

def cargaCursos ():
    df = pd.read_csv('../data/cursos.csv')
    return df