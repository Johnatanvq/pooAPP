import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.funcionalidades.conectarReservas import reservasGUI
from backend.funcionalidades.conectarMisReservas import misReservasGUI
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarEspacios import espaciosGUI
from backend.funcionalidades.conectarLogin import loginGUI
class menuPrincipalGUI(QMainWindow):
    def __init__(self, cedula_usuario):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/menuPrincipal/menuPrincipal.ui", self)
        
        self.cedula_usuario = cedula_usuario
        
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.reservasGUI)
        self.bt_misreservas_mm.clicked.connect(self.misReservasGUI)
        self.bt_usuarios_mm.clicked.connect(self.usuariosGUI)
        self.bt_espacios_mm.clicked.connect(self.espaciosGUI)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI()
        self.login_window.show()
        
    def reservasGUI(self):
        from backend.funcionalidades.conectarCalendario import calendarioGUI
        self.close()
        self.login_window = calendarioGUI(self.cedula_usuario)
        self.login_window.show()
        
    def misReservasGUI(self):
        self.close()
        self.login_window = misReservasGUI(self.cedula_usuario)
        self.login_window.show()
        
    def usuariosGUI(self):
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario)
        self.login_window.show()
        
    def espaciosGUI(self):
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario)
        self.login_window.show()
        
    def cerrarSesion(self):
        # from conectarLogin import loginGUI
        
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