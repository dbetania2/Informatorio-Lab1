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
        if columna not in self.df.columns:
            print(f"columna '{columna}' no encontrada.")
            return

        if not pd.api.types.is_numeric_dtype(self.df[columna]):
            print(f"columna '{columna}' no es numerica.")
            return

        datos = self.df[columna].dropna().round(0)  # 👈 Redondea los valores al entero más cercano

        sns.histplot(datos, bins=10, kde=False)

        plt.title(f"histograma de {columna} (redondeado)")
        plt.xlabel(columna)
        plt.ylabel("frecuencia")
        plt.tight_layout()
        plt.show()

