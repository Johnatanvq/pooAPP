import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.funcionalidades.conectarIntro import introGUI

class main(QMainWindow):
    def __init__(self, cedula_usuario, id_materia):
        super().__init__()
        self.cedula_usuario = cedula_usuario
        self.id_materia = id_materia
        self.inicioAPP()

    def inicioAPP(self):
        self.intro_window = introGUI()
        self.intro_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cedula_usuario = '1'
    id_materia = '2'
    window = main(cedula_usuario, id_materia)
    sys.exit(app.exec_())
