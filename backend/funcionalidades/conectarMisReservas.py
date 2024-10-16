import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
#from backend.classes.reserva import Reserva
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
# from conectarLogin import loginGUI
#import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class misReservasGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/misReservas/misReservas.ui", self)
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)

    def cargar_reservas(self):
        try:
            reservas = self.reserva.reservas_por_usuario(self.usuario_activo.cedula)
            #refrescar la tabla
            self.TablaReservas.setRowCount(0)
        #cargar la información
            for reserva in reservas:
                fila = self.TablaReservas.rowCount()
                self.TablaReservas.inserRow(fila)
                
                self.TablaReservas.setItem(fila, 0, QTableWidgetItem(str(reserva[0])))  # cedula usuario
                self.TablaReservas.setItem(fila, 1, QTableWidgetItem(reserva[2].strftime("%Y-%m-%d %H:%M")))  # Fecha_inicio
                self.TablaReservas.setItem(fila, 2, QTableWidgetItem(reserva[3].strftime("%Y-%m-%d %H:%M")))  # Fecha_fin
                self.TablaReservas.setItem(fila, 3, QTableWidgetItem(reserva[1]))  # Descripcion
                self.TablaReservas.setItem(fila, 4, QTableWidgetItem(reserva[4]))

        except Exception as e:
            QMessageBox.critical (self, "Error", f"No se pudieron cargar las reservas: {str(e)}")

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui

        self.close()
        self.login_window = MenuPrincipalGui()
        self.login_window.show()

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
    GUI = misReservasGUI()
    GUI.show()
    sys.exit(app.exec_())