from backend.database import Database

import psycopg2

class Reservas():
    def __init__(self):
        self.ident = None
        self.nombre = None
        self.hora_inicio = None
        self.hora_final = None
        self.fecha_inicio = None
        self.fecha_final = None
        self.lugar = None
        self.periodo = None

        self.db = Database(dbname="pooDATABASE", user="postgres", password="poo1234", host="localhost", port=5432)
        self.conexion = self.db.conectar()

        if self.conexion:
            self.cursor = self.conexion.cursor()
        else:
            print("Sin conexión")

        self.verificarCrearTablaReservas()

    def verificarCrearTablaReservas(self):
        try:
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
            query = """
            CREATE TABLE IF NOT EXISTS reservas (
                id SERIAL PRIMARY KEY,
                descripcion VARCHAR(255),
                fecha_inicio TIMESTAMP,
                fecha_final TIMESTAMP,
                cedula VARCHAR(255) REFERENCES usuarios(cedula) ON DELETE CASCADE
            );
            """
            self.cursor.execute(query)
            self.conexion.commit()
            print("Tabla 'reservas' creada correctamente.")

        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la tabla: {e}")

    def crearReserva(self, descripcion, fecha_inicio, fecha_final, cedula):
        try:
            query = """
            INSERT INTO reservas (descripcion, fecha_inicio, fecha_final, cedula)
            VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (descripcion, fecha_inicio, fecha_final, cedula))
            self.conexion.commit()
            print("Reserva creada correctamente.")
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al crear la reserva: {e}")
    
    def eliminarReserva(self, cedula, descripcion, fecha_inicio, fecha_final):
        """
        Método para eliminar una reserva usando la cédula, la descripción y las fechas como claves.
        """
        try:
            query = """
            DELETE FROM reservas
            WHERE cedula = %s AND descripcion = %s AND fecha_inicio = %s AND fecha_final = %s
            """
            self.cursor.execute(query, (cedula, descripcion, fecha_inicio, fecha_final))
            self.conexion.commit()
            print(f"Reserva eliminada correctamente para el usuario con cédula {cedula}.")
        except psycopg2.Error as e:
            self.conexion.rollback()
            print(f"Error al eliminar la reserva: {e}")
            raise Exception("Error al eliminar la reserva")
            
    def obtenerReservasPorUsuario(self, cedula):
        try:
            query = """
            SELECT descripcion, fecha_inicio, fecha_final, cedula
            FROM reservas
            WHERE cedula = %s
            """
            self.cursor.execute(query, (cedula,))
            reservas = self.cursor.fetchall()
            
            # Estructurar las reservas en un diccionario
            resultado = []
            for reserva in reservas:
                resultado.append({
                    'descripcion': reserva[0],
                    'fecha_inicio': reserva[1],
                    'fecha_final': reserva[2],
                    'cedula': reserva[3]
                })
            return resultado

        except psycopg2.Error as e:
            print(f"Error al consultar las reservas: {e}")
            return []
