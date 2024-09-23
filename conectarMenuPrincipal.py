import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.usuario import Usuario, adminUsuario
from conectarReservas import reservasGUI
from conectarMisReservas import misReservasGUI
from connectNuevoUsuario import nuevoUsuarioGUI
from conectarEspacios import espaciosGUI
from conectarUtileria import utileriaGUI
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class menuPrincipalGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/menuPrincipal/menuPrincipal.ui", self)
        
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.reservasGUI)
        self.bt_misreservas_mm.clicked.connect(self.misReservasGUI)
        self.bt_usuarios_mm.clicked.connect(self.usuariosGUI)
        self.bt_espacios_mm.clicked.connect(self.espaciosGUI)
        self.bt_utileria_mm.clicked.connect(self.utileriaGUI)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)

    def menuPrincipalGUI(self):
        from conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI()
        self.login_window.show()
        
    def reservasGUI(self):
        self.close()
        self.login_window = reservasGUI()
        self.login_window.show()
        
        
    def misReservasGUI(self):
        self.close()
        self.login_window = misReservasGUI()
        self.login_window.show()
        
    def usuariosGUI(self):
        self.close()
        self.login_window = nuevoUsuarioGUI()
        self.login_window.show()
        
    def espaciosGUI(self):
        self.close()
        self.login_window = espaciosGUI()
        self.login_window.show()
    
    def utileriaGUI(self):
        self.close()
        self.login_window = utileriaGUI()
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
    GUI = menuPrincipalGUI()
    GUI.show()
    sys.exit(app.exec_())