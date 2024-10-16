import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.usuario import Usuario, adminUsuario
from backend.funcionalidades.conectarLogin import loginGUI
# from conectarLogin import loginGUI

import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class reservasGUI(QMainWindow):
    def __init__(self, cedula_usuario):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/reservas/reservas.ui", self)
        
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.cedula_usuario = cedula_usuario
        print(f"Cédula del usuario autenticado: {self.cedula_usuario}")
        
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
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = reservasGUI()
    GUI.show()
    sys.exit(app.exec_())