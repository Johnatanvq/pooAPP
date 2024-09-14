import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.classes.usuario import Usuario, adminUsuario
import bcrypt #hashes para encriptar las contraseñas, se puede dejar para más adelante

class loginGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/login.ui", self)
        
        self.usuario = Usuario()
        self.login_bt_ingresar.clicked.connect(self.autenticar)
        
        self.login_in_usuario.textChanged.connect(self.limpiar_error)
        self.login_in_contrasena.textChanged.connect(self.limpiar_error)

    def capturar_texto(self):
        # Capturar el texto de los campos de entrada
        self.usuario.nombre = self.login_in_usuario.text()  # Asigna el valor al atributo de la clase Usuario
        self.usuario.contrasena = self.login_in_contrasena.text()
        print(f"Texto capturado del usuario: {self.usuario.nombre}")
        print(f"Texto capturado de la contraseña: {self.usuario.contrasena}")

    def autenticar(self):
        # Capturar el texto antes de autenticar
        self.capturar_texto()

        # Llamar al método de autenticación de la clase Usuario
        if self.usuario.autenticarUsuario():
            self.limpiar_error()
        else:
            self.mostrar_error()

    def closeEvent(self, event):
        # Cerrar la conexión a la base de datos al cerrar la ventana
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("Conexión a la base de datos cerrada")
    
    def mostrar_error(self):
        # Cambiar el texto y el color del label de error a rojo
        self.error_label.setText("Usuario o contraseña\n incorrectos.\nPor favor, inténtelo de nuevo.")
        self.error_label.setStyleSheet("color: red")  # Cambia el color a rojo

    def limpiar_error(self):
        # Limpiar el texto y el estilo del label de error
        self.error_label.setText("")
        self.error_label.setStyleSheet("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = loginGUI()
    GUI.show()
    sys.exit(app.exec_())