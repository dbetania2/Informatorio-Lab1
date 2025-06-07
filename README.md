# Procesamiento y Persistencia de Datasets para Análisis de Datos

Este proyecto de Python está diseñado para facilitar el **procesamiento y la persistencia de diversos datasets** desde diferentes formatos de archivo. Su objetivo principal es automatizar la carga, validación y almacenamiento de datos, preparándolos para su posterior análisis.
Este es un programa desarrollado como parte de un ejercicio de **Análisis de Datos** para el curso de programación del **Informatorio Chaco**.

### **Datasets Utilizados**

Para el desarrollo de este programa, se han utilizado los siguientes datasets:

* **JSON:** [Students Grading Dataset](https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset/data)
* **CSV:** [Extrovert vs Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data)
* **XLSX:** [HR Employee Analytics](https://www.kaggle.com/datasets/kmldas/hr-employee-data-descriptive-analytics)

## Guía detallada de configuración e instalación:

[**DelGreccoDaiana-Lab1 (Google Drive)**](<https://docs.google.com/document/d/1t-yh5uJH_E2yxYm414ChE_JypABjv9ubHDo4-zlYD1s/edit?usp=sharing>)

Este documento externo contiene todos los pasos que segui para la creación del entorno virtual hasta la instalación de dependencias y la conexión con el repositorio remoto.

## Características Principales

El proyecto permite:
* **Lectura Multi-formato:** Soporte para cargar datasets desde archivos **CSV**, **JSON** y **XLSX**.
* **Validaciones Automatizadas:** Aplicación de validaciones esenciales como la verificación de tipos de datos, campos obligatorios, eliminación de duplicados y manejo de valores nulos.
* **Persistencia Robusta:** Almacenamiento de los datos procesados en una base de datos relacional utilizando **SQLAlchemy**, con una tabla dedicada por cada dataset cargado.

## Flujo de Trabajo del Proyecto

La aplicación sigue un flujo automatizado y eficiente para el procesamiento de tus datasets:

1.  **Inicio:** El usuario ejecuta el script principal `main.py`.
2.  **Detección y Carga:** El sistema identifica y carga automáticamente todos los archivos de datasets presentes en el directorio `files/`.
3.  **Validación de Datos:** Cada dataset cargado es sometido a un conjunto de validaciones de calidad de datos, asegurando su integridad.
4.  **Persistencia:** Los datos validados se guardan de forma organizada en tablas dedicadas dentro de la base de datos `database/recolector.db`.
5.  **Reporte Final:** Al concluir, la aplicación proporciona un resumen en la terminal indicando qué datasets fueron procesados exitosamente y cuáles presentaron algún error durante el proceso.

