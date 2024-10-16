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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(612, 462)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 610, 444))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(22,26,23);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Arial\"; \n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.main_menu = QWidget(self.frame)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(140, 10, 461, 431))
        self.main_menu.setStyleSheet(u"\n"
"background-color: \n"
"rgb(255, 255, 255)")
        self.bt_cerrarlistado_mm = QPushButton(self.main_menu)
        self.bt_cerrarlistado_mm.setObjectName(u"bt_cerrarlistado_mm")
        self.bt_cerrarlistado_mm.setGeometry(QRect(10, 10, 51, 21))
        self.bt_cerrarlistado_mm.setStyleSheet(u"QPushButton {\n"
"    border-radius: 18px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QPushButton:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"   \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 255, 0, 255); /* Verde claro cuando se presiona */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cerrarlistado_mm.setIcon(icon)
        self.bt_cerrarlistado_mm.setCheckable(True)
        self.frame_ingreso = QFrame(self.main_menu)
        self.frame_ingreso.setObjectName(u"frame_ingreso")
        self.frame_ingreso.setGeometry(QRect(10, 80, 441, 291))
        self.frame_ingreso.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #04b338;\n"
"}\n"
"\n"
"QLabel {\n"
"    border: none;\n"
"}\n"
"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit {\n"
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
        self.frame_ingreso.setFrameShape(QFrame.StyledPanel)
        self.frame_ingreso.setFrameShadow(QFrame.Raised)
        self.layoutWidget_8 = QWidget(self.frame_ingreso)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(10, 20, 261, 276))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.input_nombre = QLineEdit(self.layoutWidget_8)
        self.input_nombre.setObjectName(u"input_nombre")
        self.input_nombre.setMinimumSize(QSize(0, 30))
        self.input_nombre.setMaximumSize(QSize(16777215, 16777215))
        self.input_nombre.setStyleSheet(u"QLineEdit {\n"
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
        self.input_nombre.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_nombre)

        self.input_usuario = QLineEdit(self.layoutWidget_8)
        self.input_usuario.setObjectName(u"input_usuario")
        self.input_usuario.setMinimumSize(QSize(0, 30))
        self.input_usuario.setMaximumSize(QSize(16777215, 16777215))
        self.input_usuario.setStyleSheet(u"QLineEdit {\n"
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
        self.input_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_usuario)

        self.input_contrasena = QLineEdit(self.layoutWidget_8)
        self.input_contrasena.setObjectName(u"input_contrasena")
        self.input_contrasena.setMinimumSize(QSize(0, 30))
        self.input_contrasena.setMaximumSize(QSize(16777215, 16777215))
        self.input_contrasena.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.input_contrasena.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_contrasena)

        self.input_rol = QComboBox(self.layoutWidget_8)
        self.input_rol.addItem("")
        self.input_rol.addItem("")
        self.input_rol.addItem("")
        self.input_rol.setObjectName(u"input_rol")
        self.input_rol.setStyleSheet(u"QComboBox {\n"
"    background-color: rgb(245, 245, 245);  /* Fondo gris claro para destacar en un fondo blanco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando se pasa el mouse por encima */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(100, 149, 237);  /* Color azul claro en hover */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene el foco */\n"
"    border-radius: 10px;\n"
"    font: 12pt \"Arial\";\n"
"    border: 2px solid rgb(0, 122, 204);    /* Color azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"}")
        self.input_rol.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.input_rol.setFrame(True)

        self.verticalLayout_7.addWidget(self.input_rol)

        self.input_cedula = QLineEdit(self.layoutWidget_8)
        self.input_cedula.setObjectName(u"input_cedula")
        self.input_cedula.setMinimumSize(QSize(0, 30))
        self.input_cedula.setMaximumSize(QSize(16777215, 16777215))
        self.input_cedula.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.input_cedula.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_cedula)

        self.input_telefono = QLineEdit(self.layoutWidget_8)
        self.input_telefono.setObjectName(u"input_telefono")
        self.input_telefono.setMinimumSize(QSize(0, 30))
        self.input_telefono.setMaximumSize(QSize(16777215, 16777215))
        self.input_telefono.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.input_telefono.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_telefono)

        self.input_correo = QLineEdit(self.layoutWidget_8)
        self.input_correo.setObjectName(u"input_correo")
        self.input_correo.setMinimumSize(QSize(0, 30))
        self.input_correo.setMaximumSize(QSize(16777215, 16777215))
        self.input_correo.setStyleSheet(u"QLineEdit {\n"
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
"}")
        self.input_correo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.input_correo)

        self.crear_bt_usuario = QPushButton(self.frame_ingreso)
        self.crear_bt_usuario.setObjectName(u"crear_bt_usuario")
        self.crear_bt_usuario.setGeometry(QRect(330, 20, 75, 23))
        self.crear_bt_usuario.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QPushButton:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"   \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 255, 0, 255); /* Verde claro cuando se presiona */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/user-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.crear_bt_usuario.setIcon(icon1)
        self.crear_bt_usuario.setCheckable(True)
        self.guardar_bt_usuario = QPushButton(self.frame_ingreso)
        self.guardar_bt_usuario.setObjectName(u"guardar_bt_usuario")
        self.guardar_bt_usuario.setGeometry(QRect(330, 50, 75, 23))
        self.guardar_bt_usuario.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QPushButton:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"   \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 255, 0, 255); /* Verde claro cuando se presiona */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardar_bt_usuario.setIcon(icon2)
        self.error_label_contrasena = QLabel(self.frame_ingreso)
        self.error_label_contrasena.setObjectName(u"error_label_contrasena")
        self.error_label_contrasena.setGeometry(QRect(280, 80, 151, 111))
        self.error_label_contrasena.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.error_label_correo = QLabel(self.frame_ingreso)
        self.error_label_correo.setObjectName(u"error_label_correo")
        self.error_label_correo.setGeometry(QRect(280, 260, 151, 21))
        self.error_label_correo.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.eliminar_bt_usuario = QPushButton(self.frame_ingreso)
        self.eliminar_bt_usuario.setObjectName(u"eliminar_bt_usuario")
        self.eliminar_bt_usuario.setGeometry(QRect(330, 80, 75, 23))
        self.eliminar_bt_usuario.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QPushButton:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"   \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 255, 0, 255); /* Verde claro cuando se presiona */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.eliminar_bt_usuario.setIcon(icon2)
        self.layoutWidget_7 = QWidget(self.main_menu)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(330, 10, 133, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_indicador_mreservas_3 = QLabel(self.layoutWidget_7)
        self.lb_indicador_mreservas_3.setObjectName(u"lb_indicador_mreservas_3")
        self.lb_indicador_mreservas_3.setStyleSheet(u"QLabel {\n"
"    color: rgba(0, 128, 0, 255);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.lb_indicador_mreservas_3.setPixmap(QPixmap(u":/newPrefix/users.svg"))

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_3)

        self.lb_indicador_mreservas_2 = QLabel(self.layoutWidget_7)
        self.lb_indicador_mreservas_2.setObjectName(u"lb_indicador_mreservas_2")
        self.lb_indicador_mreservas_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_2)

        self.input_filtro_usuarios = QLineEdit(self.main_menu)
        self.input_filtro_usuarios.setObjectName(u"input_filtro_usuarios")
        self.input_filtro_usuarios.setGeometry(QRect(130, 50, 241, 20))
        self.input_filtro_usuarios.setStyleSheet(u"QLineEdit {\n"
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
        self.editar_bt_usuario = QPushButton(self.main_menu)
        self.editar_bt_usuario.setObjectName(u"editar_bt_usuario")
        self.editar_bt_usuario.setGeometry(QRect(380, 50, 75, 23))
        self.editar_bt_usuario.setStyleSheet(u"QPushButton {\n"
"    border-radius: 10px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QPushButton:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"   \n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(0, 255, 0, 255); /* Verde claro cuando se presiona */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editar_bt_usuario.setIcon(icon3)
        self.editar_bt_usuario.setCheckable(True)
        self.error_campo_vacio = QLabel(self.main_menu)
        self.error_campo_vacio.setObjectName(u"error_campo_vacio")
        self.error_campo_vacio.setGeometry(QRect(30, 380, 401, 41))
        self.error_campo_vacio.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.icon_texto_widget_2 = QWidget(self.frame)
        self.icon_texto_widget_2.setObjectName(u"icon_texto_widget_2")
        self.icon_texto_widget_2.setGeometry(QRect(20, 20, 111, 431))
        self.icon_texto_widget_2.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"")
        self.layoutWidget_5 = QWidget(self.icon_texto_widget_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 290, 111, 112))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(28, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.bt_logout_mm = QPushButton(self.layoutWidget_5)
        self.bt_logout_mm.setObjectName(u"bt_logout_mm")
        self.bt_logout_mm.setStyleSheet(u"QPushButton{\n"
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
"")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_logout_mm.setIcon(icon4)
        self.bt_logout_mm.setCheckable(True)
        self.bt_logout_mm.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.bt_logout_mm)

        self.layoutWidget = QWidget(self.icon_texto_widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 20, 31, 81))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(10, 10))
        self.label_3.setMaximumSize(QSize(100, 100))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(255, 255, 255); /* Fondo blanco */\n"
