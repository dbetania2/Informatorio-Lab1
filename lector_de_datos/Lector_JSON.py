import pandas as pd
from lector_de_datos.dataset import Dataset 

class LectorJSON(Dataset):
     #clase encargada de leer y cargar datos desde archivos json. hereda de la clase base 'dataset'
    
    def cargar_datos(self):
        
        #implementacion especifica del metodo abstracto 'cargar_datos'
        
        try:
            # se asegura que siempre sea un dataframe.
            self.datos = pd.read_json(self.fuente)
            print(f"archivo json cargado desde: {self.fuente}")
        except Exception as e:
            # se captura la excepcion y se muestra un mensaje de error.
            print(f"error al cargar archivo json: {e}")
