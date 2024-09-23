import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from connectarIntro import introGUI

class main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicioAPP()

    def inicioAPP(self):
        self.intro_window = introGUI()
        self.intro_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main()
    sys.exit(app.exec_())
