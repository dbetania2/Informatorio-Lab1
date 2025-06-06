import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from persistencia.engine import engine  # importamos el engine de sqlalchemy

class DataSaver:
    
    #clase encargada de la persistencia de datos,utiliza un 'engine' de sqlalchemy para establecer la conexion.
    
    def __init__(self):
        
        #el constructor inicializa la instancia de datasaver.
        #asigna el 'engine' de sqlalchemy 
        self.engine = engine

    def guardar_dataframe(self, df: pd.DataFrame, nombre_tabla: str):
        
        # valida que el primer argumento 'df' sea una instancia de pandas.dataframe.
        # si no lo es, imprime un mensaje de error y detiene la ejecucion.
        if not isinstance(df, pd.DataFrame):
            print(f"error: se esperaba un dataframe, se recibio {type(df)}")
            return

        try:
            # .to_sql() de pandas para guardar el dataframe en la base de datos.
            # 'nombre_tabla': define el nombre de la tabla en la bd.
            # 'self.engine': la conexion a la base de datos a traves del engine.
            # 'if_exists='replace'': si la tabla ya existe, la reemplaza completamente.
            # 'index=false': no guarda el indice del dataframe como una columna en la tabla.

            df.to_sql(nombre_tabla, self.engine, if_exists='replace', index=False)
            print(f"datos guardados en tabla: {nombre_tabla}")
        except SQLAlchemyError as e:
            # captura cualquier excepcion relacionada con sqlalchemy (errores de base de datos)
            print(f"error al guardar en la base de datos: {e}")