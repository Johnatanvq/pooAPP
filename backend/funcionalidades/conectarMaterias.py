import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.materia import adminMateria
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class materiaGUI(QtWidgets.QMainWindow):
    def __init__(self, id_materia):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/materias/materias.ui", self)
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)

        #definición de las expresiones regulares
        self.idmateriaRegex = r'^[A-Za-z0-9]+$' #Letras y numeros
        self.nombreRegex = r'^[A-Za-z\s]+$' #Letras
        self.instensidadRegex = r'^[0-9]+$' #numeros

        self.materia = adminMateria()

        self.crear_bt_materia.clicked.connect(self.crearMateria)
        self.guardar_bt_materia.clicked.connect(self.actualizarMateria)
        self.eliminar_bt_materia.clicked.connect(self.eliminarMateria)
        self.editar_bt_materia.clicked.connect(self.habilitarEdicion)

        #configuracion del filtro para la busqueda de espacios
        self.configurarCompleter()
    def capturarTexto(self):
        self.materia.id_materia = self.input_idmateria.text()
        self.materia.nombre_materia = self.input_nombre.text()
        self.materia.programa = self.input_programa.text()
        self.materia.intensidad_horaria = self.input_intensidad.text()

    def validarTexto(self, regex):
        regularExpression = QRegularExpression(regex)
        regexValidated = QRegularExpressionValidator(regularExpression)
        return regexValidated
    
    def crearMateria(self):
        self.capturarTexto()
        self.input_intensidad.setValidator(self.validarTexto(self.intensidadRegex))
        intensidad_valida = self.input_intensidad.hasAcceptableInput()

        if not intensidad_valida:
            self.mostrarErrorIntensidad()
            return

        if self.materia.crearMateria(
            id_materia=self.materia.id_materia,
            nombre_materia=self.materia.nombre_materia,
            programa=self.materia.programa,
            intensidad_horaria=self.materia.intensidad_horaria
        ):
            self.limpiarCampos()

    #metodo para mostrar errores
    def mostrarErrorIntensidad(self):
        self.error_label_intensidad.setText("La intensidad horaria debe ser un número válido")
        self.error_label_intensidad.setStyleSheet("color:red;font-size: 8pt;")
    def limpiarErrorCapacidad(self):
        self.error_label_intensidad.setText("")
        self.error_label_intensidad.setStyleSheet("")
    
    #metodo para actualizar estadio
    def actualizarMateria(self):
        if not self.materia.id_materia:
            print("Error: No se ha especificado un ID de materia válido")
            return

        self.capturarTexto()
        actualizado = self.materia.actualizarMateria(
            self.materia.id_materia,
            self.materia.nombre_materia,
            self.materia.programa,
            self.materia.intensidad_horaria
        )
        if actualizado:
            print(f"Materia {self.materia.id_materia} actualizada correctamente")
            self.limpiarCampos()
        
    def eliminarMateria(self):
        if self.materia.id_materia:
            eliminado = self.materia.eliminarMateria(self.materia.id_materia)
            if eliminado:
                print(f"Materia {self.materia.id_materia} eliminada correctamente")
                self.limpiarCampos()
                self.configurarCompleter()

    def limpiarCampos(self):
        self.input_idmateria.clear()
        self.input_nombre.clear()
        self.input_programa.clear()
        self.input_intensidad.clear()
        self.materia.id_materia = None

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
            self.input_nombre.setText(detalles_materia[1])
            self.input_programa.setText(detalles_materia[2])
            self.input_intensidad.setText(str(detalles_materia[3]))
            self.desabilitarEdicion()

    def desabilitarEdicion(self):
        self.input_idmateria.setReadOnly(True)
        self.input_nombre.setReadOnly(True)
        self.input_programa.setReadOnly(True)
        self.input_intensidad.setReadOnly(True)

    def habilitarEdicion(self):
        self.input_idmateria.setReadOnly(False)
        self.input_nombre.setReadOnly(False)
        self.input_programa.setReadOnly(False)
        self.input_intensidad.setReadOnly(False)

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
        self.close()
        self.login_window = menuPrincipalGUI(self.cedula_usuario)
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
        #self.login_window = loginGUI()  # Instanciar la ventana de login
        self.login_window.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MateriaGUI()
    GUI.show()
    sys.exit(app.exec_())