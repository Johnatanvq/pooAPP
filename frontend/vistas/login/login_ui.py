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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(1003, 587)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_ingreso = QFrame(self.centralwidget)
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
        self.verticalLayout_3 = QVBoxLayout(self.frame_ingreso)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.login_imageninstitucional = QLabel(self.frame_ingreso)
        self.login_imageninstitucional.setObjectName(u"login_imageninstitucional")
        self.login_imageninstitucional.setMaximumSize(QSize(16777215, 16777215))
        self.login_imageninstitucional.setPixmap(QPixmap(u"../../imagenes/logo-altacalidad-uco.png"))
        self.login_imageninstitucional.setScaledContents(True)
        self.login_imageninstitucional.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.login_imageninstitucional)

        self.horizontalSpacer_2 = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_lb_ingresousuario = QLabel(self.frame_ingreso)
        self.login_lb_ingresousuario.setObjectName(u"login_lb_ingresousuario")
        self.login_lb_ingresousuario.setMinimumSize(QSize(0, 0))
        self.login_lb_ingresousuario.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.login_lb_ingresousuario.setFont(font)
        self.login_lb_ingresousuario.setLineWidth(1)
        self.login_lb_ingresousuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.login_lb_ingresousuario)

        self.login_in_usuario = QLineEdit(self.frame_ingreso)
        self.login_in_usuario.setObjectName(u"login_in_usuario")
        self.login_in_usuario.setMinimumSize(QSize(0, 30))
        self.login_in_usuario.setMaximumSize(QSize(16777215, 16777215))
        self.login_in_usuario.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(245, 245, 245);  /* Fondo gris claro para destacar en un fondo blanco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando se pasa el mouse por encima */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(100, 149, 237);  /* Color azul claro en hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene el foco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(0, 122, 204);    /* Color azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"}\n"
"")
        self.login_in_usuario.setMaxLength(20)
        self.login_in_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.login_in_usuario)

        self.login_in_contrasena = QLineEdit(self.frame_ingreso)
        self.login_in_contrasena.setObjectName(u"login_in_contrasena")
        self.login_in_contrasena.setMinimumSize(QSize(0, 30))
        self.login_in_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.login_in_contrasena.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(245, 245, 245);  /* Fondo gris claro para destacar en un fondo blanco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando se pasa el mouse por encima */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(100, 149, 237);  /* Color azul claro en hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene el foco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(0, 122, 204);    /* Color azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"}\n"
"\n"
"")
        self.login_in_contrasena.setMaxLength(20)
        self.login_in_contrasena.setEchoMode(QLineEdit.Password)
        self.login_in_contrasena.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.login_in_contrasena)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.error_label = QLabel(self.frame_ingreso)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setStyleSheet(u"QLabel#error_label{\n"
"	font: 13pt;\n"
"}")

        self.verticalLayout_3.addWidget(self.error_label)

        self.verticalSpacer = QSpacerItem(20, 138, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.login_bt_ingresar = QPushButton(self.frame_ingreso)
        self.login_bt_ingresar.setObjectName(u"login_bt_ingresar")
        self.login_bt_ingresar.setMinimumSize(QSize(0, 30))
        self.login_bt_ingresar.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,2"
                        "55,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.login_bt_ingresar)

        self.login_label_linkuco = QLabel(self.frame_ingreso)
        self.login_label_linkuco.setObjectName(u"login_label_linkuco")

        self.verticalLayout_2.addWidget(self.login_label_linkuco)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.frame_ingreso, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.login_imageninstitucional.setText("")
        self.login_lb_ingresousuario.setText(QCoreApplication.translate("Login", u"INGRESO USUARIOS", None))
        self.login_in_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.login_in_contrasena.setText("")
        self.login_in_contrasena.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.error_label.setText("")
        self.login_bt_ingresar.setText(QCoreApplication.translate("Login", u"INGRESAR", None))
        self.login_label_linkuco.setText(QCoreApplication.translate("Login", u"www.uco.edu.co", None))
    # retranslateUi

