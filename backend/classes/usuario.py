from backend.database import Database
import psycopg2

class Usuario():
    ident = ""
    nombre = ""
    contrasena = ""
    cedula = None
    email = ""
    rol = None
    telefono = None
    
    def __init__(self):
        self.ident = None
        self.nombre = None
        self.contrasena = None
        self.cedula = None
        self.email = None
        self.rol = None
        self.telefono = None

        self.db = Database(dbname = "pooDATABASE" , user = "postgres", password = "poo1234", host = "localhost", port = 5432)
        self.conexion = self.db.conectar()
        
        #objeto que representa la conexion a la base de datos
        if self.conexion:
            self.cursor = self.conexion.cursor()
        else: 
            print('Sin conexión')
        
        self.verificarCrearTablaUsuarios()
            
    #método para autenticar el usuario y contraseña
    def autenticarUsuario(self):
        if self.nombre and self.contrasena:
            try:
                # Consulta para obtener la cédula y verificar la contraseña
                query = "SELECT contrasena, cedula FROM usuarios WHERE usuario = %s AND contrasena = %s"
                values = (self.nombre, self.contrasena)
                self.cursor.execute(query, values)
                resultado = self.cursor.fetchone()  # Obtener el primer resultado coincidente

                if resultado:
                    self.ident = resultado[0]  # ID del usuario
                    self.cedula = resultado[1]  # Almacenar la cédula del usuario autenticado
                    print(f"Autenticación exitosa. Bienvenido {self.nombre}. Cédula de usuario: {self.cedula}")
                    return True
                else:
                    print("Autenticación fallida: Usuario o contraseña incorrectos")
                    return False
            except psycopg2.Error as e:
                print(f"Error al consultar la base de datos: {e}")
                self.conexion.rollback()
        else:
            print("No hay datos para autenticar")
            
            
    #método para verificar si la tabla de 'usuarios' existe en la base de datos
    def verificarCrearTablaUsuarios(self):
        try:
            self.cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM pg_tables
                    WHERE tablename = 'usuarios'
                );
            """)
            tabla_existe = self.cursor.fetchone()[0]

            if not tabla_existe:
                self.crearTablaUsuarios()

        except psycopg2.Error as e:
            print(f"Error al verificar si la tabla existe: {e}")
            self.conexion.rollback()
            
    #metodo para crear la tabla 'usuarios' en la base de datos
    def crearTablaUsuarios(self):
        try:
            query = """
            CREATE TABLE IF NOT EXISTS usuarios (
                nombre VARCHAR(255),     -- Nombre de usuario
                usuario VARCHAR(255),     -- Nombre de usuario
                contrasena VARCHAR(255), -- Contraseña
                cedula VARCHAR(255) PRIMARY KEY,               -- Cédula o identificación del usuario
                email VARCHAR(255),               -- Correo electrónico
                rol VARCHAR(255),             -- Rol (TRUE para admin, FALSE para usuario regular)
                telefono VARCHAR(255)              -- Teléfono del usuario
            );
            """
            #consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'usuarios' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")


class adminUsuario(Usuario):
                    
    def crearUsuario(self, nombre, usuario, contrasena, cedula, email, rol, telefono):
        # Verificar si todos los campos tienen datos
        if self.nombre and self.usuario and self.contrasena and self.cedula and self.email and self.telefono:
            try:
                # SQL insertar datos
                query = """
                INSERT INTO usuarios (nombre, usuario, contrasena, cedula, email, rol, telefono)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                
                # Asigna valores capturados de entradas
                values = (self.nombre, self.usuario, self.contrasena, self.cedula, self.email, self.rol, self.telefono)
                
                # Ejecuta la consulta
                self.cursor.execute(query, values)

                # Guardar los cambios
                self.conexion.commit()

                print(f"Usuario creado correctamente con cédula: {self.cedula}")
                return True
            except psycopg2.Error as e:
                # Si hay un error, hacemos rollback para no aplicar cambios parciales
                self.conexion.rollback()
                print(f"Error al guardar los datos: {e}")
                return False
        else:
            print("Faltan datos para crear el usuario. Asegúrate de que todos los campos estén llenos.")
            return False
        
    # método para actualizar los datos del usuario en la base de datos
    def actualizarUsuario(self, cedula, nombre, usuario, contrasena, email, rol, telefono):
        try:
            query = """
            UPDATE usuarios SET 
                nombre = %s, 
                usuario = %s, 
                contrasena = %s, 
                email = %s, 
                rol = %s, 
                telefono = %s
            WHERE cedula = %s
            """
            values = (nombre, usuario, contrasena, email, rol, telefono, cedula)
            self.cursor.execute(query, values)
            self.conexion.commit()
            return True
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al actualizar usuario: {e}")
            return False


    #metodo para eliminar el usuario por completo
    def eliminarUsuario(self, cedula):
        try:
            query = "DELETE FROM usuarios WHERE cedula = %s"
            self.cursor.execute(query, (cedula,))
            self.conexion.commit()
            return True
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al eliminar usuario: {e}")
            return False

        
    #metodo para cargar los nombres existentes en la base de datos
    def cargarUsuarios(self):
        try:
            query = "SELECT nombre FROM usuarios"
            self.cursor.execute(query)
            usuarios = self.cursor.fetchall()
            return [usuario[0] for usuario in usuarios]
        except psycopg2.Error as e:
            print(f"Error al cargar los usuarios: {e}")
            return []
        
    #metodo para cargar los datos de cada usuario existentes en la base de datos
    def cargarDetallesUsuario(self, nombre_usuario):
        try:
            query = "SELECT id, nombre, usuario, contrasena, cedula, email, rol, telefono FROM usuarios WHERE nombre = %s"
            self.cursor.execute(query, (nombre_usuario,))
            return self.cursor.fetchone()
        except psycopg2.Error as e:
            print(f"Error al cargar detalles del usuario: {e}")
            return None
        
    def mostrarUsuario(self):
        print(f"Usuario: {self.nombre}, Rol: {self.rol}")
        
    # def closeEvent(self, event):
        # # Cerrar la conexión a la base de datos al cerrar la ventana
        # if self.cursor:
        #     self.cursor.close()
        # if self.conexion:
        #     self.conexion.close()
        # print("Conexión a la base de datos cerrada")