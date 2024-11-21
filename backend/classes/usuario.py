from backend.database import Database
import psycopg2

class Usuario:
    def __init__(self):
        self.ident = None
        self.nombre = None
        self.usuario = None
        self.contrasena = None
        self.cedula = None
        self.email = None
        self.rol = None
        self.telefono = None
        self.es_admin = False  # Atributo para identificar si es admin

        self.db = Database(dbname="pooDATABASE", user="postgres", password="poo1234", host="localhost", port=5432)
        self.conexion = self.db.conectar()

        if self.conexion:
            self.cursor = self.conexion.cursor()
        else:
            print('Sin conexión')

        self.verificarCrearTablaUsuarios()

    def autenticarUsuario(self):
        if self.nombre and self.contrasena:
            try:
                # Consulta para verificar credenciales
                query = "SELECT contrasena, cedula, usuario FROM usuarios WHERE usuario = %s AND contrasena = %s"
                values = (self.nombre, self.contrasena)
                self.cursor.execute(query, values)
                resultado = self.cursor.fetchone()

                if resultado:
                    self.ident = resultado[0]  # Contraseña
                    self.cedula = resultado[1]  # Cédula
                    self.usuario = resultado[2]  # Nombre

                    # Verificar si es admin
                    self.es_admin = self.nombre == "admin" and self.contrasena == "Admin1!"
                    print(f"Autenticación exitosa. Usuario: {self.nombre}, Es admin: {self.es_admin}")
                    return True
                else:
                    print("Autenticación fallida: Usuario o contraseña incorrectos")
                    return False
            except psycopg2.Error as e:
                print(f"Error al consultar la base de datos: {e}")
                self.conexion.rollback()
        else:
            print("No hay datos para autenticar")
        return False
            
            
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
            # Crear la tabla si no existe
            query_tabla = """
            CREATE TABLE IF NOT EXISTS usuarios (
                nombre VARCHAR(255),     -- Nombre completo del usuario
                usuario VARCHAR(255), -- Nombre de usuario (único)
                contrasena VARCHAR(255), -- Contraseña
                cedula VARCHAR(255) PRIMARY KEY,     -- Cédula o identificación
                email VARCHAR(255),      -- Correo electrónico
                rol VARCHAR(255),        -- Rol (puede ser "admin" o "usuario")
                telefono VARCHAR(255)    -- Teléfono
            );
            """
            self.cursor.execute(query_tabla)
            self.conexion.commit()
            print("Tabla 'usuarios' creada correctamente.")

            # Verificar si ya existe un usuario admin
            query_verificar_admin = "SELECT COUNT(*) FROM usuarios WHERE usuario = 'admin'"
            self.cursor.execute(query_verificar_admin)
            existe_admin = self.cursor.fetchone()[0]

            if not existe_admin:
                # Insertar el usuario admin si no existe
                query_admin = """
                INSERT INTO usuarios (nombre, usuario, contrasena, cedula, email, rol, telefono) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values_admin = (
                    "Administrador",         # Nombre
                    "admin",                 # Usuario
                    "Admin1!",               # Contraseña
                    "0000000001",            # Cédula
                    "admin@pooapp.com",      # Email
                    "admin",                 # Rol
                    "0000000000"             # Teléfono
                )
                self.cursor.execute(query_admin, values_admin)
                self.conexion.commit()
                print("Usuario 'admin' creado con todos los campos.")
            else:
                print("El usuario 'admin' ya existe.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla o insertar el usuario admin: {e}")


class adminUsuario(Usuario):
                    
    def crearUsuario(self, nombre, usuario, contrasena, cedula, email, rol, telefono):
        if nombre and usuario and contrasena and cedula and email and telefono:
            try:
                query = """
                INSERT INTO usuarios (nombre, usuario, contrasena, cedula, email, rol, telefono)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                values = (nombre, usuario, contrasena, cedula, email, rol, telefono)
                self.cursor.execute(query, values)
                self.conexion.commit()
                print(f"Usuario creado correctamente con cédula: {cedula}")
                return True
            except psycopg2.IntegrityError:
                self.conexion.rollback()
                print("Error: Un usuario con esta cédula ya existe.")
                return False
            except psycopg2.Error as e:
                self.conexion.rollback()
                print(f"Error al guardar el usuario: {e}")
                return False
        else:
            print("Faltan datos para crear el usuario. Asegúrate de que todos los campos estén llenos.")
            return False

    def actualizarUsuario(self, cedula, nombre, usuario, contrasena, email, rol, telefono):
        if not cedula:
            print("Error: No se ha especificado una cédula válida.")
            return False

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
            print(f"Usuario con cédula {cedula} actualizado correctamente.")
            return True
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al actualizar usuario: {e}")
            return False

    def eliminarUsuario(self, cedula):
        if not cedula:
            print("Error: No se ha especificado una cédula válida.")
            return False
        try:
            query = "DELETE FROM usuarios WHERE cedula = %s"
            self.cursor.execute(query, (cedula,))
            self.conexion.commit()
            print(f"Usuario con cédula {cedula} eliminado correctamente.")
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
            query = "SELECT nombre, usuario, contrasena, cedula, email, rol, telefono FROM usuarios WHERE nombre = %s"
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