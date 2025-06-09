from sqlalchemy import create_engine

# ruta a base de datos sqlite.
database_url = "sqlite:///database/recolector.db"


#  motor de sqlalchemy..
# 'echo=false' para no imprirmi cada consulta sql en la consola .
#  'echo=true' para ver todas las consultas sql en la consola.
engine = create_engine(database_url, echo=False)
