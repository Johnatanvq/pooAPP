import psycopg2

class Database():
    dbname = ""
    user = ""
    password = ""
    host= ""

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def conectar(self):
        try:
            credenciales = {
                "dbname": self.dbname,
                "user": self.user,
                "password": self.password,
                "host": self.host,
                "port": self.port
            }
            conexion = psycopg2.connect(**credenciales)
            if conexion:
                print("Conexión exitosa")
            return conexion
        except psycopg2.Error as e:
            print("Ocurrió un error al conectar a PostgreSQL: ", e)