"""
Enunciado:
Crea una clase llamada "DatabaseConnector" que represente un conector de
base de datos genérico con bajo acoplamiento, fácil de mantener y extender,
Por lo tanto, que permita conectarse a diferentes tipos de bases
de datos. La clase debe tener un método "connect" que permita establecer
una conexión con una base de datos específica.

Además, se deben crear tres clases para diferentes tipos de bases de datos:
"SQLDatabase", "PostgresDatabase", y "RedshiftDatabase". Cada clase de base
de datos debe tener una propiedad "connected" que se establezca en True
cuando se conecta correctamente a la base de datos.

Métodos y propiedades:

Clase "DatabaseConnector":
    connect(database): conecta a una base de datos específica. El parámetro
    "database" debe ser una instancia de una de las clases de base de datos
    ("SQLDatabase", "PostgresDatabase" o "RedshiftDatabase").

Clase "SQLDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Clase "PostgresDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Clase "RedshiftDatabase":
    connected: propiedad booleana que indica si la conexión a la base de
    datos se estableció correctamente.

Ejemplo:
    Entrada:
        db_connector = DatabaseConnector()
        sql_db = SQLDatabase()
        postgres_db = PostgresDatabase()
        redshift_db = RedshiftDatabase()
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)
        db_connector.connect(sql_db)
        db_connector.connect(postgres_db)
        db_connector.connect(redshift_db)
        print(sql_db.connected, postgres_db.connected, redshift_db.connected)

    Salida:
        False False False
        True True True
"""

class DatabaseConnector:
    def __init__(self):
       self.database = None

    def connect(self, database):
        self.database = database
        database.connected = True


class SQLDatabase:
    def __init__(self):
        self.connected = False


class PostgresDatabase:
    def __init__(self):
        self.connected = False


class RedshiftDatabase:
    def __init__(self):
        self.connected = False


# Por la propia naturaleza del ejercicios no se puede probar imprimiendo por pantalla, 
# revisa los tests para revisar la corrección de tu propuesta de solución
