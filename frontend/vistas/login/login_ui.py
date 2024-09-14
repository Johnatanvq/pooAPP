# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(608, 447)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(22,26,23);\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"QPushButton {\n"
"    border-radius: 18px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgba(0,128,128,255), /* Cian oscuro */\n"
"                                      stop:1 rgba(0,255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.login_label = QLabel(self.frame_superior)
        self.login_label.setObjectName(u"login_label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet(u"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Arial\"; \n"
"}")

        self.horizontalLayout.addWidget(self.login_label)

        self.login_horizontalSpacer = QSpacerItem(102, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.login_horizontalSpacer)

        self.login_bt_minimizar = QPushButton(self.frame_superior)
        self.login_bt_minimizar.setObjectName(u"login_bt_minimizar")
        self.login_bt_minimizar.setMinimumSize(QSize(38, 38))
        self.login_bt_minimizar.setMaximumSize(QSize(38, 38))
        icon = QIcon()
        icon.addFile(u"Imagenes/minus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_bt_minimizar.setIcon(icon)
        self.login_bt_minimizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.login_bt_minimizar)

        self.login_bt_maximizar = QPushButton(self.frame_superior)
        self.login_bt_maximizar.setObjectName(u"login_bt_maximizar")
        self.login_bt_maximizar.setMinimumSize(QSize(38, 38))
        self.login_bt_maximizar.setMaximumSize(QSize(38, 38))
        icon1 = QIcon()
        icon1.addFile(u"Imagenes/plus-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_bt_maximizar.setIcon(icon1)
        self.login_bt_maximizar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.login_bt_maximizar)

        self.login_bt_cerrar = QPushButton(self.frame_superior)
        self.login_bt_cerrar.setObjectName(u"login_bt_cerrar")
        self.login_bt_cerrar.setMinimumSize(QSize(38, 38))
        self.login_bt_cerrar.setMaximumSize(QSize(38, 38))
        icon2 = QIcon()
        icon2.addFile(u"Imagenes/x-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.login_bt_cerrar.setIcon(icon2)
        self.login_bt_cerrar.setIconSize(QSize(38, 38))

        self.horizontalLayout.addWidget(self.login_bt_cerrar)


        self.verticalLayout_2.addWidget(self.frame_superior)

        self.frame_contenido = QFrame(self.frame)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"Arial\"; \n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 18px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:1 , y2:0.5 , stop:0 rgba(0,128,0,255), stop:1 rgba(0,255,0,255)); /* De verde oscuro a verde claro */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    color: rgb(255, 255, 254);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, stop:0 rgba(0,255,255,255), stop:1 rgba(0,128,128,255)); /* De cian claro a cian oscuro */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    color: rgb(255, 255, 254);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(22, 22, 26);\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(114, 117, 126);\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(22, 22, 26);\n"
"    border-radius: 10px;\n"
"    font: 12"
                        "pt \"Arial\";\n"
"    border: 2px solid rgb(44, 182, 125);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(1, 1, 1);\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(127, 90, 240);\n"
"}")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_ingreso = QFrame(self.frame_contenido)
        self.frame_ingreso.setObjectName(u"frame_ingreso")
        self.frame_ingreso.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #04b338;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"")
        self.frame_ingreso.setFrameShape(QFrame.StyledPanel)
        self.frame_ingreso.setFrameShadow(QFrame.Raised)
        self.login_lb_ingresousuario = QLabel(self.frame_ingreso)
        self.login_lb_ingresousuario.setObjectName(u"login_lb_ingresousuario")
        self.login_lb_ingresousuario.setGeometry(QRect(10, 20, 261, 40))
        self.login_lb_ingresousuario.setMinimumSize(QSize(0, 0))
        self.login_lb_ingresousuario.setMaximumSize(QSize(16777215, 40))
        self.login_lb_ingresousuario.setLineWidth(1)
        self.login_lb_ingresousuario.setAlignment(Qt.AlignCenter)
        self.login_label_recuperacioncontrasena = QLabel(self.frame_ingreso)
        self.login_label_recuperacioncontrasena.setObjectName(u"login_label_recuperacioncontrasena")
        self.login_label_recuperacioncontrasena.setGeometry(QRect(30, 230, 231, 21))
        self.login_label_recuperacioncontrasena.setMaximumSize(QSize(16777215, 40))
        self.layoutWidget = QWidget(self.frame_ingreso)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 260, 261, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.login_bt_limpiar = QPushButton(self.layoutWidget)
        self.login_bt_limpiar.setObjectName(u"login_bt_limpiar")
        self.login_bt_limpiar.setMinimumSize(QSize(0, 30))
        self.login_bt_limpiar.setStyleSheet(u"QPushButton{\n"
"border-top-left-radius: 0 px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton:hover{\n"
"border-top-left-radius: 0 px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 0px\n"
"}")

        self.horizontalLayout_3.addWidget(self.login_bt_limpiar)

        self.login_bt_ingresar = QPushButton(self.layoutWidget)
        self.login_bt_ingresar.setObjectName(u"login_bt_ingresar")
        self.login_bt_ingresar.setMinimumSize(QSize(0, 30))
        self.login_bt_ingresar.setStyleSheet(u"QPushButton{\n"
"border-top-left-radius: 0 px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton:hover{\n"
"border-top-left-radius: 0 px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 0px\n"
"}")

        self.horizontalLayout_3.addWidget(self.login_bt_ingresar)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.layoutWidget1 = QWidget(self.frame_ingreso)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 70, 261, 68))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.login_in_usuario = QLineEdit(self.layoutWidget1)
        self.login_in_usuario.setObjectName(u"login_in_usuario")
        self.login_in_usuario.setMinimumSize(QSize(0, 30))
        self.login_in_usuario.setMaximumSize(QSize(16777215, 16777215))
        self.login_in_usuario.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255,255,254);\n"
