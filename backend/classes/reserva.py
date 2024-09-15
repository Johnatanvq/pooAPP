from backend.database import Database

import psycopg2

class Reserva():
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
            
