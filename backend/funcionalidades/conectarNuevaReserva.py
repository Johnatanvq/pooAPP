import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.classes.usuario import Usuario
from datetime import datetime, timedelta
import time
from backend.classes.reserva import Reservas
from backend.funcionalidades.conectarLogin import loginGUI
from backend import variablesGlobales
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui

import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class nuevaReservaGUI(QMainWindow):
    def __init__(self, cedula_usuario):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/nuevaReserva/nuevaReserva.ui", self)
        
        self.reservas = Reservas()  # Instancia de la clase Reservas
        self.cedula_usuario = cedula_usuario

        self.separarCastearFechaInicio()
        self.mostrarFechaInicio()

        # Inicializar checkboxes y botones
        self._toggle = True
        self.no_duracion_checkbox.clicked.connect(self.unicoEstadoCheckbox)
        self.no_duracion_checkbox.stateChanged.connect(self.desabilitarInput)
        self.si_duracion_checkbox.clicked.connect(self.unicoEstadoCheckbox)
        self.crear_bt_reserva.clicked.connect(self.guardarReserva)

    def unicoEstadoCheckbox(self):
        self.no_duracion_checkbox.setChecked(self._toggle)
        self._toggle = not self._toggle
        self.si_duracion_checkbox.setChecked(self._toggle)

    def desabilitarInput(self):
        if self.no_duracion_checkbox.isChecked():
            # Desactivar inputs de fecha final
            self.select_dia_final.setDisabled(True)
            self.select_mes_final.setDisabled(True)
            self.input_ano_final.setDisabled(True)
            self.select_hora_final.setDisabled(True)
            self.select_minuto_final.setDisabled(True)
        else:
            # Activar inputs de fecha final
            self.select_dia_final.setDisabled(False)
            self.select_mes_final.setDisabled(False)
            self.input_ano_final.setDisabled(False)
            self.select_hora_final.setDisabled(False)
            self.select_minuto_final.setDisabled(False)

    def separarCastearFechaInicio(self):
        # Obtener la fecha de inicio desde la variable global
        self.dia = datetime.strftime(variablesGlobales.fechaInicio, "%d")
        self.mes = datetime.strftime(variablesGlobales.fechaInicio, "%B")
        self.ano = datetime.strftime(variablesGlobales.fechaInicio, "%Y")
        self.hora = datetime.strftime(variablesGlobales.fechaInicio, "%H")
        self.minutos = datetime.strftime(variablesGlobales.fechaInicio, "%M")

    def mostrarFechaInicio(self):
        # Mostrar la fecha de inicio en los inputs correspondientes
        self.select_dia_inicio.setCurrentText(self.dia)
        self.select_mes_inicio.setCurrentText(self.mes)
        self.input_ano_inicio.setText(self.ano)
        self.select_hora_inicio.setCurrentText(self.hora)
        self.select_minutos_inicio.setCurrentText(self.minutos)

    def guardarReserva(self):
        # Capturar la descripción del evento
        descripcion = self.input_descripcion_evento.text()

        # Construir la fecha de inicio con los datos del UI
        dia_inicio = self.select_dia_inicio.currentText()
        mes_inicio = self.select_mes_inicio.currentText()
        ano_inicio = self.input_ano_inicio.text()
        hora_inicio = self.select_hora_inicio.currentText()
        minuto_inicio = self.select_minutos_inicio.currentText()

        # Crear fecha de inicio
        fecha_inicio_str = f"{ano_inicio}-{mes_inicio}-{dia_inicio} {hora_inicio}:{minuto_inicio}"
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%B-%d %H:%M")

        # Determinar la fecha de finalización
        if self.no_duracion_checkbox.isChecked():
            # Sin duración: la fecha final será 1 día después de la fecha de inicio
            fecha_final = fecha_inicio + timedelta(days=1)
        else:
            # Con duración personalizada
            dia_final = self.select_dia_final.currentText()
            mes_final = self.select_mes_final.currentText()
            ano_final = self.input_ano_final.text()
            hora_final = self.select_hora_final.currentText()
            minuto_final = self.select_minuto_final.currentText()

            # Crear fecha de finalización
            fecha_final_str = f"{ano_final}-{mes_final}-{dia_final} {hora_final}:{minuto_final}"
            fecha_final = datetime.strptime(fecha_final_str, "%Y-%B-%d %H:%M")

        # Guardar la reserva en la base de datos con la cédula del usuario
        self.reservas.agregar_reserva(descripcion, fecha_inicio, fecha_final, self.cedula_usuario)
        print("Reserva creada correctamente")

    def cerrarSesion(self):
        # Cerrar la sesión y volver al login
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
    cedula = "123456789"  # Aquí deberías pasar la cédula del usuario autenticado
    GUI = nuevaReservaGUI(cedula)
    GUI.show()
    sys.exit(app.exec_())