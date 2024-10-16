import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.classes.usuario import Usuario
from datetime import datetime
import time
from backend.classes.reserva import Reservas
from backend.funcionalidades.conectarLogin import loginGUI
from backend import variablesGlobales
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui

import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class nuevaReservaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/nuevaReserva/nuevaReserva.ui", self)
        
        self.separarCastearFechaInicio()
        self.mostrarFechaInicio()
        self._toggle = True #Parámetro para manejar los checkboxes sin tener error de "recursividad infinita"
        self.no_duracion_checkbox.clicked.connect(self.unicoEstadoCheckbox)
        self.no_duracion_checkbox.stateChanged.connect(self.desabilitarInput)

        self.si_duracion_checkbox.clicked.connect(self.unicoEstadoCheckbox)

        # self.nuevaReserva = Reservas()
        
    
    def unicoEstadoCheckbox(self):
        self.no_duracion_checkbox.setChecked(self._toggle) # Old value of our check1 becomes the value of check2
        self._toggle = not self._toggle # Invert
        self.si_duracion_checkbox.setChecked(self._toggle) # New value is assigned to check1
        
    def desabilitarInput(self):
        if self.no_duracion_checkbox.isChecked():
            self.select_dia_final.setDisabled(True)
            self.select_mes_final.setDisabled(True)
            self.input_ano_final.setDisabled(True)
            self.select_hora_final.setDisabled(True)
            self.select_minuto_final.setDisabled(True)
        else:
            self.select_dia_final.setDisabled(False)
            self.select_mes_final.setDisabled(False)
            self.input_ano_final.setDisabled(False)
            self.select_hora_final.setDisabled(False)
            self.select_minuto_final.setDisabled(False)
            
    def separarCastearFechaInicio(self):
        
        self.dia = datetime.strftime(variablesGlobales.fechaInicio, "%d")
        self.mes = datetime.strftime(variablesGlobales.fechaInicio, "%B")
        print(self.mes)
        self.ano = datetime.strftime(variablesGlobales.fechaInicio, "%Y")
        
        self.hora = datetime.strftime(variablesGlobales.fechaInicio, "%H")
        self.minutos = datetime.strftime(variablesGlobales.fechaInicio, "%M")
        # print("la hora de inicio es: ", (hora))
        
    def mostrarFechaInicio(self):
        self.select_dia_inicio.setCurrentText(self.dia)
        self.select_mes_inicio.setCurrentText(self.mes)
        self.input_ano_inicio.setText(self.ano)
        self.select_hora_inicio.setCurrentText(self.hora)
        self.select_minutos_inicio.setCurrentText(self.minutos)        
            
    def cerrarSesion(self):
        
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
    GUI = nuevaReservaGUI()
    GUI.show()
    sys.exit(app.exec_())