# Clase abstracta base que define la interfaz para cargar y transformar datos
from abc import ABC, abstractmethod
import pandas as pd

class Dataset(ABC):
    #clase base abstracta para la gestion de datasets.
    
    def __init__(self, fuente):
        # el atributo _fuente almacena la ruta o identificador de la fuente de datos.
        # esta protegido (por el guion bajo) para indicar que no debe ser accedido directamente
        # fuera de la clase.
        self._fuente = fuente
        # el atributo _datos almacenara el dataframe de pandas una vez que los datos sean cargados y protegidos.
        self._datos = None

    @property
    def datos(self):
        #getter de datos
        return self._datos

    @datos.setter
    def datos(self, value):
        #setter para datos
        if not isinstance(value, pd.DataFrame):
            raise ValueError("los datos deben ser un dataframe.")
        self._datos = value

    @property
    def fuente(self):
        #getter de fuente 
        return self._fuente

    @abstractmethod
    def cargar_datos(self):
        #metodo abstracto que debe ser implementado por las subclases.
        pass

    def transformar_datos(self):
        
        #aplica transformaciones basicas y generales al dataframe de datos.
        
        if self._datos is not None:
            # normaliza los nombres de las columnas: los convierte a minusculas
            # y elimina espacios en blanco al inicio y al final.
            self._datos.columns = self._datos.columns.str.lower().str.strip()
            # itera sobre las columnas de tipo 'object' (normalmente texto)
            # para eliminar espacios en blanco al inicio y al final de cada celda.
            for col in self._datos.select_dtypes(include="object").columns:
                self._datos[col] = self._datos[col].astype(str).str.strip()
            # elimina filas completamente duplicadas del dataframe.
            self._datos.drop_duplicates(inplace=True)
            print("transformaciones basicas aplicadas.")
        else:
            print("no hay datos para transformar.")
    
    def mostrar_resumen(self):
        
        #muestra un resumen estadistico basico del dataframe.
        if self._datos is not None:
            print(self._datos.describe(include='all'))
        else:
            print("no hay datos cargados.")