import pandas as pd
import matplotlib.pyplot as plt
from carga import carga_estudiantes, carga_inscripciones

df_estudiantes_limpio = carga_estudiantes()
df_inscripciones_limpio = carga_inscripciones()

# print("--- GRÁFICO 1: TENDENCIA TEMPORAL (Líneas) ---")
# plt.figure(figsize=(8, 4))
# # marker='o' pone un punto en cada mes
# plt.plot(df_estudiantes_limpio['mes'], df_meses['ventas'], color='#2ca02c', marker='o', linewidth=2)
# plt.title("Crecimiento de Ventas (Enero - Mayo)", fontsize=14, fontweight='bold')
# plt.xlabel("Mes")
# plt.ylabel("Millones USD")
# plt.show() # Cierra y renderiza el primer gráfico

print("Grafico 1: Ciudades con más estudiantes inscritos")
plt.figure(figsize=(8, 4))
# Contar el número de estudiantes por ciudad
ciudades = df_estudiantes_limpio['Ciudad_origen'].value_counts()
# Crear un gráfico de barras
ciudades.plot(kind='bar', color='#1f77b4')
plt.title("Número de Estudiantes por Ciudad", fontsize=14, fontweight='bold')
plt.xlabel("Ciudad")
plt.ylabel("Número de Estudiantes")
plt.show() 
