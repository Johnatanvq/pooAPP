from backend.database import Database
import psycopg2

class Materia():
    ident = ""
    nombre = ""
    facultad = ""
    cedula = None
    pregrado = ""
    
    def __init__(self):
        self.ident = None
        self.nombre = None
        self.facultad = None
        self.cedula = None
        self.pregrado = None

        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        if self.conexion:
            self.cursor = self.conexion.cursor() 
        else: 
            print('Sin conexión')
            
        self.verificarCrearTablaMateria()
            
    def verificarCrearTablaMateria(self):
        try:
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE tablename = 'materia'
                );
            """)
            tabla_existe = self.cursor.fetchone()[0]

            if not tabla_existe:
                self.crearTablaMateria()

        except psycopg2.Error as e:
            print(f"Error al verificar si la tabla existe: {e}")
            self.conexion.rollback()
            
    #metodo para crear la tabla 'materia' en la base de datos
    def crearTablaMateria(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS materia (
                id SERIAL PRIMARY KEY,            -- ID auto-incrementable y clave primaria
                nombre VARCHAR(255),     -- nombre
                facultad VARCHAR(255),     -- facultad
                cedula VARCHAR(255), -- cedula
                pregrado VARCHAR(255), --pregrado
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'materia' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")