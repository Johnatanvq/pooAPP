from backend.database import Database

import psycopg2

class Reservas():
    ident = ""
    nombre = ""
    hora_inicio = ""
    hora_final = ""
    fecha = ""
    lugar = ""
    periodo = ""
    
    def __init__(self):
        self.ident = None
        self.nombre = None
        self.hora_inicio = None
        self.hora_final = None
        self.fecha = None
        self.lugar = None
        self.periodo = None

        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        if self.conexion:
            self.cursor = self.conexion.cursor()
        else:
            print("Sin conexión")
        
        self.verificarCrearTablaReservas()
        
    
    def verificarCrearTablaReservas(self):
        try:
            # Verificar si la tabla ya existe
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE tablename = 'reservas'
                );
            """)
            tabla_existe = self.cursor.fetchone()[0]

            if not tabla_existe:
                self.crearTablaReservas()

        except psycopg2.Error as e:
            print(f"Error al verificar si la tabla existe: {e}")
            self.conexion.rollback()
            
    def crearTablaReservas(self):
        try:
            #SQL para crear la tabla 'reservas'
            query = """
            CREATE TABLE IF NOT EXISTS reservas (
                id SERIAL PRIMARY KEY,            -- ID auto-incrementable y clave primaria
                descripcion VARCHAR(255), --Descripción de la reserva
                fecha_inicio     -- fecha inicio de la reserva
                fecha_final VARCHAR(255),     -- fecha final de la reserva
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'reservas' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")
