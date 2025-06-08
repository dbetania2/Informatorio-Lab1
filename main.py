import os
from lector_de_datos.lector_csv import LectorCSV
from lector_de_datos.lector_json import LectorJSON
from lector_de_datos.lector_xlsx import LectorXLSX

from validaciones.validador import ValidadorDatos
from persistencia.data_saver import DataSaver

from estadisticas.analisis_basico import AnalisisBasico
from visualizaciones.grafico_simple import GraficoSimple

def procesar_archivo(archivo: str, carpeta_archivos: str, saver: DataSaver):
    
    #encapsula la logica completa para procesar un unico archivo de datos.

    # construye la ruta completa al archivo, uniendo la carpeta y el nombre del archivo.
    ruta_completa = os.path.join(carpeta_archivos, archivo)

    # determina el tipo de lector segun la extension del archivo.
    if archivo.endswith(".csv"):
        #se crea una instancia de 'lectorcsv'.
        lector = LectorCSV(ruta_completa)
    elif archivo.endswith(".json"):
        #se crea una instancia de 'lectorjson'.
        lector = LectorJSON(ruta_completa)
    elif archivo.endswith(".xlsx"):
        #se crea una instancia de 'lectorxlsx'.
        lector = LectorXLSX(ruta_completa)
    else:
        
        print(f"error de al procesar archivo: {archivo}")
        return

    # cargar los datos desde la fuente (csv,json,excel) usando el lector.
    lector.cargar_datos()
    #aplicar transformaciones estandar a los datos cargados.
    lector.transformar_datos()
    #obtener el dataframe procesado del objeto lector.
    df = lector.datos

    #validar los datos del dataframe.
    # se crea una instancia de 'validadordatos' con el dataframe.
    validador = ValidadorDatos(df)
    # se ejecutan las validaciones
    validador.validar_tipos()
    validador.validar_nulos()
    validador.validar_duplicados()

    #guardar el dataframe.
    # se obtiene el nombre de la tabla de la base de datos a partir del nombre del archivoeliminando su extension.
    nombre_tabla = os.path.splitext(archivo)[0]

    # mostrar estadistica y grafico simple
    print(f"\n--- analisis para '{archivo}' ---")

    # intenta encontrar la primera columna numerica en el dataframe.
    # 'select_dtypes(include=["number"])' selecciona solo las columnas de tipo numerico.
    # '.columns[0]' toma el nombre de la primera de esas columnas.
    # 'if not ... empty else none' maneja el caso donde no hay columnas numericas.
    columna = df.select_dtypes(include=["number"]).columns[0] if not df.select_dtypes(include=["number"]).empty else None

    # si se encontro una columna numerica, procede con el analisis y la visualizacion.
    if columna:
    # inicializa una instancia de 'analisisbasico' con el dataframe actual.
        analisis = AnalisisBasico(df)
    # llama al metodo para mostrar las estadisticas de la columna numerica encontrada.
        analisis.mostrar_estadisticas(columna)

    # inicializa una instancia de 'graficosimple' con el dataframe actual.
        grafico = GraficoSimple(df)
    # llama al metodo para mostrar el histograma de la columna numerica.
        grafico.mostrar_histograma(columna)
    else:
    # si no se encuentra ninguna columna numerica en el dataframe, imprime un mensaje.
        print("no se encontro una columna numerica para analisis.")

    # persistencia de datos
    saver.guardar_dataframe(df, nombre_tabla)

def main():
    
    #funcion principal para procesamiento de multiples archivos.
   
    # define la carpeta donde se encuentran los archivos a procesar.
    carpeta_archivos = "files"

    # obtiene una lista de todos los nombres de archivos dentro de la carpeta especificada.
    archivos = os.listdir(carpeta_archivos)

    # unica instancia de 'datasaver' para todos los archivos.
    saver = DataSaver()

    # itera sobre cada archivo en la lista y delega su procesamiento a 'procesar_archivo'.
    for archivo in archivos:
        procesar_archivo(archivo, carpeta_archivos, saver)

if __name__ == "__main__":
    main()