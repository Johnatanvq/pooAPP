import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QMovie
from connectLogin import loginGUI

class introGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("../pooAPP/frontend/vistas/intro/intro.ui", self)
        
        self.movie = QMovie("../pooAPP/frontend/imagenes/intro.gif")
        self.intro_gif.setMovie(self.movie)
        self.movie.start()  # Inicia la animación del GIF
        
        self.intro_bt.clicked.connect(self.open_login)

    def open_login(self):
        self.close()
        self.login_window = loginGUI()
        self.login_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = introGUI()
    window.show()
    sys.exit(app.exec_())
