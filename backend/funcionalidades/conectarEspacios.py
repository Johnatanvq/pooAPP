import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.espacio import adminEspacio
from backend.classes.reserva import Reservas
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarMaterias import materiaGUI
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante
class espaciosGUI(QtWidgets.QMainWindow):
    def __init__(self, cedula_usuario, id_materia, es_admin):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/espacios/espacios.ui", self)
        self.cedula_usuario = cedula_usuario
        self.id_materia = id_materia
        self.es_admin = es_admin  # True si es admin, False si no

        # Solo visible para admin
        self.bt_usuarios_mm.setVisible(self.es_admin)

        # Conectar botones
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        self.bt_reservas_mm.clicked.connect(self.misReservas)
        self.bt_configuraciones_mm.clicked.connect(self.materias)
        self.bt_misreservas_mm.clicked.connect(self.reservados)
        self.bt_usuarios_mm.clicked.connect(self.usuarios)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)
        self.editar_bt_espacio.clicked.connect(self.habilitarEdicion)
        self.eliminar_bt_espacio.clicked.connect(self.eliminarEspacio)
        

        # Configurar expresiones regulares y botones
        self.idespacioRegex = r'^[A-Za-z0-9]+$'  # Letras y números
        self.bloqueRegex = r'^[A-Za-z0-9]+$'  # Letras
        self.capacidadRegex = r'^[0-9]+$'  # Números

        self.espacio = adminEspacio()
        self.configurarCompleter()
        self.crear_bt_espacio.clicked.connect(self.crearEspacio)
        self.guardar_bt_espacio.clicked.connect(self.actualizarEspacio)
        self.eliminar_bt_espacio.clicked.connect(self.eliminarEspacio)
        self.editar_bt_espacio.clicked.connect(self.habilitarEdicion)

        # Configuración del filtro para la búsqueda de espacios
        
    def capturarTexto(self):
        self.espacio.nombre = self.input_idespacio.text()
        self.espacio.bloque = self.input_bloque.text()
        self.espacio.capacidad = self.input_capacidad.text()
        self.espacio.tipo = self.input_tipo.text().lower()

    def validarTexto(self, regex):
        regularExpression = QRegularExpression(regex)
        regexValidated = QRegularExpressionValidator(regularExpression)
        return regexValidated
    
    def crearEspacio (self):
        self.capturarTexto()
        self.input_capacidad.setValidator(self.validarTexto(self.capacidadRegex))
        capacidad_valida = self.input_capacidad.hasAcceptableInput()

        if not capacidad_valida:
            self.mostrarErrorCapacidad()
            return
        
        if self.espacio.crearEspacio(
            nombre=self.espacio.nombre,
            bloque=self.espacio.bloque,
            capacidad=self.espacio.capacidad,
            tipo=self.espacio.tipo
        ):
            self.limpiarCampos()

    #metodo para mostrar errores
    def mostrarErrorCapacidad(self):
        self.error_label_capacidad.setText("La capacidad debe ser un número válido")
        self.error_label_capacidad.setStyleSheet("color:red;font-size: 8pt;")
    def limpiarErrorCapacidad(self):
        self.error_label_capacidad.setText("")
        self.error_label_capacidad.setStyleSheet("")
    
    #metodo para actualizar estado
    def actualizarEspacio(self):
        # if not self.espacio.nombre:
        #     print("Error: No se ha especificado un nombre de espacio válido")
        #     return
        
        self.capturarTexto()
        actualizado = self.espacio.actualizarEspacio(
            self.espacio.nombre,
            self.espacio.bloque,
            self.espacio.capacidad,
            self.espacio.tipo
        )
        if actualizado: 
            print(f"El espacio {self.espacio.nombre} ha sido actualizado correctamente")
            self.limpiarCampos()
            self.configurarCompleter()
        
    def eliminarEspacio(self):
        self.capturarTexto()
        if self.espacio.nombre:
            eliminado = self.espacio.eliminarEspacio(self.espacio.nombre)
            if eliminado:
                print(f"El espacio {self.espacio.nombre} se ha eliminado correctamente ")
                self.limpiarCampos()
                self.configurarCompleter()

    def limpiarCampos(self):
        self.input_idespacio.clear()
        self.input_bloque.clear()
        self.input_capacidad.clear()
        self.input_tipo.clear()
        self.espacio.nombre = None

    def configurarCompleter(self):
        espacios = self.espacio.cargarEspacio()
        completer = QCompleter(espacios, self)
        completer.setCaseSensitivity(False)
        self.input_filtro_espacios.setCompleter(completer)
        completer.activated.connect(self.mostrarEspacioSeleccionado)

    def mostrarEspacioSeleccionado(self, nombre_espacio):
        detalles_espacio = self.espacio.cargarDetallesEspacio(nombre_espacio)
        if detalles_espacio:
            self.espacio.ident = detalles_espacio[0]
            self.input_idespacio.setText(detalles_espacio[0])
            self.input_bloque.setText(detalles_espacio[1])
            self.input_capacidad.setText(str(detalles_espacio[2]))
            self.input_tipo.setText(detalles_espacio[3])
            self.desabilitarEdicion()

    def desabilitarEdicion(self):
        self.input_idespacio.setReadOnly(True)
        self.input_bloque.setReadOnly(True)
        self.input_capacidad.setReadOnly(True)
        self.input_tipo.setReadOnly(True)

    def habilitarEdicion(self):
        self.input_idespacio.setReadOnly(False)
        self.input_bloque.setReadOnly(False)
        self.input_capacidad.setReadOnly(False)
        self.input_tipo.setReadOnly(False)
        
        
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
        self.close()
        self.login_window = nuevoUsuarioGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()

    def materias(self):
        self.close()
        self.login_window = materiaGUI(self.cedula_usuario, self.id_materia, self.es_admin)
        self.login_window.show()
        
    def cerrarSesion(self):
        from backend.funcionalidades.conectarLogin import loginGUI
        if hasattr(self.espacio, 'cursor') and self.espacio.cursor:
            self.espacio.cursor.close()
        if hasattr(self.espacio, 'conexion') and self.espacio.conexion:
            self.espacio.conexion.close()
        print("Conexión a la base de datos cerrada")
        
        #redirigir login
        self.close()
        self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()