import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.materia import adminMateria
from backend.classes.usuario import adminUsuario
# from backend.funcionalidades.conectarMaterias import materiaGUI
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class materiaGUI(QMainWindow):
    def __init__(self, id_materia, cedula_usuario, es_admin):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/materias/materias.ui", self)
        
        self.id_materia = id_materia
        self.cedula_usuario = cedula_usuario
        self.es_admin = es_admin  # True si es admin, False si no

        # Solo visible para admin
        self.bt_usuarios_mm.setVisible(self.es_admin)
        self.bt_espacios_mm.setVisible(self.es_admin)

        # Conección botones
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.misReservas)
        self.bt_espacios_mm.clicked.connect(self.espacios)
        self.bt_usuarios_mm.clicked.connect(self.usuarios)
        self.bt_misreservas_mm.clicked.connect(self.reservados)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)
        
        #definición de las expresiones regulares
        self.idmateriaRegex = r'^[A-Za-z0-9]+$' #Letras y numeros
        self.nombreRegex = r'^[A-Za-z\s]+$' #Letras
        self.intensidadRegex = r'^[0-9]+$' #numeros

        self.materia = adminMateria()
        self.id_materia = id_materia
        self.cedula_usuario = cedula_usuario

        # Configurar expresiones regulares
        self.intensidadRegex = r'^[0-9]+$'
        
        # Configurar filtro
        self.configurarCompleter()
        
        # Asignar funciones a botones
        self.crear_bt_materia.clicked.connect(self.crearMateria)
        self.guardar_bt_materia.clicked.connect(self.actualizarMateria)
        self.eliminar_bt_materia.clicked.connect(self.eliminarMateria)
        self.editar_bt_materia.clicked.connect(self.habilitarEdicion)
    
    def capturarTexto(self):
        self.materia.id_materia = self.input_idmateria.text()
        self.materia.nombre_materia = self.input_nombremateria.text()
        self.materia.programa = self.input_programa.text()
        self.materia.intensidad_horaria = self.input_intensidadhoraria.text()

    def validarTexto(self, regex):
        regularExpression = QRegularExpression(regex)
        regexValidated = QRegularExpressionValidator(regularExpression)
        return regexValidated

    def crearMateria(self):
        self.capturarTexto()
        self.input_intensidadhoraria.setValidator(self.validarTexto(self.intensidadRegex))
        
        if self.input_intensidadhoraria.hasAcceptableInput():
            if self.materia.crearMateria(
                    id_materia=self.materia.id_materia,
                    nombre_materia=self.materia.nombre_materia,
                    programa=self.materia.programa,
                    intensidad_horaria=self.materia.intensidad_horaria):
                print("Materia creada correctamente.")
                self.limpiarCampos()
                self.configurarCompleter()
        else:
            self.mostrarErrorIntensidad()

    def mostrarErrorIntensidad(self):
        self.error_label_intensidad.setText("La intensidad horaria debe ser un número válido.")
        self.error_label_intensidad.setStyleSheet("color:red;font-size: 8pt;")
        
    def limpiarErrorIntensidad(self):
        self.error_label_intensidad.setText("")
        self.error_label_intensidad.setStyleSheet("")

    def actualizarMateria(self):
        if not self.materia.id_materia:
            print("Error: No se ha especificado un ID de materia válido.")
            return

        self.capturarTexto()
        if self.materia.actualizarMateria(
            id_materia=self.materia.id_materia,
            nombre_materia=self.materia.nombre_materia,
            programa=self.materia.programa,
            intensidad_horaria=self.materia.intensidad_horaria):
            print(f"Materia {self.materia.id_materia} actualizada correctamente.")
            self.limpiarCampos()
            self.configurarCompleter()

    def eliminarMateria(self):
        if self.materia.id_materia:
            if self.materia.eliminarMateria(self.materia.id_materia):
                print(f"Materia {self.materia.id_materia} eliminada correctamente.")
                self.limpiarCampos()
                self.configurarCompleter()
    
    def limpiarCampos(self):
        self.input_idmateria.clear()
        self.input_nombremateria.clear()
        self.input_programa.clear()
        self.input_intensidadhoraria.clear()
        self.materia.id_materia = None
        self.limpiarErrorIntensidad()

    def configurarCompleter(self):
        materias = self.materia.cargarMaterias()
        completer = QCompleter(materias, self)
        completer.setCaseSensitivity(False)
        self.input_filtro_materias.setCompleter(completer)
        completer.activated.connect(self.mostrarMateriaSeleccionada)

    def mostrarMateriaSeleccionada(self, nombre_materia):
        detalles_materia = self.materia.cargarDetallesMaterias(nombre_materia)
        if detalles_materia:
            self.materia.id_materia = detalles_materia[0]
            self.input_idmateria.setText(detalles_materia[0])
            self.input_nombremateria.setText(detalles_materia[1])
            self.input_programa.setText(detalles_materia[2])
            self.input_intensidadhoraria.setText(str(detalles_materia[3]))
            self.desabilitarEdicion()

    def habilitarEdicion(self):
        self.input_idmateria.setReadOnly(False)
        self.input_nombremateria.setReadOnly(False)
        self.input_programa.setReadOnly(False)
        self.input_intensidadhoraria.setReadOnly(False)

    def desabilitarEdicion(self):
        self.input_idmateria.setReadOnly(True)
        self.input_nombremateria.setReadOnly(True)
        self.input_programa.setReadOnly(True)
        self.input_intensidadhoraria.setReadOnly(True)

    def habilitarEdicion(self):
        self.input_idmateria.setReadOnly(False)
        self.input_nombremateria.setReadOnly(False)
        self.input_programa.setReadOnly(False)
        self.input_intensidadhoraria.setReadOnly(False)

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()

    def misReservas(self):
        from backend.funcionalidades.conectarCalendario import calendarioGUI
        self.close()
        self.login_window = calendarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def reservados(self):
        from backend.funcionalidades.conectarMisReservas import misReservasGUI
        self.close()
        self.login_window = misReservasGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
    
    def espacios(self):
        from backend.funcionalidades.conectarEspacios import espaciosGUI
        self.close()
        self.login_window = espaciosGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def usuarios(self):
        from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()

    def materias(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia)
        self.login_window.show()

    def cerrarSesion(self):
        from backend.funcionalidades.conectarLogin import loginGUI
        if hasattr(self.materia, 'cursor') and self.materia.cursor:
            self.materia.cursor.close()
        if hasattr(self.materia, 'conexion') and self.materia.conexion:
            self.materia.conexion.close()
        print("Conexión a la base de datos cerrada")
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()