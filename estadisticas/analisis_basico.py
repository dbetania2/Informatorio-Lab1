import pandas as pd

class AnalisisBasico:
    """
    clase dedicada a realizar analisis estadisticos descriptivos basicos a modo de practica y ejemplo
    sobre columnas numericas de un dataframe de pandas.
    """
    def __init__(self, df: pd.DataFrame):
        
        # el atributo 'self.df' almacena el dataframe sobre el cual se realizaran los analisis.
        self.df = df

    def mostrar_estadisticas(self, columna: str):
        
        #calcula y muestra la media, mediana y moda para una columna numerica especifica del dataframe.

        
        # verifica si la columna especificada por el usuario existe en el dataframe.
        if columna not in self.df.columns:
            print(f"columna '{columna}' no encontrada.")
            return # si la columna no existe, se detiene la ejecucion del metodo.

        # verifica si la columna es de un tipo de dato numerico.
        # 'pd.api.types.is_numeric_dtype' es la forma preferida de pandas para esta comprobacion.
        if not pd.api.types.is_numeric_dtype(self.df[columna]):
            print(f"columna '{columna}' no es numerica.")
            return # si la columna no es numerica, se detiene la ejecucion.

        # calcula la media (promedio) de los valores en la columna.
        media = self.df[columna].mean()
        # calcula la mediana (valor central) de los valores en la columna.
        mediana = self.df[columna].median()
        # calcula la moda (valor mas frecuente) de los valores en la columna.
        # '.mode()' puede devolver multiples modas si hay empates, y '.iloc[0]' toma el primero.
        # 'if not self.df[columna].mode().empty else none' maneja el caso donde no hay moda (columna vacia).
        moda = self.df[columna].mode().iloc[0] if not self.df[columna].mode().empty else None

        # imprime las estadisticas calculadas de forma legible.
        print(f"\nestadisticas de la columna '{columna}':")
        print(f"  media:   {media}")
        print(f"  mediana: {mediana}")
        print(f"  moda:    {moda}")