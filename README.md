## Proyecto de Análisis de Datos — Proceso de Inscripciones Universitarias

## Descripción del Proyecto
Este proyecto fue desarrollado en Python con el objetivo de analizar información relacionada con estudiantes aspirantes e inscripciones a programas académicos universitarios.

## La aplicación permite:

Cargar archivos CSV con información de estudiantes e inscripciones.
Realizar limpieza y transformación de datos.
Detectar y corregir valores nulos, duplicados e inconsistencias.
Unir bases de datos relacionadas mediante merge.
Ejecutar análisis estadísticos y consultas relevantes.
Mostrar resultados en consola.

El proyecto aplica buenas prácticas de desarrollo como modularización del código, uso de entorno virtual (venv) y control de versiones con Git Flow.

## Estructura del Proyecto

proyecto-python/
│── data/
│   ├── estudiantes.csv
│   └── inscripciones.csv
│
│── src/
│   ├── carga.py
│   ├── limpieza_estudiantes.py
│   ├── limpieza_inscripciones.py
│   └── analisis.py
│
│── requirements.txt
│── README.md
│── .gitignore

## Requisitos Previos
Tener instalado:
Python 3.10+
Git
Visual Studio Code (opcional)

## Configuración del Entorno Virtual
Crear entorno virtual:
python -m venv venv
Activar entorno virtual en Windows:
.\venv\Scripts\Activate.ps1

## Instalación de Dependencias
Instalar pandas
pip install pandas
O instalar desde requirements.txt:
pip install -r requirements.txt

## Ejecución del proyecto
Ingresar a la carpeta del código fuente:
cd src
Ejecutar el script principal:
python analisis.py

## Análisis Realizados
El sistema responde preguntas como:

¿Cuál programa tiene mayor número de inscripciones?
¿Cuál es el promedio del valor de matrícula por programa?
¿Cuántos estudiantes fueron aprobados en Medicina?
¿Qué ciudad registra más aspirantes?
¿Cuántas inscripciones están pendientes?

## Limpieza de Datos Aplicada
Eliminación de registros duplicados.
Corrección de datos nulos.
Estandarización de texto.
Conversión de tipos de datos.
Homologación de estados y categorías.
Limpieza de fechas, teléfonos y valores monetarios.

## Tecnologías Utilizadas
- Python
Lenguaje principal
- Pandas
Análisis de datos
- Git / GitHub
Control de versiones

## Autor
Ana María Zapata Pinillos
Desarrolladora del Proyecto
