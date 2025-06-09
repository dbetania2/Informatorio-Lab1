# Clase LectorXLSX
import pandas as pd
from lector_de_datos.dataset import Dataset 

class LectorXLSX(Dataset):
    
    #clase encargada de leer y cargar datos desde archivos XLSX .hereda de la clase base 'dataset'
    def cargar_datos(self):
        #implementacion especifica del metodo abstracto 'cargar_datos' para archivos xlsx.
        try:
            
            self.datos = pd.read_excel(self.fuente)
            print(f"archivo excel cargado desde: {self.fuente}")
        except Exception as e:
            # se captura la excepcion y se el error.
            print(f"error al cargar archivo excel: {e}")