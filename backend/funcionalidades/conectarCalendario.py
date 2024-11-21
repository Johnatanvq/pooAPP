import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime
import locale, time
# from conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI
from backend.funcionalidades.conectarMisReservas import misReservasGUI
from backend.funcionalidades.conectarEspacios import espaciosGUI
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarMaterias import materiaGUI
from backend import variablesGlobales
from backend.classes.usuario import Usuario

class calendarioGUI(QMainWindow):
    def __init__(self, cedula_usuario, id_materia, es_admin):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/calendario/calendario.ui", self)
        
        self.nuevoUsuario = Usuario()
        self.cedula_usuario = cedula_usuario
        self.id_materia = id_materia
        self.es_admin = es_admin  # True si es admin, False si no
        
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8') 
        self.calendario.selectionChanged.connect(self.capturarFecha)
        
        # Solo visible para admin
        self.bt_usuarios_mm.setVisible(self.es_admin)  
        self.bt_espacios_mm.setVisible(self.es_admin) 
        self.bt_configuraciones_mm.setVisible(self.es_admin)

        # Conectar botones visibles para todos
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_misreservas_mm.clicked.connect(self.misReservas)

        # Conectar botones exclusivos del admin
        self.bt_espacios_mm.clicked.connect(self.espacios)
        self.bt_usuarios_mm.clicked.connect(self.usuarios)
        self.bt_configuraciones_mm.clicked.connect(self.materias)

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
        self.login_window = nuevaReservaGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def misReservas(self):
        self.close()
        self.login_window = misReservasGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
    
    def espacios(self):
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def usuarios(self):
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
    
    def materias(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()

    def cerrarSesion(self): 
        from backend.funcionalidades.conectarLogin import loginGUI
        if hasattr(self.nuevoUsuario, 'cursor') and self.nuevoUsuario.cursor:
            self.nuevoUsuario.cursor.close()
        if hasattr(self.nuevoUsuario, 'conexion') and self.nuevoUsuario.conexion:
            self.nuevoUsuario.conexion.close()
        print("Conexión a la base de datos cerrada")
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()
