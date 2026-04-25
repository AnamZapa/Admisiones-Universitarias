from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

def carga_estudiantes():
    ruta = RAW_DIR / "estudiantes_sucio.csv"
    return pd.read_csv(ruta, sep=";")

def carga_inscripciones():
    ruta = RAW_DIR / "inscripciones_sucio.csv"
    return pd.read_csv(ruta, sep=";")