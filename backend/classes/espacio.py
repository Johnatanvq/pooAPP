from backend.database import Database
import psycopg2

class Espacio():
    ident = ""
    bloque = ""
    ocupantes = ""
    sector = ""
    ubicacion = ""
    
    def __init__(self):
        self.ident = None
        self.bloque = None
        self.ocupantes = None
        self.sector = None
        self.ubicacion = None

        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        if self.conexion:
            self.cursor = self.conexion.cursor() 
        else: 
            print('Sin conexión')
        
        self.verificarCrearTablaEspacio()
            
    def verificarCrearTablaEspacio(self):
        try:
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE tablename = 'espacio'
                );
            """)
            tabla_existe = self.cursor.fetchone()[0]

            if not tabla_existe:
                self.crearTablaEspacio()

        except psycopg2.Error as e:
            print(f"Error al verificar si la tabla existe: {e}")
            self.conexion.rollback()
            
    #metodo para crear la tabla 'espacio' en la base de datos
    def crearTablaEspacio(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS espacio (
                id SERIAL PRIMARY KEY,            -- ID auto-incrementable y clave primaria
                bloque VARCHAR(255),     -- bloque
                ocupantes VARCHAR(255),     -- ocupantes
                sector VARCHAR(255), -- sector
                ubicacion VARCHAR(255), --ubicación
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'espacio' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")
            