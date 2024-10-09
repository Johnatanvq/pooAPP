import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator
from backend.classes.usuario import Usuario, adminUsuario
# from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MPGUI
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class loginGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/login/login.ui", self)
        
        self.usuario = Usuario()
        self.login_bt_ingresar.clicked.connect(self.autenticar)
        self.login_in_usuario.textChanged.connect(self.limpiarError)
        self.login_in_contrasena.textChanged.connect(self.limpiarError)

    def capturarTexto(self):
        # Capturar el texto de los campos de entrada
        self.usuario.nombre = self.login_in_usuario.text()  # Asigna el valor al atributo de la clase Usuario
        self.usuario.contrasena = self.login_in_contrasena.text()
        print(f"Texto capturado del usuario: {self.usuario.nombre}")
        print(f"Texto capturado de la contraseña: {self.usuario.contrasena}")

    def autenticar(self):
        self.capturarTexto() # Capturar el texto antes de autenticar

        # llama al método de autenticación de la clase Usuario
        if self.usuario.autenticarUsuario():
            self.limpiarError()
            self.abrirMenuPrincipal()
        else:
            self.mostrarError()

    def mostrarError(self):
        # Cambiar texto y estilos
        self.error_label.setText("Usuario o contraseña\n incorrectos.\nPor favor, inténtelo de nuevo.")
        self.error_label.setStyleSheet("color: red")

    def limpiarError(self):
        # Limpiar texto y estilos
        self.error_label.setText("")
        self.error_label.setStyleSheet("")
        
    def abrirMenuPrincipal(self):
        from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI as MPGUI

        self.close()
        self.login_window = MPGUI()
        self.login_window.show()
        
    # def closeEvent(self, event):
    #     # Cerrar la conexión a la base de datos al cerrar la ventana
    #     if self.cursor:
    #         self.cursor.close()
    #     if self.conexion:
    #         self.conexion.close()
    #     print("Conexión a la base de datos cerrada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = loginGUI()
    GUI.show()
    sys.exit(app.exec_())