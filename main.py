import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from backend.funcionalidades.conectarIntro import introGUI
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI
from backend.funcionalidades.conectarCalendario import calendarioGUI
from backend.funcionalidades.conectarLogin import loginGUI
from backend.funcionalidades.conectarMenuPrincipal import menuPrincipalGUI
from backend.funcionalidades.conectarNuevoUsuario import nuevoUsuarioGUI
from backend.funcionalidades.conectarReservas import reservasGUI
from backend.funcionalidades.conectarMisReservas import misReservasGUI
from backend.funcionalidades.conectarUtileria import utileriaGUI
from backend.funcionalidades.conectarEspacios import espacioGUI
from backend.funcionalidades.conectarNuevaReserva import nuevaReservaGUI

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicioAPP()

    def inicioAPP(self):
        # self.intro_window = nuevaReservaGUI()
        # self.intro_window = menuPrincipalGUI()
        # self.intro_window = loginGUI()
        # self.intro_window = nuevoUsuarioGUI()
        # self.intro_window = introGUI()
        self.intro_window = reservasGUI()
        #self.intro_window = espaciosGUI()
        self.intro_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())
