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