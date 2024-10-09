import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.classes.usuario import Usuario
from datetime import datetime
# from conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI

import time
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class calendarioGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/calendario/calendario.ui", self)
        
        
        
        self.calendario.selectionChanged.connect(self.capturarFecha)
        
    def capturarFecha(self):
        fechaSeleccionada = self.calendario.selectedDate().toPyDate()
        print(fechaSeleccionada)
        fecha_ordenada = datetime.strftime(fechaSeleccionada, '%d-%m-%Y')
        print(type(fecha_ordenada))
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