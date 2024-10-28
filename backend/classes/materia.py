from backend.database import Database
import psycopg2

class Materia():
    id_materia = ""
    nombre_materia = ""
    programa = ""
    intensidad_horaria = ""
    
    def _init_(self):
        self.id_materia = None
        self.nombre_materia = None
        self.programa = None
        self.intensidad_horaria = None
        
        #Configuración BD
        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        if self.conexion:
            self.cursor = self.conexion.cursor() 
        else: 
            print('Sin conexión a la base de datos')
            
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
                id_materia VARCHAR(10) PRIMARY KEY,  -- Identificador de la materia y clave primaria
                nombre_materia VARCHAR(255),         -- nombre
                programa VARCHAR(255),               -- facultad
                intesidad_horaria INT                -- Instensidad horaria
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'materia' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")

class adminMateria(Materia):
    def crearMateria (self, id_materia, nombre_materia, programa, intensidad_horaria):
        if self.id_materia and self.nombre_materia and self.programa and self.intensidad_horaria:
            try: 
                query = """
                INSERT INTO materias(id_materia, nombre_materia, programa, intensidad_horaria)
                VALUES (%s, %s, %s, %s)
                """
            except psycopg2.Error as e:
                self.conexion.rollback()
                print(f"Error al crear la materia: {e}")
                return False
    def actualizarMateria (self, id_materia, nombre_materia, programa, intensidad_horaria):
        try:
            query = """
            UPDATE materias SET
                nombre_materia = %s,
                programa = %s,
                intensidad_horaria = %s,
            WHERE id_materia = %s
            """
            values = (nombre_materia, programa, intensidad_horaria, id_materia)
            self.cursor.execute(query, values)
            self.conexion.commit()
            print(f"Materia con ID{id_materia} actualizada correctamente")
            return True
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al actualizar la materia: {e}")
            return False
        
    def eliminarMateria (self, id_materia):
        try:
            query = "DELETE FROM materias EHERE id_materia = %s"
            self.cursor.execute(query, (id_materia,))
            self.conexion.commit()
            print(f"Materia con ID {id_materia} eliminada correctamente")
            return True
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al aeliminar la materia: {e}")
            return False
        
    def cargarMaterias(self):
        try:
            query = "SELECT nombre_materia FROM materias"
            self.cursor.execute(query)
            materias = self.cursor.fetchall()
            return [materia[0] for materia in materias]
        except psycopg2.Error as e:
            print(f"Error al cargar las materias: {e}")
            return []
    
    def cargarDetallerMaterias (self, id_materia):
        try:
            query = "SELECT id_materia, nombre_materia, programa, intensidad_horaria FROM materias WHERE id_materia = %s"
            self.cursor.execute(query, (id_materia,))
            return self.cursor.fetchone() 
        except psycopg2.Error as e:
            print(f"Error al cargar detalles de la materia: {e}")
            return None