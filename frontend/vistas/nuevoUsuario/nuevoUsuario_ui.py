# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevoUsuario.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QFrame{\n"
"background-color: rgb(22,26,23);\n"
"border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 791, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.input_usuario = QLineEdit(self.frame)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setGeometry(QRect(460, 40, 259, 30))
        self.input_usuario.setMinimumSize(QSize(0, 30))
        self.input_usuario.setMaximumSize(QSize(16777215, 16777215))
        self.input_usuario.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_usuario.setMaxLength(50)
        self.input_usuario.setAlignment(Qt.AlignCenter)
        self.input_correo = QLineEdit(self.frame)
        self.input_correo.setObjectName(u"input_correo")
        self.input_correo.setGeometry(QRect(70, 320, 259, 30))
        self.input_correo.setMinimumSize(QSize(0, 30))
        self.input_correo.setMaximumSize(QSize(16777215, 16777215))
        self.input_correo.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_correo.setMaxLength(50)
        self.input_correo.setAlignment(Qt.AlignCenter)
        self.input_nombre = QLineEdit(self.frame)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setGeometry(QRect(80, 40, 259, 30))
        self.input_nombre.setMinimumSize(QSize(0, 30))
        self.input_nombre.setMaximumSize(QSize(16777215, 16777215))
        self.input_nombre.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_nombre.setMaxLength(50)
        self.input_nombre.setAlignment(Qt.AlignCenter)
        self.input_ro = QLineEdit(self.frame)
        self.input_ro.setObjectName(u"input_ro")
        self.input_ro.setGeometry(QRect(460, 150, 259, 30))
        self.input_ro.setMinimumSize(QSize(0, 30))
        self.input_ro.setMaximumSize(QSize(16777215, 16777215))
        self.input_ro.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_ro.setMaxLength(20)
        self.input_ro.setAlignment(Qt.AlignCenter)
        self.input_contrasena = QLineEdit(self.frame)
        self.input_contrasena.setObjectName(u"input_contrasena")
        self.input_contrasena.setGeometry(QRect(80, 160, 259, 30))
        self.input_contrasena.setMinimumSize(QSize(0, 30))
        self.input_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.input_contrasena.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_contrasena.setMaxLength(50)
        self.input_contrasena.setAlignment(Qt.AlignCenter)
        self.input_cedula = QLineEdit(self.frame)
        self.input_cedula.setObjectName(u"input_cedula")
        self.input_cedula.setGeometry(QRect(70, 240, 259, 30))
        self.input_cedula.setMinimumSize(QSize(0, 30))
        self.input_cedula.setMaximumSize(QSize(16777215, 16777215))
        self.input_cedula.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_cedula.setMaxLength(20)
        self.input_cedula.setAlignment(Qt.AlignCenter)
        self.crear_bt_usuario = QPushButton(self.frame)
        self.crear_bt_usuario.setObjectName(u"crear_bt_usuario")
        self.crear_bt_usuario.setGeometry(QRect(480, 530, 93, 28))
        self.input_telefono = QLineEdit(self.frame)
        self.input_telefono.setObjectName(u"input_telefono")
        self.input_telefono.setGeometry(QRect(470, 260, 259, 30))
        self.input_telefono.setMinimumSize(QSize(0, 30))
        self.input_telefono.setMaximumSize(QSize(16777215, 16777215))
        self.input_telefono.setStyleSheet(u"QLineEdit{\n"
"color: black\n"
"font: 12pt \"Arial\";\n"
"}")
        self.input_telefono.setMaxLength(20)
        self.input_telefono.setAlignment(Qt.AlignCenter)
        self.error_label_correo = QLabel(self.frame)
        self.error_label_correo.setObjectName(u"error_label_correo")
        self.error_label_correo.setGeometry(QRect(70, 380, 281, 51))
        self.error_label_correo.setStyleSheet(u"QLabel{\n"
"	background: blue;\n"
"}")
        self.error_label_contrasena = QLabel(self.frame)
        self.error_label_contrasena.setObjectName(u"error_label_contrasena")
        self.error_label_contrasena.setGeometry(QRect(430, 410, 331, 81))
        self.error_label_contrasena.setStyleSheet(u"QLabel{\n"
"	background: blue;\n"
"}")
        self.input_rol = QComboBox(self.frame)
        self.input_rol.addItem("")
        self.input_rol.addItem("")
        self.input_rol.addItem("")
        self.input_rol.setObjectName(u"input_rol")
        self.input_rol.setGeometry(QRect(530, 350, 141, 21))
        self.error_campo_vacio = QLabel(self.frame)
        self.error_campo_vacio.setObjectName(u"error_campo_vacio")
        self.error_campo_vacio.setGeometry(QRect(70, 450, 221, 81))
        self.error_campo_vacio.setStyleSheet(u"QLabel{\n"
"	background: blue;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.input_correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"correo", None))
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.input_ro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rol", None))
        self.input_contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contrase\u00f1a", None))
        self.input_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cedula", None))
        self.crear_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"crear usuarion", None))
        self.input_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"telefono", None))
        self.error_label_correo.setText("")
        self.error_label_contrasena.setText("")
        self.input_rol.setItemText(0, QCoreApplication.translate("MainWindow", u"Administrador", None))
        self.input_rol.setItemText(1, QCoreApplication.translate("MainWindow", u"Estuditante", None))
        self.input_rol.setItemText(2, QCoreApplication.translate("MainWindow", u"Profeso", None))

        self.error_campo_vacio.setText("")
    # retranslateUi

