from backend.database import Database

import psycopg2

class Espacio():
    ident = ""
    bloque = ""
    ocupantes = ""
    sector = ""
    ubicacion = ""
    
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
            