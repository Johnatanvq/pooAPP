import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator, QValidator
from backend.classes.usuario import Usuario, adminUsuario
import re
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class nuevoUsuarioGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/nuevoUsuario/nuevoUsuario.ui", self)
        
        self.nuevoUsuario = adminUsuario()

        #para email
        # self.emailRegex = QRegularExpression(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        self.emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        self.contrasenaRegex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{1,}$'

        # Validate strong password
        # re.match(self.contrasenaRegex, 'secret') # Returns None
        # re.match(self.contrasenaRegex, 'Secr3t.')
        
        
        # Aplicar el validador al campo 'login_in_usuario'
        
        # self.login_in_usuario.setValidator(email_validator)
        
        self.crear_bt_usuario.clicked.connect(self.crearUsuario)
        # self.login_in_usuario.textChanged.connect(self.limpiar_error)
        self.input_correo.textChanged.connect(self.limpiar_error_correo)
        self.input_contrasena.textChanged.connect(self.limpiar_error_contrasena)


    def capturar_texto(self):
        self.nuevoUsuario.nombre = self.input_nombre.text()
        self.nuevoUsuario.usuario = self.input_usuario.text()
        self.nuevoUsuario.contrasena = self.input_contrasena.text()
        self.nuevoUsuario.cedula = self.input_cedula.text()
        self.nuevoUsuario.email = self.input_correo.text()
        self.nuevoUsuario.telefono = self.input_telefono.text()
        self.nuevoUsuario.rol = self.input_rol.currentText().lower()
    
    def validar_texto(self, regex):
        regularExpression = QRegularExpression(regex)
        regexValidated = QRegularExpressionValidator(regularExpression)
        return regexValidated
        


    def crearUsuario(self):
        # Capturar el texto antes de autenticar
        self.capturar_texto()
        
        
        # self.email_validador = QRegularExpressionValidator(self.emailRegex)
        # self.input_correo.setValidator(self.email_validador)
        #LAS DE ARRRIBA HACEN LO MISMO PERO MAS FEO
        self.input_correo.setValidator(self.validar_texto(self.emailRegex))
        self.input_contrasena.setValidator(self.validar_texto(self.contrasenaRegex))
        correo_valido = self.input_correo.hasAcceptableInput()
        contrasena_valida = self.input_contrasena.hasAcceptableInput()
        
        if not correo_valido or not contrasena_valida:
        # Mostrar errores específicos según la validación

            if not (self.nuevoUsuario.nombre and
                    self.nuevoUsuario.usuario and 
                    self.nuevoUsuario.contrasena and
                    self.nuevoUsuario.cedula and
                    self.nuevoUsuario.email and
                    self.nuevoUsuario.telefono
                ):
                self.mostrar_error_campoVacio()
            else:
                self.limpiar_error_campo_vacio()
            if not correo_valido:
                self.mostrar_error_correo()
            else:
                self.limpiar_error_correo()
            
            if not contrasena_valida:
                self.mostrar_error_contrasena()
            else:
                self.limpiar_error_contrasena()

            return  # Detener el proceso si alguna validación falla

        # Si ambos son válidos, crear el usuario
        if self.nuevoUsuario.crearUsuario(
                nombre=self.nuevoUsuario.nombre, 
                usuario=self.nuevoUsuario.usuario, 
                contrasena=self.nuevoUsuario.contrasena, 
                cedula=self.nuevoUsuario.cedula, 
                email=self.nuevoUsuario.email, 
                rol=self.nuevoUsuario.rol, 
                telefono=self.nuevoUsuario.telefono
            ):
            self.limpiar_error_correo()
            self.limpiar_error_contrasena()
            
            
    def mostrar_error_correo(self):
        # Cambiar el texto y el color del label de error a rojo
        # self.error_label_contrasena.setText("La contraseña debe contener mayúsculas, minúsculas y carácteres especiales: @#$%^&+=")
        # self.error_label_contrasena.setStyleSheet("color: red") 
        self.error_label_correo.setText("Ingrese un correo válido")
        self.error_label_correo.setStyleSheet("color: red")
    
    def mostrar_error_contrasena(self):
        # Cambiar el texto y el color del label de error a rojo
        self.error_label_contrasena.setText("La contraseña debe contener mayúsculas,\n minúsculas y carácteres especiales: @#$%^&+=")
        self.error_label_contrasena.setStyleSheet("color: red")
        # self.error_label_correo.setText("Ingrese un correo válido")
        # self.error_label_correo.setStyleSheet("color: red") 
    
    def mostrar_error_campoVacio(self):
        # Cambiar el texto y el color del label de error a rojo
        self.error_campo_vacio.setText("Debe llenar todos los campos")
        self.error_campo_vacio.setStyleSheet("color: yellow")
        # self.error_label_correo.setText("Ingrese un correo válido")
        # self.error_label_correo.setStyleSheet("color: red") 

    def limpiar_error_contrasena(self):
        # Limpiar el texto y el estilo del label de error
        # self.error_label_correo.setText("")
        # self.error_label_correo.setStyleSheet("")
        self.error_label_contrasena.setText("")
        self.error_label_contrasena.setStyleSheet("")
    
    def limpiar_error_correo(self):
        # Limpiar el texto y el estilo del label de error
        self.error_label_correo.setText("")
        self.error_label_correo.setStyleSheet("")
        # self.error_label_contrasena.setText("")
        # self.error_label_contrasena.setStyleSheet("")
    
    def limpiar_error_campo_vacio(self):
        # Limpiar el texto y el estilo del label de error
        self.error_campo_vacio.setText("")
        self.error_campo_vacio.setStyleSheet("")
        # self.error_label_contrasena.setText("")
        # self.error_label_contrasena.setStyleSheet("")

    # def mostrar_error(self):
    #     # Cambiar el texto y el color del label de error a rojo
    #     self.error_label.setText("Usuario o contraseña\n incorrectos.\nPor favor, inténtelo de nuevo.")
    #     self.error_label.setStyleSheet("color: red")  # Cambia el color a rojo

    # def limpiar_error(self):
    #     # Limpiar el texto y el estilo del label de error
    #     self.error_label.setText("")
    #     self.error_label.setStyleSheet("")
        
    def closeEvent(self, event):
        # Cerrar la conexión a la base de datos al cerrar la ventana
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("Conexión a la base de datos cerrada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = nuevoUsuarioGUI()
    GUI.show()
    sys.exit(app.exec_())