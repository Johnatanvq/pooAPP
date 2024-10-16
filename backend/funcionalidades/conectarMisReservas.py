import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.reserva import Reservas
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
# from conectarLogin import loginGUI
#import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class misReservasGUI(QMainWindow):
    def __init__(self, cedula_usuario):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/misReservas/misReservas.ui", self)
        self.cedula_usuario = cedula_usuario  # La cédula del usuario logueado se recibe al inicializar
        self.reserva = Reservas()  # Instanciar la clase que gestiona las reservas
        self.cargar_reservas()
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)

    def cargar_reservas(self):
        try:
            # Obtener las reservas del usuario por su cédula
            reservas = self.reserva.obtener_reservas_por_usuario(self.cedula_usuario)
            
            # Refrescar la tabla
            self.TablaReservas.setRowCount(0)
            
            # Cargar la información en la tabla
            for reserva in reservas:
                fila = self.TablaReservas.rowCount()
                self.TablaReservas.insertRow(fila)
                
                # Asignar los datos a las columnas correspondientes
                self.TablaReservas.setItem(fila, 0, QTableWidgetItem(reserva['cedula']))  # Cédula usuario
                self.TablaReservas.setItem(fila, 1, QTableWidgetItem(reserva['descripcion']))  # Descripción
                self.TablaReservas.setItem(fila, 2, QTableWidgetItem(reserva['fecha_inicio'].strftime("%Y-%m-%d %H:%M")))  # Fecha_inicio
                self.TablaReservas.setItem(fila, 3, QTableWidgetItem(reserva['fecha_final'].strftime("%Y-%m-%d %H:%M")))  # Fecha_final

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudieron cargar las reservas: {str(e)}")

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
        
        self.close()
        self.menu_window = MenuPrincipalGui()
        self.menu_window.show()

    # def cerrarSesion(self):
    #     #se cierra la conexión a la base de datos desde la clase Usuario
    #     if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
    #         self.nuevoUsuario.cursor.close()
    #     if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
    #         self.nuevoUsuario.conexion.close()
    #     print("Conexión a la base de datos cerrada")
        
    #     #redirigir login
    #     self.close()
    #     self.login_window = loginGUI()  # Instanciar la ventana de login
    #     self.login_window.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = misReservasGUI()
    GUI.show()
    sys.exit(app.exec_())