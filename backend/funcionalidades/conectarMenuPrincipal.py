import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.funcionalidades.conectarReservas import reservasGUI
from backend.funcionalidades.conectarMisReservas import misReservasGUI
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarEspacios import espaciosGUI
from backend.funcionalidades.conectarLogin import loginGUI
from backend.funcionalidades.conectarMaterias import materiaGUI
from backend.classes.usuario import Usuario
class menuPrincipalGUI(QMainWindow):
    def __init__(self, cedula_usuario, id_materia):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/menuPrincipal/menuPrincipal.ui", self)
        
        self.usuario = Usuario()
        self.cedula_usuario = cedula_usuario
        self.id_materia = id_materia
        
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.reservasGUI)
        self.bt_misreservas_mm.clicked.connect(self.misReservasGUI)
        self.bt_usuarios_mm.clicked.connect(self.usuariosGUI)
        self.bt_espacios_mm.clicked.connect(self.espaciosGUI)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)
        self.bt_materias_mm.clicked.connect(self.materiaGUI)

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def reservasGUI(self):
        from backend.funcionalidades.conectarCalendario import calendarioGUI
        self.close()
        self.login_window = calendarioGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def misReservasGUI(self):
        self.close()
        self.login_window = misReservasGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def usuariosGUI(self):
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def espaciosGUI(self):
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
    def materiaGUI(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()
        
    def cerrarSesion(self):
        from backend.funcionalidades.conectarLogin import loginGUI
        
        if hasattr(self.usuario, 'cursor') and self.usuario.cursor:
            self.usuario.cursor.close()
        if hasattr(self.usuario, 'conexion') and self.usuario.conexion:
            self.usuario.conexion.close()
        print("Conexión a la base de datos cerrada")
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = menuPrincipalGUI()
    GUI.show()
    sys.exit(app.exec_())