import pandas as pd
from carga import carga_estudiantes, carga_inscripciones
from limpieza import limpiezaEstudiantes, limpiezaInscripciones

df_estudiantes = carga_estudiantes()
df_inscripciones = carga_inscripciones()

print("Carga de datos completada. Iniciando limpieza de datos.")

df_estudiantes_limpio = limpiezaEstudiantes(df_estudiantes)
df_inscripciones_limpio = limpiezaInscripciones(df_inscripciones)

print("Limpieza de datos completada. Iniciando análisis de datos.")

df = pd.merge(
    df_inscripciones_limpio,
    df_estudiantes_limpio,
    on="ID_estudiante",
    how="inner"
)

print("Tablas unidas correctamente")

# PREGUNTA 1 - Programa con mayor cantidad de registros
print("\nAnalizando programa con mayor cantidad de registros")
programa_top = df["Programa_inscrito"].value_counts()
print("Programa con más inscripciones:")
print(programa_top.head(1))


# PREGUNTA 2 - Promedio valor matrícula por programa
print("\nAnalizando promedio de valor matrícula por programa")

promedio_programa = (
    df.groupby("Programa_inscrito")["Valor_matricula"]
    .mean()
    .sort_values(ascending=False)
)
print("Promedio matrícula por programa:")
print(promedio_programa)

# PREGUNTA 3 - Cuántos estudiantes aprobaron Medicina
print("\nAnalizando cantidad de estudiantes que aprobaron Medicina")

aprobados_medicina = df[
    (df["Programa_inscrito"] == "Medicina") &
    (df["Estado_inscripcion"] == "Aprobada")
]

print("Cantidad aprobados en Medicina:")
print(len(aprobados_medicina))

# PREGUNTA 4 - Ciudad con más inscripciones
print("\nAnalizando ciudad con más inscripciones")
ciudad_top = df["Ciudad_origen"].value_counts()
print("Ciudad con más inscripciones:")
print(ciudad_top.head(1))