"font: 12pt \"Arial\";\n"
"}")
        self.login_in_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.login_in_usuario)

        self.login_in_contrasena = QLineEdit(self.layoutWidget1)
        self.login_in_contrasena.setObjectName(u"login_in_contrasena")
        self.login_in_contrasena.setMinimumSize(QSize(0, 30))
        self.login_in_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.login_in_contrasena.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255,255,254);\n"
"font: 12pt \"Arial\";\n"
"}")
        self.login_in_contrasena.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.login_in_contrasena)

        self.error_label = QLabel(self.frame_ingreso)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(10, 150, 261, 71))
        self.error_label.setStyleSheet(u"QLabel#error_label{\n"
"	font: 13pt;\n"
"}")

        self.horizontalLayout_2.addWidget(self.frame_ingreso)

        self.frame_banner = QFrame(self.frame_contenido)
        self.frame_banner.setObjectName(u"frame_banner")
        self.frame_banner.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #04b338;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}")
        self.frame_banner.setFrameShape(QFrame.StyledPanel)
        self.frame_banner.setFrameShadow(QFrame.Raised)
        self.login_imageninstitucional = QLabel(self.frame_banner)
        self.login_imageninstitucional.setObjectName(u"login_imageninstitucional")
        self.login_imageninstitucional.setGeometry(QRect(10, 20, 261, 321))
        self.login_imageninstitucional.setMaximumSize(QSize(16777215, 16777215))
        self.login_imageninstitucional.setPixmap(QPixmap(u"Imagenes/mapauco.jpeg"))
        self.login_imageninstitucional.setAlignment(Qt.AlignCenter)
        self.login_label_linkuco = QLabel(self.frame_banner)
        self.login_label_linkuco.setObjectName(u"login_label_linkuco")
        self.login_label_linkuco.setGeometry(QRect(160, 340, 117, 18))

        self.horizontalLayout_2.addWidget(self.frame_banner)


        self.verticalLayout_2.addWidget(self.frame_contenido)


        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.login_label.setText(QCoreApplication.translate("Login", u"FORMULARIO CON BASE DE DATOS SQLITE", None))
        self.login_bt_minimizar.setText("")
        self.login_bt_maximizar.setText("")
        self.login_bt_cerrar.setText("")
        self.login_lb_ingresousuario.setText(QCoreApplication.translate("Login", u"INGRESO USUARIOS", None))
        self.login_label_recuperacioncontrasena.setText(QCoreApplication.translate("Login", u"\u00bfOlvidaste tu contrase\u00f1a?", None))
        self.login_bt_limpiar.setText(QCoreApplication.translate("Login", u"LIMPIAR", None))
        self.login_bt_ingresar.setText(QCoreApplication.translate("Login", u"INGRESAR", None))
        self.login_in_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.login_in_contrasena.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.error_label.setText("")
        self.login_imageninstitucional.setText("")
        self.login_label_linkuco.setText(QCoreApplication.translate("Login", u"www.uco.edu.co", None))
    # retranslateUi

