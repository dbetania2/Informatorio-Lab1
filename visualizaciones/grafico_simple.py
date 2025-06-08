import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class GraficoSimple:
    """
    clase dedicada a la creacion y visualizacion de graficos basicos a modo de practica y ejemplo
    a partir de un dataframe de pandas, utilizando las librerias
    seaborn y matplotlib.
    """
    def __init__(self, df: pd.DataFrame):
        
        #inicializa una instancia de graficosimple.

        # almacena el dataframe que sera visualizado.
        self.df = df

    def mostrar_histograma(self, columna: str):
        
        #la funcion realiza validaciones para asegurar que la columna exista y que sea de tipo numerico antes de intentar crear el grafico.
        
        # verifica si la columna especificada existe en el dataframe.
        if columna not in self.df.columns:
            print(f"columna '{columna}' no encontrada.")
            return # sale de la funcion si la columna no existe.

        # verifica si la columna es de tipo numerico.
        if not pd.api.types.is_numeric_dtype(self.df[columna]):
            print(f"columna '{columna}' no es numerica.")
            return # sale de la funcion si la columna no es numerica.

        # crea el histograma usando seaborn.histplot.
        # 'self.df[columna]': los datos de la columna seleccionada.
        # 'kde=false': desactiva la estimacion de densidad del kernel.
        # 'bins=10': divide el rango de datos en 10 barras (bins).
        sns.histplot(self.df[columna], kde=False, bins=10)
        
        # configura el titulo del grafico.
        plt.title(f"histograma de {columna}")
        # configura la etiqueta del eje x.
        plt.xlabel(columna)
        # configura la etiqueta del eje y.
        plt.ylabel("frecuencia")
        
        # ajusta automaticamente los parametros de la trama para que encajen en el area de la figura.
        plt.tight_layout()
        # muestra el grafico.
        plt.show()
