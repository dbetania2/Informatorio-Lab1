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

    def limpiar_nulos(self):

        try:
            columnas_reemplazadas = 0

            for col in self.df.columns:
                nulos_antes = self.df[col].isnull().sum()
                if nulos_antes > 0:
                    if self.df[col].dtype == "object":
                        self.df[col].fillna("0", inplace=True)
                    else:
                        self.df[col].fillna(0, inplace=True)
                    columnas_reemplazadas += 1
                    print(f"→ Se reemplazaron {nulos_antes} nulos en la columna '{col}'")

            if columnas_reemplazadas == 0:
                print("No se encontraron nulos para reemplazar.")
            else:
                print(f"\nTotal de columnas tratadas : {columnas_reemplazadas}")

        except Exception as e:
            print(f"error al intentar limpiar nulos: {e}")



 

