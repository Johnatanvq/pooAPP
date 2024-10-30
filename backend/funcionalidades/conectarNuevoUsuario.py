import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator, QValidator
from backend.classes.usuario import adminUsuario
from backend.classes.materia import adminMateria
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
from backend.funcionalidades.conectarLogin import loginGUI

import re
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante
import psycopg2

class nuevoUsuarioGUI(QMainWindow):
    def __init__(self, cedula_usuario, id_materia):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/nuevoUsuario/nuevoUsuario.ui", self)
        
        #definición de las expresiones regulares
        self.emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        self.contrasenaRegex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{1,}$'
        
        #se instancia la clase para hacer uso de sus respectivos métodos
        self.nuevoUsuario = adminUsuario()
        self.cedula_usuario = cedula_usuario
        self.materia = adminMateria()
        self.id_materia = id_materia
        #configuración para el filtrado en las búsquedas de usuarios
        self.configurarCompleter()
        
        #se asocia cada elementos con sus funcionalidades
        self.input_correo.textChanged.connect(self.limpiarErrorCorreo)
        self.input_contrasena.textChanged.connect(self.limpiarErrorContrasena)
        self.crear_bt_usuario.clicked.connect(self.crearUsuario)
        self.guardar_bt_usuario.clicked.connect(self.actualizarUsuario)
        self.eliminar_bt_usuario.clicked.connect(self.eliminarUsuario)
        self.editar_bt_usuario.clicked.connect(self.habilitarEdicion)
        self.crear_bt_usuario.clicked.connect(self.crearUsuario)
        self.bt_logout_mm.clicked.connect(self.cerrarSesion)
        self.bt_home_mm.clicked.connect(self.menuPrincipalGUI)
        
    #se asocian atributos de la clase Usuario a las capturas de inputs en la UI
    def capturarTexto(self):
        self.nuevoUsuario.nombre = self.input_nombre.text()
        self.nuevoUsuario.usuario = self.input_usuario.text()
        self.nuevoUsuario.contrasena = self.input_contrasena.text()
        self.nuevoUsuario.cedula = self.input_cedula.text().replace('.','')
        self.nuevoUsuario.email = self.input_correo.text()
        self.nuevoUsuario.telefono = self.input_telefono.text()
        self.nuevoUsuario.rol = self.input_rol.currentText().lower()
    
    #método para validar las expresiones regulares
    def validarTexto(self, regex):
        regularExpression = QRegularExpression(regex)
        regexValidated = QRegularExpressionValidator(regularExpression)
        return regexValidated
        
    #método para crear el usuario
    def crearUsuario(self):
        self.capturarTexto()
        self.input_correo.setValidator(self.validarTexto(self.emailRegex))
        self.input_contrasena.setValidator(self.validarTexto(self.contrasenaRegex))
        correo_valido = self.input_correo.hasAcceptableInput()
        contrasena_valida = self.input_contrasena.hasAcceptableInput()
        
        if not correo_valido or not contrasena_valida:
            if not (self.nuevoUsuario.nombre and
                    self.nuevoUsuario.usuario and 
                    self.nuevoUsuario.contrasena and
                    self.nuevoUsuario.cedula and
                    self.nuevoUsuario.email and
                    self.nuevoUsuario.telefono
                ):
                self.mostrarErrorCampoVacio()
            else:
                self.limpiarErrorCampoVacio()
                
            if not correo_valido:
                self.mostrarErrorCorreo()
            else:
                self.limpiarErrorCorreo()
            
            if not contrasena_valida:
                self.mostrarErrorContrasena()
            else:
                self.limpiarErrorContrasena()

            return  #parar si alguna validación falla

        if self.nuevoUsuario.crearUsuario(
                nombre=self.nuevoUsuario.nombre, 
                usuario=self.nuevoUsuario.usuario, 
                contrasena=self.nuevoUsuario.contrasena, 
                cedula=self.nuevoUsuario.cedula, 
                email=self.nuevoUsuario.email, 
                rol=self.nuevoUsuario.rol, 
                telefono=self.nuevoUsuario.telefono
            ):
            self.limpiarErrorCorreo()
            self.limpiarErrorContrasena()
            
    # métodos para cambiar el texto y el color del label de error a rojo
    def mostrarErrorCorreo(self):
        self.error_label_correo.setText("Ingrese un correo válido")
        self.error_label_correo.setStyleSheet(("""
                                                    color: red;
                                                    font-size: 8pt;
                                                """))
    
    def mostrarErrorContrasena(self):
        self.error_label_contrasena.setText("La contraseña debe\n contener mayúsculas,\n minúsculas y carácteres\n especiales: @#$%^&+=")
        self.error_label_contrasena.setStyleSheet("""
                                                    color: red;
                                                    font-size: 8pt;
                                                """)
    
    def mostrarErrorCampoVacio(self):
        self.error_campo_vacio.setText("Debe llenar todos los campos")
        self.error_campo_vacio.setStyleSheet("""
                                                color: yellow;
                                                text-decoration: bold;
                                            """)
        
    #métodos para limpiar el texto y el estilo del label de error
    def limpiarErrorContrasena(self):
        self.error_label_contrasena.setText("")
        self.error_label_contrasena.setStyleSheet("")
    
    def limpiarErrorCorreo(self):
        self.error_label_correo.setText("")
        self.error_label_correo.setStyleSheet("")
    
    def limpiarErrorCampoVacio(self):
        self.error_campo_vacio.setText("")
        self.error_campo_vacio.setStyleSheet("")
        
    def actualizarUsuario(self):
        if not self.nuevoUsuario.ident:
            print("Error: No se ha especificado un ID de usuario.")
            return
        
        actualizado = self.nuevoUsuario.actualizarUsuario(
            self.nuevoUsuario.ident,
            self.nuevoUsuario.nombre,
            self.nuevoUsuario.usuario,
            self.nuevoUsuario.contrasena,
            self.nuevoUsuario.cedula,
            self.nuevoUsuario.email,
            self.nuevoUsuario.telefono,
            self.nuevoUsuario.rol
        )
        if actualizado:
            print(f"Usuario con ID {self.nuevoUsuario.ident} actualizado correctamente")

    #método para eliminar el usuario, limpia los campos de los input y actualiza el filtro de búsqueda
    def eliminarUsuario(self):
        if self.nuevoUsuario.ident:
            eliminado = self.nuevoUsuario.eliminarUsuario(self.nuevoUsuario.ident)
            if eliminado:
                print(f"Usuario con ID {self.nuevoUsuario.ident} eliminado correctamente")
                self.limpiarCampos()
                self.configurarCompleter()

    def limpiarCampos(self):
        self.input_nombre.clear()
        self.input_usuario.clear()
        self.input_contrasena.clear()
        self.input_cedula.clear()
        self.input_correo.clear()
        self.input_telefono.clear()
        self.input_rol.setCurrentIndex(0)
        self.nuevoUsuario.ident = None

    def configurarCompleter(self):
        usuarios = self.nuevoUsuario.cargarUsuarios()
        completer = QCompleter(usuarios, self)
        completer.setCaseSensitivity(False)
        self.input_filtro_usuarios.setCompleter(completer)
        completer.activated.connect(self.mostrarUsuarioSeleccionado)

    def mostrarUsuarioSeleccionado(self, nombre_usuario):
        detalles_usuario = self.nuevoUsuario.cargarDetallesUsuario(nombre_usuario)
        if detalles_usuario:
            self.nuevoUsuario.ident = detalles_usuario[0]
            self.input_nombre.setText(detalles_usuario[1])
            self.input_usuario.setText(detalles_usuario[2])
            self.input_contrasena.setText(detalles_usuario[3])
            self.input_cedula.setText(detalles_usuario[4])
            self.input_correo.setText(detalles_usuario[5])
            self.input_rol.setCurrentText(detalles_usuario[6].capitalize())
            self.input_telefono.setText(detalles_usuario[7])

            # Desactivar edición
            self.desabilitarEdicion()

    def desabilitarEdicion(self):
        self.input_nombre.setReadOnly(True)
        self.input_usuario.setReadOnly(True)
        self.input_contrasena.setReadOnly(True)
        self.input_cedula.setReadOnly(True)
        self.input_correo.setReadOnly(True)
        self.input_rol.setEnabled(False)
        self.input_telefono.setReadOnly(True)

    def habilitarEdicion(self):
        self.input_nombre.setReadOnly(False)
        self.input_usuario.setReadOnly(False)
        self.input_contrasena.setReadOnly(False)
        self.input_cedula.setReadOnly(False)
        self.input_correo.setReadOnly(False)
        self.input_rol.setEnabled(True)
        self.input_telefono.setReadOnly(False)

    def cerrarSesion(self):
        self.nuevoUsuario.cursor.close()
        self.nuevoUsuario.conexion.close()
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()

    def menuPrincipalGUI(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MenuPrincipalGui
        self.close()
        self.login_window = MenuPrincipalGui(self.cedula_usuario, self.id_materia)
        self.login_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = nuevoUsuarioGUI()
    GUI.show()
    sys.exit(app.exec_())