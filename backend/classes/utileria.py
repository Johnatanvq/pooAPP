from backend.database import Database
import psycopg2

class Utileria():
    ident = ""
    tipo = ""
    capacidad = None
    ubicacion = ""
    
    def __init__(self):
        self.ident = None
        self.tipo = None
        self.capacidad = None
        self.ubicacion = None

        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        if self.conexion:
            self.cursor = self.conexion.cursor()
        else: 
            print('Sin conexión')

        self.verificarCrearTablaUtileria()
    def verificarCrearTablaUtileria(self):
        try:
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE tablename = 'utileria'
                );
            """)
            tabla_existe = self.cursor.fetchone()[0]

            if not tabla_existe:
                self.crearTablaUtileria()

        except psycopg2.Error as e:
            print(f"Error al verificar si la tabla existe: {e}")
            self.conexion.rollback()
            
    #metodo para crear la tabla 'usuarios' en la base de datos
    def crearTablaUtileria(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS utileria (
                id SERIAL PRIMARY KEY,            -- ID auto-incrementable y clave primaria
                tipo VARCHAR(255),     -- tipo
                capacidad VARCHAR(255),     -- capacidad
                ubicacion VARCHAR(255), -- ubicación
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'utileria' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")