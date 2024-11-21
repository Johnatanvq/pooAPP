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
    def __init__(self, cedula_usuario, id_materia, es_admin):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/menuPrincipal/menuPrincipal.ui", self)
        
        self.nuevoUsuario = Usuario()
        self.cedula_usuario = cedula_usuario
        self.id_materia = id_materia
        self.es_admin = es_admin  # True si es admin, False si es usuario regular

        # Conectar botones visibles usuario normalito
        self.bt_reservas_mm.clicked.connect(self.reservasGUI)
        self.bt_misreservas_mm.clicked.connect(self.misReservasGUI)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)

        # botones exclusivos admin
        self.bt_usuarios_mm.clicked.connect(self.usuariosGUI)
        self.bt_espacios_mm.clicked.connect(self.espaciosGUI)
        self.bt_materias_mm.clicked.connect(self.materiaGUI)

        # Ajustar visibilidad de botones según el tipo de usuario
        self.bt_usuarios_mm.setVisible(self.es_admin)
        self.bt_espacios_mm.setVisible(self.es_admin)
        self.bt_materias_mm.setVisible(self.es_admin)

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def reservasGUI(self):
        from backend.funcionalidades.conectarCalendario import calendarioGUI
        self.close()
        self.login_window = calendarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def misReservasGUI(self):
        self.close()
        self.login_window = misReservasGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def usuariosGUI(self):
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def espaciosGUI(self):
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()

    def materiaGUI(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def cerrarSesion(self):
        if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
            self.nuevoUsuario.cursor.close()
        if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
            self.nuevoUsuario.conexion.close()
        print("Conexión a la base de datos cerrada")

        self.close()
        self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()