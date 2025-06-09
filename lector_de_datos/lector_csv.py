# Clase LectorCSV
import pandas as pd
from lector_de_datos.dataset import Dataset 

class LectorCSV(Dataset):
    
    #clase encargada de leer y cargar datos desde archivos CSV.hereda de la clase base 'dataset'
    def cargar_datos(self):
        #implementacion especifica del metodo abstracto 'cargar_datos' para archivos CSV.
        try:
            
            self.datos = pd.read_csv(self.fuente)
            print(f"archivo csv cargado desde: {self.fuente}")
        except Exception as e:
            # se captura la excepcion y se el error.
            print(f"error al cargar archivo csv: {e}")
