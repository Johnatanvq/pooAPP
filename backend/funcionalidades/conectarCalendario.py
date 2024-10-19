import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime
import locale, time
# from conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI
from backend import variablesGlobales

class calendarioGUI(QMainWindow):
    def __init__(self, cedula_usuario):  # Ahora acepta la cédula del usuario
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/calendario/calendario.ui", self)
        
        self.cedula_usuario = cedula_usuario
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
        self.calendario.selectionChanged.connect(self.capturarFecha)
        
    def capturarFecha(self):
        fechaSeleccionada = self.calendario.selectedDate().toPyDate()
        print(fechaSeleccionada)
        # Formatear la fecha como 'dd-mm-YYYY'
        fechaOrdenada = datetime.strftime(fechaSeleccionada, '%d-%B-%Y')
        
        # Capturar la hora y minutos actuales
        horaActual = datetime.now().strftime("%H:%M")
        
        # Concatenar la fecha y hora
        fechaCompletaStr = f"{fechaOrdenada} {horaActual}"
        
        # Convertir el string a datetime usando strptime con el formato correcto
        variablesGlobales.fechaInicio = datetime.strptime(fechaCompletaStr, "%d-%B-%Y %H:%M")
        print(variablesGlobales.fechaInicio)
        self.close()
        self.login_window = nuevaReservaGUI(self.cedula_usuario)  # Instanciar la ventana de login
        self.login_window.show()

    def cerrarSesion(self): 
        from conectarLogin import loginGUI

        #se cierra la conexión a la base de datos desde la clase Usuario
        if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
            self.nuevoUsuario.cursor.close()
        if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
            self.nuevoUsuario.conexion.close()
        print("Conexión a la base de datos cerrada")
        self.close()
        self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = calendarioGUI()
    GUI.show()
    sys.exit(app.exec_())