import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.classes.usuario import Usuario
from datetime import datetime
import locale

# from conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI

import time
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante
from backend import variablesGlobales

class calendarioGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/calendario/calendario.ui", self)
        
        
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
        self.calendario.selectionChanged.connect(self.capturarFecha)
        
    def capturarFecha(self):
        fechaSeleccionada = self.calendario.selectedDate().toPyDate()
        print(fechaSeleccionada)
        # Formatear la fecha como 'dd-mm-YYYY'
        fechaOrdenada = datetime.strftime(fechaSeleccionada, '%d-%B-%Y')
        
        # Capturar la hora y minutos actuales
        horaActual = datetime.now().strftime("%H:%M")
        
        # Concatenar la fecha y la hora en un string
        fechaCompletaStr = f"{fechaOrdenada} {horaActual}"
        
        # Convertir el string a datetime usando strptime con el formato correcto
        variablesGlobales.fechaInicio = datetime.strptime(fechaCompletaStr, "%d-%B-%Y %H:%M")
        
        # Verificar el tipo de fechaInicio (será un objeto datetime)
        print(type(variablesGlobales.fechaInicio))
        print(variablesGlobales.fechaInicio)
        self.close()
        self.login_window = nuevaReservaGUI()  # Instanciar la ventana de login
        self.login_window.show()

    def cerrarSesion(self): 
        from conectarLogin import loginGUI

        #se cierra la conexión a la base de datos desde la clase Usuario
        if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
            self.nuevoUsuario.cursor.close()
        if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
            self.nuevoUsuario.conexion.close()
        print("Conexión a la base de datos cerrada")
        
        #redirigir login
        self.close()
        self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = calendarioGUI()
    GUI.show()
    sys.exit(app.exec_())