"    background-image: url(path/to/your/image.png); /* Imagen de fondo */\n"
"    background-position: center; /* Centrar la imagen */\n"
"    background-repeat: no-repeat; /* Evitar que la imagen se repita */\n"
"    background-size: cover; /* Escalar la imagen para cubrir la QLabel */\n"
"    \n"
"    border-radius: 50px; /* Redondear las esquinas (50px es para un c\u00edrculo si el tama\u00f1o es cuadrado) */\n"
"    border: none; /* Sin borde */\n"
"    margin: 0px; /* Sin margen */\n"
"    padding: 0px; /* Sin padding */\n"
"    \n"
"    min-width: 10px;  /* Establecer tama\u00f1o m\u00ednimo */\n"
"    min-height: 10px;\n"
"    max-width: 100px;  /* Establecer tama\u00f1o m\u00e1ximo */\n"
"    max-height: 100px;\n"
"}\n"
"")
        self.label_3.setPixmap(QPixmap(u"../../../Downloads/Captura de pantalla 2024-09-21 151950.jpg"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.verticalSpacer_4 = QSpacerItem(28, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.layoutWidget_2 = QWidget(self.icon_texto_widget_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 110, 113, 171))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_home_mm = QPushButton(self.layoutWidget_2)
        self.bt_home_mm.setObjectName(u"bt_home_mm")
        self.bt_home_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_home_mm.setIcon(icon5)
        self.bt_home_mm.setCheckable(True)
        self.bt_home_mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_home_mm)

        self.bt_reservas__mm = QPushButton(self.layoutWidget_2)
        self.bt_reservas__mm.setObjectName(u"bt_reservas__mm")
        self.bt_reservas__mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_reservas__mm.setIcon(icon6)
        self.bt_reservas__mm.setCheckable(True)
        self.bt_reservas__mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_reservas__mm)

        self.bt_misreservas_mm = QPushButton(self.layoutWidget_2)
        self.bt_misreservas_mm.setObjectName(u"bt_misreservas_mm")
        self.bt_misreservas_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_misreservas_mm.setIcon(icon7)
        self.bt_misreservas_mm.setCheckable(True)
        self.bt_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_misreservas_mm)

        self.bt_configuraciones_mm = QPushButton(self.layoutWidget_2)
        self.bt_configuraciones_mm.setObjectName(u"bt_configuraciones_mm")
        self.bt_configuraciones_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_configuraciones_mm.setIcon(icon8)
        self.bt_configuraciones_mm.setCheckable(True)
        self.bt_configuraciones_mm.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.bt_configuraciones_mm)

        self.widget = QWidget(self.layoutWidget_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.bt_usuarios_mm = QPushButton(self.widget)
        self.bt_usuarios_mm.setObjectName(u"bt_usuarios_mm")
        self.bt_usuarios_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_usuarios_mm.setIcon(icon9)
        self.bt_usuarios_mm.setCheckable(True)
        self.bt_usuarios_mm.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.bt_usuarios_mm)

        self.bt_espacios_mm = QPushButton(self.widget)
        self.bt_espacios_mm.setObjectName(u"bt_espacios_mm")
        self.bt_espacios_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"QPushButton {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    \n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border-radius: 18"
                        "px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_espacios_mm.setIcon(icon10)
        self.bt_espacios_mm.setCheckable(True)
        self.bt_espacios_mm.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.bt_espacios_mm)


        self.verticalLayout_4.addWidget(self.widget)

        self.icon_solamente_widget = QWidget(self.frame)
        self.icon_solamente_widget.setObjectName(u"icon_solamente_widget")
        self.icon_solamente_widget.setGeometry(QRect(10, 20, 51, 431))
        self.icon_solamente_widget.setStyleSheet(u"")
        self.layoutWidget_3 = QWidget(self.icon_solamente_widget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 290, 34, 112))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(28, 88, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.bt_icono_logout_mm = QPushButton(self.layoutWidget_3)
        self.bt_icono_logout_mm.setObjectName(u"bt_icono_logout_mm")
        self.bt_icono_logout_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_logout_mm.setIcon(icon4)
        self.bt_icono_logout_mm.setCheckable(True)
        self.bt_icono_logout_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_logout_mm)

        self.layoutWidget_4 = QWidget(self.icon_solamente_widget)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 111, 34, 171))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_icono_home_mm = QPushButton(self.layoutWidget_4)
        self.bt_icono_home_mm.setObjectName(u"bt_icono_home_mm")
        self.bt_icono_home_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_home_mm.setIcon(icon5)
        self.bt_icono_home_mm.setCheckable(True)
        self.bt_icono_home_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_home_mm)

        self.bt_icono_reservas_mm = QPushButton(self.layoutWidget_4)
        self.bt_icono_reservas_mm.setObjectName(u"bt_icono_reservas_mm")
        self.bt_icono_reservas_mm.setMaximumSize(QSize(16777, 16777215))
        self.bt_icono_reservas_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_reservas_mm.setIcon(icon6)
        self.bt_icono_reservas_mm.setCheckable(True)
        self.bt_icono_reservas_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_reservas_mm)

        self.bt_icono_misreservas_mm = QPushButton(self.layoutWidget_4)
        self.bt_icono_misreservas_mm.setObjectName(u"bt_icono_misreservas_mm")
        self.bt_icono_misreservas_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_misreservas_mm.setIcon(icon7)
        self.bt_icono_misreservas_mm.setCheckable(True)
        self.bt_icono_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_misreservas_mm)

        self.bt_icono_configuraciones_mm = QPushButton(self.layoutWidget_4)
        self.bt_icono_configuraciones_mm.setObjectName(u"bt_icono_configuraciones_mm")
        self.bt_icono_configuraciones_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_configuraciones_mm.setIcon(icon8)
        self.bt_icono_configuraciones_mm.setCheckable(True)
        self.bt_icono_configuraciones_mm.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.bt_icono_configuraciones_mm)

        self.widget_2 = QWidget(self.layoutWidget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bt_icono_usuarios_mm = QPushButton(self.widget_2)
        self.bt_icono_usuarios_mm.setObjectName(u"bt_icono_usuarios_mm")
        self.bt_icono_usuarios_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_usuarios_mm.setIcon(icon9)
        self.bt_icono_usuarios_mm.setCheckable(True)
        self.bt_icono_usuarios_mm.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.bt_icono_usuarios_mm)

        self.bt_icono_espacios_mm = QPushButton(self.widget_2)
        self.bt_icono_espacios_mm.setObjectName(u"bt_icono_espacios_mm")
        self.bt_icono_espacios_mm.setStyleSheet(u"QPushButton{\n"
"	border-top-left-radius: 0 px;\n"
"	border-bottom-left-radius: 30px;\n"
"	border-top-right-radius: 30px;\n"
"	border-bottom-right-radius: 0px;\n"
"	text-align: left;\n"
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
"                              "
                        "        stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
        self.bt_icono_espacios_mm.setIcon(icon10)
        self.bt_icono_espacios_mm.setCheckable(True)
        self.bt_icono_espacios_mm.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.bt_icono_espacios_mm)


        self.verticalLayout.addWidget(self.widget_2)

        self.layoutWidget_6 = QWidget(self.icon_solamente_widget)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 20, 31, 81))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(10, 10))
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background-color: rgb(255, 255, 255); /* Fondo blanco */\n"
"    background-image: url(path/to/your/image.png); /* Imagen de fondo */\n"
"    background-position: center; /* Centrar la imagen */\n"
"    background-repeat: no-repeat; /* Evitar que la imagen se repita */\n"
"    background-size: cover; /* Escalar la imagen para cubrir la QLabel */\n"
"    \n"
"    border-radius: 50px; /* Redondear las esquinas (50px es para un c\u00edrculo si el tama\u00f1o es cuadrado) */\n"
"    border: none; /* Sin borde */\n"
"    margin: 0px; /* Sin margen */\n"
"    padding: 0px; /* Sin padding */\n"
"    \n"
"    min-width: 10px;  /* Establecer tama\u00f1o m\u00ednimo */\n"
"    min-height: 10px;\n"
"    max-width: 100px;  /* Establecer tama\u00f1o m\u00e1ximo */\n"
"    max-height: 100px;\n"
"}\n"
"")
        self.label_4.setPixmap(QPixmap(u"../../../Downloads/Captura de pantalla 2024-09-21 151950.jpg"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_5 = QSpacerItem(28, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bt_cerrarlistado_mm.toggled.connect(self.icon_solamente_widget.setHidden)
        self.bt_cerrarlistado_mm.toggled.connect(self.icon_texto_widget_2.setVisible)
        self.bt_icono_configuraciones_mm.toggled.connect(self.widget_2.setVisible)
        self.bt_configuraciones_mm.toggled.connect(self.widget.setVisible)
        self.editar_bt_usuario.toggled.connect(self.crear_bt_usuario.setDisabled)
        self.crear_bt_usuario.toggled.connect(self.editar_bt_usuario.setDisabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_cerrarlistado_mm.setText("")
        self.input_nombre.setText("")
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.input_usuario.setText("")
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.input_contrasena.setText("")
        self.input_contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.input_rol.setItemText(0, QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.input_rol.setItemText(1, QCoreApplication.translate("MainWindow", u"Profesor", None))
        self.input_rol.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrativo", None))

        self.input_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00e9dula", None))
        self.input_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.input_correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.crear_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.guardar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.error_label_contrasena.setText("")
        self.error_label_correo.setText("")
        self.eliminar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.lb_indicador_mreservas_3.setText("")
        self.lb_indicador_mreservas_2.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.input_filtro_usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar Usuario", None))
        self.editar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.error_campo_vacio.setText("")
        self.bt_logout_mm.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.label_3.setText("")
        self.bt_home_mm.setText(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.bt_reservas__mm.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.bt_misreservas_mm.setText(QCoreApplication.translate("MainWindow", u"Mis reservas", None))
        self.bt_configuraciones_mm.setText(QCoreApplication.translate("MainWindow", u"Configuraciones", None))
        self.bt_usuarios_mm.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.bt_espacios_mm.setText(QCoreApplication.translate("MainWindow", u"Espacios", None))
        self.bt_icono_logout_mm.setText("")
        self.bt_icono_home_mm.setText("")
        self.bt_icono_reservas_mm.setText("")
        self.bt_icono_misreservas_mm.setText("")
        self.bt_icono_configuraciones_mm.setText("")
        self.bt_icono_usuarios_mm.setText("")
        self.bt_icono_espacios_mm.setText("")
        self.label_4.setText("")
    # retranslateUi

