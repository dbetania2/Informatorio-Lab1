import pandas as pd

class ValidadorDatos:
    
    #clase dedicada a realizar validaciones basicas sobre un dataframe de pandas.
    
    def __init__(self, df: pd.DataFrame):
        
        #inicializa una instancia de validadordatos.

        # el atributo 'self.df' almacena el dataframe que sera validado por los metodos de la clase.
        self.df = df

    def validar_nulos(self):
        
       # verifica y reporta si existen valores nulos dentro del dataframe.

       
        # 'self.df.isnull().values.any()' devuelve 'true' si hay al menos un valor nulo en el dataframe.
        if self.df.isnull().values.any():
            print("datos nulos detectados.")
        else:
            print("no hay datos nulos.")

    def validar_duplicados(self):
        
        #cuenta y reporta la cantidad de filas completamente duplicadas en el dataframe.
        # 'self.df.duplicated().sum()' cuenta el numero de filas que son duplicados.
        duplicados = self.df.duplicated().sum()
        if duplicados > 0:
            print(f"hay {duplicados} filas duplicadas.")
        else:
            print("no hay filas duplicadas.")

    def validar_tipos(self):
        
        #muestra en la consola los tipos de datos inferidos para cada columna del dataframe.
        
        print("tipos de datos detectados:")
        # 'self.df.dtypes' devuelve una serie con los tipos de datos de cada columna.
        print(self.df.dtypes)
    
