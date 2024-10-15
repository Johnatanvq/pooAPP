from backend.database import Database
import psycopg2

class Espacio():
    nombre = ""
    bloque = ""
    capacidad = ""
    tipo = ""
    #ubicacion = ""
    
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
                nombre VARCHAR(255) PRIMARY KEY,     -- nombre es la clave primaria
                bloque VARCHAR(255),     -- bloque
                capacidad VARCHAR(255), -- capacidad
                tipo VARCHAR(255), -- tipo
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'espacio' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")
class adminEspacio(Espacio):
    def crearEspacio (self, nombre, bloque, capacidad, tipo):
        #capturar datos recibidos de inputs
        self.nombre = nombre
        self.bloque = bloque
        self.capacidad = capacidad
        self.tipo = tipo

    #verificar si todos los datos tienen campos
        if self.nombre and self.bloque and self.capacidad and self.tipo:
            try:
                 #SQL insertar datos
                query = """
                INTERT INTO espacios (nombre, bloque, capacidad, tipo) 
                 VALUES (%s, %s, %s, %s )
                 RETURNING id;
                """ # %s placeholders

                #Asigna valores capturados de entradas
                values = (self.nombre, self.bloque, self.capacidad, self.tipo)

                 #consulta y obtenemos el ID generado
                self.cursor.execute(query, values)
                
                #Recupere el id del nuevo espacio
                #new_space_id = self.cursos.fetchone()[0]#si no hay mas filas, fetchone devuelve none

                #Guardad los cambios
                self.conexion.commit()
                print(f"Espacio '{self.nombre} creado correctamente")
                return True
            except psycopg2.Error as e:
                # Si hay un error, hacemos rollback para no aplicar cambios parciales
                self.conexion.rollback()
                print(f"Error al guardar los datos: {e}")
                return False
        else:
            print("Faltan datos para crear el espacio. Asegúrate de que todos los campos estén diligenciados")
            return False
#Metodo para actualizar los datos del espacio en la BD
def actualizarEspacio (self, nombre, bloque, capacidad, tipo):
    try:
        query = """
        UPDATE espacios SET
            bloque = %s,
            capacidad = %s,
            tipo = %s
        WHERE nombre = %s
        """
        values = (bloque, capacidad, tipo, nombre) # nombre para identificar el espacio
        self.cursor.execute(query, values)
        self.conexion.commit()
        return True
    except psycopg2.Error as e:
        self.conexion.rollback()
        print(f"Error al actualizar espacios: {e}")
        return False
#metodo para eliminar espacios
def eliminarEspacio(self, nombre):
    try:
        query= "DELETE FROM espacio WHERE nombre = %s"
        self.cursor.execute(query, (nombre,))
        self.conexion.commit()
        return True
    except psycopg2.Error as e:
        self.conexion.rollback()
        print(f"Error al eliminar espacio: {e}")
        return False
#metoodo para cargar los nombre existentes en la base de datos 
def cargarEspacio(self):
    try:
        query = "SELECT nombre FROM espacio"
        self.cursor.execute(query)
        espacios = self.cursor.fetchall()
        return [espacios[0] for espacio in espacios]
    except psycopg2.Error as e:
        print(f"Error al cargar los espacios: {e}")
        return []
 
#Metodo para cargar los datos de cada espacio existente en la BD
def cargarDetallesEspacio(self, nombre_espacio):
    try:
        query ="SELEC nombre, bloque, capacidad, tipo FRON espacio WHERE nombre = %s"
        self.cursor.execute(query, (nombre_espacio,))
        return self.cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Error al cargar detaller del espacio: {e}")
        return None
    
def mostrarEspacio(self):
    print(f"Espacio: {self.nombre}, Tipo: {self.tipo}")
    

