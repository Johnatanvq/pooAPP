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
        if self.conexion:
            self.cursor = self.conexion.cursor()  
            
    def autenticarUsuario(self):
        if self.nombre and self.contrasena:
            try:
                # Consulta a la base de datos para verificar usuario y contraseña
                query = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
                values = (self.nombre, self.contrasena)
                self.cursor.execute(query, values)
                resultado = self.cursor.fetchone()  # Obtener el primer resultado coincidente
                #fetchall para traerse todos los elementos coincidentes
                
                if resultado:
                    # FALTA QUE TIRE A LA OTRA PANTALLA
                    print(f"""Autenticación exitosa
                            Bienvenido {self.nombre}""")
                    
                    return True
                    
                else:
                    # Mostrar mensaje de error si no hay coincidencia
                    print("Autenticación fallida")
                    #MANDAR A POP UP
                    return False
            except psycopg2.Error as e:
                print(f"Error al consultar la base de datos: {e}")
                self.conexion.rollback() 
        else:
            print("No hay datos para autenticar")




class adminUsuario(Usuario):

    def guardar(self):
        # Capturar el texto antes de guardar en la base de datos
        self.capturar_texto()

        # Verificar si se capturaron datos en ambos campos
        if self.texto and self.numero:
            try:
                # Ejecutar la inserción en la tabla usuario
                query = "INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)"
                values = (self.texto, self.numero)
                self.cursor.execute(query, values)
                self.conexion.commit()  # Asegurar que los cambios se guarden
                
                print("Datos guardados en la base de datos correctamente")
            except psycopg2.Error as e:
                self.conexion.rollback()
                print(f"Error al guardar los datos: {e}")
        else:
            print("No hay datos para guardar")

    # def closeEvent(self, event):
        # # Cerrar la conexión a la base de datos al cerrar la ventana
        # if self.cursor:
        #     self.cursor.close()
        # if self.conexion:
        #     self.conexion.close()
        # print("Conexión a la base de datos cerrada")