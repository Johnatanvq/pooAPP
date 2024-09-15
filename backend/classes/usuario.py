from backend.database import Database

import psycopg2

class Usuario():
    ident = ""
    nombre = ""
    contrasena = ""
    cedula = None
    email = ""
    rol = bool()
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
            
    def autenticarUsuario(self):
        if self.nombre and self.contrasena:
            try:
                # Consulta para obtener el ID y verificar la contraseña
                query = "SELECT id, contrasena FROM usuarios WHERE usuario = %s AND contrasena = %s"
                values = (self.nombre, self.contrasena)
                self.cursor.execute(query, values)
                resultado = self.cursor.fetchone()  # Obtener el primer resultado coincidente
                
                if resultado:
                    # Almacenar el ID del usuario autenticado
                    self.ident = resultado[0]
                    
                    print(f"Autenticación exitosa. Bienvenido {self.nombre}. ID de usuario: {self.ident}")
                    return True
                    
                else:
                    print("Autenticación fallida: Usuario o contraseña incorrectos")
                    return False
            except psycopg2.Error as e:
                print(f"Error al consultar la base de datos: {e}")
                self.conexion.rollback() 
        else:
            print("No hay datos para autenticar")
    
    #CREAR LA TABLA EN LA DB
    def crear_tabla_usuarios(self):
        try:
            # Consulta SQL para crear la tabla 'usuarios'
            query = """
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,            -- ID auto-incrementable y clave primaria
                usuario VARCHAR(50) NOT NULL,     -- Nombre de usuario
                contrasena VARCHAR(255) NOT NULL, -- Contraseña
                cedula VARCHAR(20),               -- Cédula o identificación del usuario
                email VARCHAR(100),               -- Correo electrónico
                rol BOOLEAN NOT NULL,             -- Rol (TRUE para admin, FALSE para usuario regular)
                telefono VARCHAR(20)              -- Teléfono del usuario
            );
            """
            # Ejecutar la consulta para crear la tabla
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'usuarios' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")




class adminUsuario(Usuario):
                    
    def crearUsuario(self, nombre, contrasena, cedula, email, rol, telefono):
        # Capturamos los datos recibidos desde la pantalla (inputs y dropdowns)
        self.nombre = nombre
        self.contrasena = contrasena
        self.cedula = cedula
        self.email = email
        self.rol = rol  # Booleano: True si es admin, False si es usuario regular
        self.telefono = telefono

        # Verificamos si todos los campos esenciales tienen datos
        if self.nombre and self.contrasena and self.cedula and self.email and self.telefono:
            try:
                # Consulta SQL para insertar los datos del nuevo usuario
                query = """
                INSERT INTO usuarios (usuario, contrasena, cedula, email, rol, telefono)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING id;
                """
                
                # Asignamos los valores capturados de los inputs y dropdowns
                values = (self.nombre, self.contrasena, self.cedula, self.email, self.rol, self.telefono)
                
                # Ejecutamos la consulta y obtenemos el ID generado
                self.cursor.execute(query, values)
                
                # Recuperamos el ID del nuevo usuario
                new_user_id = self.cursor.fetchone()[0]

                # Hacemos commit para guardar los cambios
                self.conexion.commit()

                print(f"Usuario creado correctamente con ID: {new_user_id}")
                return True
            except psycopg2.Error as e:
                # Si hay un error, hacemos rollback para no aplicar cambios parciales
                self.conexion.rollback()
                print(f"Error al guardar los datos: {e}")
                return False
        else:
            print("Faltan datos para crear el usuario. Asegúrate de que todos los campos estén llenos.")
            return False

    def mostrarUsuario(self):
        # Este método puede acceder a los valores asignados anteriormente
        print(f"Usuario: {self.nombre}, Rol: {self.rol}")
        

    # def closeEvent(self, event):
        # # Cerrar la conexión a la base de datos al cerrar la ventana
        # if self.cursor:
        #     self.cursor.close()
        # if self.conexion:
        #     self.conexion.close()
        # print("Conexión a la base de datos cerrada")