# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevaReserva.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1067, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bt_icono_home_mm = QPushButton(self.widget)
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
        icon = QIcon()
        icon.addFile(u"../../imagenes/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_home_mm.setIcon(icon)
        self.bt_icono_home_mm.setIconSize(QSize(40, 40))
        self.bt_icono_home_mm.setCheckable(True)
        self.bt_icono_home_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_home_mm)

        self.bt_icono_reservas_mm = QPushButton(self.widget)
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
        icon1 = QIcon()
        icon1.addFile(u"../../imagenes/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_reservas_mm.setIcon(icon1)
        self.bt_icono_reservas_mm.setIconSize(QSize(40, 40))
        self.bt_icono_reservas_mm.setCheckable(True)
        self.bt_icono_reservas_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_reservas_mm)

        self.bt_icono_misreservas_mm = QPushButton(self.widget)
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
        icon2 = QIcon()
        icon2.addFile(u"../../imagenes/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_misreservas_mm.setIcon(icon2)
        self.bt_icono_misreservas_mm.setIconSize(QSize(40, 40))
        self.bt_icono_misreservas_mm.setCheckable(True)
        self.bt_icono_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_misreservas_mm)

        self.bt_icono_configuraciones_mm = QPushButton(self.widget)
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
        icon3 = QIcon()
        icon3.addFile(u"../../imagenes/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_configuraciones_mm.setIcon(icon3)
        self.bt_icono_configuraciones_mm.setIconSize(QSize(40, 40))
        self.bt_icono_configuraciones_mm.setCheckable(True)
        self.bt_icono_configuraciones_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_configuraciones_mm)

        self.bt_icono_espacios_mm = QPushButton(self.widget)
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
        icon4 = QIcon()
        icon4.addFile(u"../../imagenes/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_espacios_mm.setIcon(icon4)
        self.bt_icono_espacios_mm.setIconSize(QSize(40, 40))
        self.bt_icono_espacios_mm.setCheckable(True)
        self.bt_icono_espacios_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_espacios_mm)

        self.bt_icono_usuarios_mm = QPushButton(self.widget)
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
        icon5 = QIcon()
        icon5.addFile(u"../../imagenes/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_usuarios_mm.setIcon(icon5)
        self.bt_icono_usuarios_mm.setIconSize(QSize(40, 40))
        self.bt_icono_usuarios_mm.setCheckable(True)
        self.bt_icono_usuarios_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_usuarios_mm)

        self.verticalSpacer = QSpacerItem(20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bt_icono_logout_mm = QPushButton(self.widget)
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
        icon6 = QIcon()
        icon6.addFile(u"../../imagenes/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_logout_mm.setIcon(icon6)
        self.bt_icono_logout_mm.setIconSize(QSize(40, 40))
        self.bt_icono_logout_mm.setCheckable(True)
        self.bt_icono_logout_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_logout_mm)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_home_mm = QPushButton(self.widget_2)
        self.bt_home_mm.setObjectName(u"bt_home_mm")
        font = QFont()
        font.setPointSize(11)
        self.bt_home_mm.setFont(font)
        self.bt_home_mm.setStyleSheet(u"QPushButton {\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 30px;\n"
"    border-top-right-radius: 30px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                       stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                       stop:0.369469 rgba(0,128,0,255), \n"
"                                       stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"    padding-left: 0px; /* Espacio a la izquierda para simular alineaci\u00f3n */\n"
"    border: none; /* Sin borde, opcional */\n"
"    text-align: left; /* Aunque esto no tendr\u00e1 efecto en QPushButton, lo incluimos para claridad */\n"
"    border-radius: 18px; /* Si quieres bordes redondeados uniformes */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-top-left-radius: 0px;\n"
"    border-bottom-left-radius: 30px;\n"
"    border-top-right-radius: 30px;\n"
"    border-bottom-right-radi"
                        "us: 0px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(225, 225, 224);\n"
"    font: 24pt \"Arial\";\n"
"}\n"
"")
        self.bt_home_mm.setIcon(icon)
        self.bt_home_mm.setIconSize(QSize(40, 40))
        self.bt_home_mm.setCheckable(True)
        self.bt_home_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_home_mm)

        self.bt_reservas__mm = QPushButton(self.widget_2)
        self.bt_reservas__mm.setObjectName(u"bt_reservas__mm")
        self.bt_reservas__mm.setFont(font)
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
"    font: 18pt \"Arial\";\n"
"}")
        self.bt_reservas__mm.setIcon(icon1)
        self.bt_reservas__mm.setIconSize(QSize(40, 40))
        self.bt_reservas__mm.setCheckable(True)
        self.bt_reservas__mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_reservas__mm)

        self.bt_misreservas_mm = QPushButton(self.widget_2)
        self.bt_misreservas_mm.setObjectName(u"bt_misreservas_mm")
        self.bt_misreservas_mm.setFont(font)
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
        self.bt_misreservas_mm.setIcon(icon2)
        self.bt_misreservas_mm.setIconSize(QSize(40, 40))
        self.bt_misreservas_mm.setCheckable(True)
        self.bt_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_misreservas_mm)

        self.bt_configuraciones_mm = QPushButton(self.widget_2)
        self.bt_configuraciones_mm.setObjectName(u"bt_configuraciones_mm")
        self.bt_configuraciones_mm.setFont(font)
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
        self.bt_configuraciones_mm.setIcon(icon3)
        self.bt_configuraciones_mm.setIconSize(QSize(40, 40))
        self.bt_configuraciones_mm.setCheckable(True)
        self.bt_configuraciones_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_configuraciones_mm)

        self.bt_espacios_mm = QPushButton(self.widget_2)
        self.bt_espacios_mm.setObjectName(u"bt_espacios_mm")
        self.bt_espacios_mm.setFont(font)
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
        self.bt_espacios_mm.setIcon(icon4)
        self.bt_espacios_mm.setIconSize(QSize(40, 40))
        self.bt_espacios_mm.setCheckable(True)
        self.bt_espacios_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_espacios_mm)

        self.bt_usuarios_mm = QPushButton(self.widget_2)
        self.bt_usuarios_mm.setObjectName(u"bt_usuarios_mm")
        self.bt_usuarios_mm.setFont(font)
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
        self.bt_usuarios_mm.setIcon(icon5)
        self.bt_usuarios_mm.setIconSize(QSize(40, 40))
        self.bt_usuarios_mm.setCheckable(True)
        self.bt_usuarios_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_usuarios_mm)

        self.verticalSpacer_2 = QSpacerItem(20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.bt_logout_mm = QPushButton(self.widget_2)
        self.bt_logout_mm.setObjectName(u"bt_logout_mm")
        self.bt_logout_mm.setFont(font)
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
        self.bt_logout_mm.setIcon(icon6)
        self.bt_logout_mm.setIconSize(QSize(40, 40))
        self.bt_logout_mm.setCheckable(True)
        self.bt_logout_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_logout_mm)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"\n"
"background-color: \n"
"rgb(255, 255, 255)")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.lb_indicador_mreservas_3 = QLabel(self.widget_3)
        self.lb_indicador_mreservas_3.setObjectName(u"lb_indicador_mreservas_3")
        self.lb_indicador_mreservas_3.setStyleSheet(u"QLabel {\n"
"    color: rgba(0, 128, 0, 255);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.lb_indicador_mreservas_3.setPixmap(QPixmap(u":/newPrefix/calendar.svg"))

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_3)

        self.lb_indicador_mreservas_2 = QLabel(self.widget_3)
        self.lb_indicador_mreservas_2.setObjectName(u"lb_indicador_mreservas_2")
        self.lb_indicador_mreservas_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.bt_cerrarlistado = QPushButton(self.widget_3)
        self.bt_cerrarlistado.setObjectName(u"bt_cerrarlistado")
        self.bt_cerrarlistado.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cerrarlistado.setIcon(icon7)
        self.bt_cerrarlistado.setIconSize(QSize(40, 40))
        self.bt_cerrarlistado.setCheckable(True)

        self.gridLayout.addWidget(self.bt_cerrarlistado, 0, 0, 1, 1)

        self.frame_ingreso = QFrame(self.widget_3)
        self.frame_ingreso.setObjectName(u"frame_ingreso")
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
        self.gridLayout_3 = QGridLayout(self.frame_ingreso)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.frame_ingreso)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 5, 7, 1, 1)

        self.select_hora_inicio = QComboBox(self.frame_ingreso)
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.addItem("")
        self.select_hora_inicio.setObjectName(u"select_hora_inicio")
        self.select_hora_inicio.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.select_hora_inicio, 2, 9, 1, 1)

        self.select_mes_inicio = QComboBox(self.frame_ingreso)
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.addItem("")
        self.select_mes_inicio.setObjectName(u"select_mes_inicio")
        self.select_mes_inicio.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"")

        self.gridLayout_3.addWidget(self.select_mes_inicio, 2, 2, 1, 3)

        self.select_dia_inicio = QComboBox(self.frame_ingreso)
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.addItem("")
        self.select_dia_inicio.setObjectName(u"select_dia_inicio")
        self.select_dia_inicio.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"")
        self.select_dia_inicio.setEditable(True)

        self.gridLayout_3.addWidget(self.select_dia_inicio, 2, 5, 1, 1)

        self.comboBox = QComboBox(self.frame_ingreso)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.comboBox, 4, 9, 1, 4)

        self.label_5 = QLabel(self.frame_ingreso)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 2)

        self.label_6 = QLabel(self.frame_ingreso)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_6, 2, 8, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(24, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 12, 1, 2)

        self.select_hora_final = QComboBox(self.frame_ingreso)
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.addItem("")
        self.select_hora_final.setObjectName(u"select_hora_final")
        self.select_hora_final.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"")

        self.gridLayout_3.addWidget(self.select_hora_final, 5, 9, 1, 2)

        self.horizontalSpacer_5 = QSpacerItem(14, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 14, 1, 1)

        self.label_4 = QLabel(self.frame_ingreso)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 5, 8, 1, 1)

        self.input_ano_final = QLineEdit(self.frame_ingreso)
        self.input_ano_final.setObjectName(u"input_ano_final")
        self.input_ano_final.setLayoutDirection(Qt.RightToLeft)
        self.input_ano_final.setStyleSheet(u"QLineEdit {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }")
        self.input_ano_final.setReadOnly(False)

        self.gridLayout_3.addWidget(self.input_ano_final, 5, 6, 1, 1)

        self.select_minutos_inicio = QComboBox(self.frame_ingreso)
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.addItem("")
        self.select_minutos_inicio.setObjectName(u"select_minutos_inicio")
        self.select_minutos_inicio.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"")

        self.gridLayout_3.addWidget(self.select_minutos_inicio, 2, 10, 1, 2)

        self.no_duracion_checkbox = QCheckBox(self.frame_ingreso)
        self.no_duracion_checkbox.setObjectName(u"no_duracion_checkbox")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.no_duracion_checkbox.setFont(font1)
        self.no_duracion_checkbox.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.no_duracion_checkbox, 3, 1, 1, 2)

        self.si_duracion_checkbox = QCheckBox(self.frame_ingreso)
        self.si_duracion_checkbox.setObjectName(u"si_duracion_checkbox")
        self.si_duracion_checkbox.setFont(font1)
        self.si_duracion_checkbox.setCheckable(True)

        self.gridLayout_3.addWidget(self.si_duracion_checkbox, 3, 3, 1, 3)

        self.input_descripcion_evento = QLineEdit(self.frame_ingreso)
        self.input_descripcion_evento.setObjectName(u"input_descripcion_evento")
        self.input_descripcion_evento.setStyleSheet(u"QLineEdit {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }")
        self.input_descripcion_evento.setReadOnly(False)

        self.gridLayout_3.addWidget(self.input_descripcion_evento, 1, 4, 1, 10)

        self.input_ano_inicio = QLineEdit(self.frame_ingreso)
        self.input_ano_inicio.setObjectName(u"input_ano_inicio")
        self.input_ano_inicio.setStyleSheet(u"QLineEdit {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }")
        self.input_ano_inicio.setReadOnly(False)

        self.gridLayout_3.addWidget(self.input_ano_inicio, 2, 6, 1, 1)

        self.error_label_capacidad = QLabel(self.frame_ingreso)
        self.error_label_capacidad.setObjectName(u"error_label_capacidad")
        self.error_label_capacidad.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.error_label_capacidad, 0, 0, 1, 1)

        self.select_minuto_final = QComboBox(self.frame_ingreso)
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.addItem("")
        self.select_minuto_final.setObjectName(u"select_minuto_final")
        self.select_minuto_final.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"")

        self.gridLayout_3.addWidget(self.select_minuto_final, 5, 11, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(88, 231, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 7, 1, 1, 3)

        self.select_dia_final = QComboBox(self.frame_ingreso)
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.addItem("")
        self.select_dia_final.setObjectName(u"select_dia_final")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.select_dia_final.setFont(font2)
        self.select_dia_final.setLayoutDirection(Qt.RightToLeft)
        self.select_dia_final.setAutoFillBackground(False)
        self.select_dia_final.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }\n"
"        ")

        self.gridLayout_3.addWidget(self.select_dia_final, 5, 5, 1, 1)

        self.label_7 = QLabel(self.frame_ingreso)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 4)

        self.select_mes_final = QComboBox(self.frame_ingreso)
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.addItem("")
        self.select_mes_final.setObjectName(u"select_mes_final")
        self.select_mes_final.setLayoutDirection(Qt.RightToLeft)
        self.select_mes_final.setStyleSheet(u"QComboBox{\n"
"	background: white;\n"
"}\n"
"QComboBox {\n"
"            background-color: rgb(245, 245, 245);  /* Fondo gris claro */\n"
"            border-radius: 10px;\n"
"            font: 11pt \"Arial\";\n"
"            border: 2px solid rgb(180, 180, 180);  /* Borde gris claro */\n"
"            padding: 5px;\n"
"        }\n"
"        QComboBox:hover {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro al pasar el mouse */\n"
"            border: 2px solid rgb(100, 149, 237);  /* Azul claro en hover */\n"
"        }\n"
"        QComboBox:focus {\n"
"            background-color: rgb(255, 255, 255);  /* Blanco puro cuando tiene foco */\n"
"            border: 2px solid rgb(0, 122, 204);    /* Azul m\u00e1s oscuro cuando est\u00e1 en foco */\n"
"        }\n"
"        QComboBox::drop-down {\n"
"            border: none;\n"
"        }\n"
"        QComboBox::down-arrow {\n"
"            image: url(none); /* Puedes personalizar esto o quitarlo */\n"
"        }\n"
"        QComboBox QAbstrac"
                        "tItemView {\n"
"            background-color: white;\n"
"            border-radius: 10px;\n"
"            border: 1px solid rgb(180, 180, 180);\n"
"            selection-background-color: rgb(100, 149, 237); /* Azul claro para la selecci\u00f3n */\n"
"        }")

        self.gridLayout_3.addWidget(self.select_mes_final, 5, 2, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(12, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 5, 13, 1, 1)

        self.crear_bt_reserva = QPushButton(self.frame_ingreso)
        self.crear_bt_reserva.setObjectName(u"crear_bt_reserva")
        self.crear_bt_reserva.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u"../../imagenes/calendar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.crear_bt_reserva.setIcon(icon8)
        self.crear_bt_reserva.setIconSize(QSize(40, 40))

        self.gridLayout_3.addWidget(self.crear_bt_reserva, 6, 9, 1, 1)


        self.gridLayout.addWidget(self.frame_ingreso, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.widget_3, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_3.raise_()
        self.widget.raise_()
        self.widget_2.raise_()

        self.retranslateUi(MainWindow)
        self.bt_cerrarlistado.toggled.connect(self.widget.setHidden)
        self.bt_cerrarlistado.toggled.connect(self.widget_2.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_icono_home_mm.setText("")
        self.bt_icono_reservas_mm.setText("")
        self.bt_icono_misreservas_mm.setText("")
        self.bt_icono_configuraciones_mm.setText("")
        self.bt_icono_espacios_mm.setText("")
        self.bt_icono_usuarios_mm.setText("")
        self.bt_icono_logout_mm.setText("")
        self.bt_home_mm.setText(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.bt_reservas__mm.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.bt_misreservas_mm.setText(QCoreApplication.translate("MainWindow", u"Mis reservas", None))
        self.bt_configuraciones_mm.setText(QCoreApplication.translate("MainWindow", u"Configuraciones", None))
        self.bt_espacios_mm.setText(QCoreApplication.translate("MainWindow", u"Espacios", None))
        self.bt_usuarios_mm.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.bt_logout_mm.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.lb_indicador_mreservas_3.setText("")
        self.lb_indicador_mreservas_2.setText(QCoreApplication.translate("MainWindow", u"NUEVA RESERVA", None))
        self.bt_cerrarlistado.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fecha Final:", None))
        self.select_hora_inicio.setItemText(0, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_hora_inicio.setItemText(1, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_hora_inicio.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_hora_inicio.setItemText(3, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_hora_inicio.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_hora_inicio.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_hora_inicio.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_hora_inicio.setItemText(7, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_hora_inicio.setItemText(8, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_hora_inicio.setItemText(9, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_hora_inicio.setItemText(10, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_hora_inicio.setItemText(11, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_hora_inicio.setItemText(12, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_hora_inicio.setItemText(13, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_hora_inicio.setItemText(14, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_hora_inicio.setItemText(15, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_hora_inicio.setItemText(16, QCoreApplication.translate("MainWindow", u"22", None))

        self.select_mes_inicio.setItemText(0, QCoreApplication.translate("MainWindow", u"enero", None))
        self.select_mes_inicio.setItemText(1, QCoreApplication.translate("MainWindow", u"febrero", None))
        self.select_mes_inicio.setItemText(2, QCoreApplication.translate("MainWindow", u"marzo", None))
        self.select_mes_inicio.setItemText(3, QCoreApplication.translate("MainWindow", u"abril", None))
        self.select_mes_inicio.setItemText(4, QCoreApplication.translate("MainWindow", u"mayo", None))
        self.select_mes_inicio.setItemText(5, QCoreApplication.translate("MainWindow", u"junio", None))
        self.select_mes_inicio.setItemText(6, QCoreApplication.translate("MainWindow", u"julio", None))
        self.select_mes_inicio.setItemText(7, QCoreApplication.translate("MainWindow", u"agosto", None))
        self.select_mes_inicio.setItemText(8, QCoreApplication.translate("MainWindow", u"septiembre", None))
        self.select_mes_inicio.setItemText(9, QCoreApplication.translate("MainWindow", u"octubre", None))
        self.select_mes_inicio.setItemText(10, QCoreApplication.translate("MainWindow", u"noviembre", None))
        self.select_mes_inicio.setItemText(11, QCoreApplication.translate("MainWindow", u"diciembre", None))

        self.select_dia_inicio.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.select_dia_inicio.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.select_dia_inicio.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.select_dia_inicio.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.select_dia_inicio.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.select_dia_inicio.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_dia_inicio.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_dia_inicio.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_dia_inicio.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_dia_inicio.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_dia_inicio.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_dia_inicio.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_dia_inicio.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_dia_inicio.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_dia_inicio.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_dia_inicio.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_dia_inicio.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_dia_inicio.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_dia_inicio.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_dia_inicio.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_dia_inicio.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_dia_inicio.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.select_dia_inicio.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.select_dia_inicio.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.select_dia_inicio.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.select_dia_inicio.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.select_dia_inicio.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.select_dia_inicio.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.select_dia_inicio.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.select_dia_inicio.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.select_dia_inicio.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sal\u00f3n", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Laboratorio", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Auditorio", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fecha Inicial:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hora final:", None))
        self.select_hora_final.setItemText(0, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_hora_final.setItemText(1, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_hora_final.setItemText(2, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_hora_final.setItemText(3, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_hora_final.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_hora_final.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_hora_final.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_hora_final.setItemText(7, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_hora_final.setItemText(8, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_hora_final.setItemText(9, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_hora_final.setItemText(10, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_hora_final.setItemText(11, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_hora_final.setItemText(12, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_hora_final.setItemText(13, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_hora_final.setItemText(14, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_hora_final.setItemText(15, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_hora_final.setItemText(16, QCoreApplication.translate("MainWindow", u"22", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hora final:", None))
        self.input_ano_final.setText(QCoreApplication.translate("MainWindow", u"2020", None))
        self.select_minutos_inicio.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.select_minutos_inicio.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.select_minutos_inicio.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.select_minutos_inicio.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.select_minutos_inicio.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.select_minutos_inicio.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_minutos_inicio.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_minutos_inicio.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_minutos_inicio.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_minutos_inicio.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_minutos_inicio.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_minutos_inicio.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_minutos_inicio.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_minutos_inicio.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_minutos_inicio.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_minutos_inicio.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_minutos_inicio.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_minutos_inicio.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_minutos_inicio.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_minutos_inicio.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_minutos_inicio.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_minutos_inicio.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.select_minutos_inicio.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.select_minutos_inicio.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.select_minutos_inicio.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.select_minutos_inicio.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.select_minutos_inicio.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.select_minutos_inicio.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.select_minutos_inicio.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.select_minutos_inicio.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.select_minutos_inicio.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))
        self.select_minutos_inicio.setItemText(31, QCoreApplication.translate("MainWindow", u"32", None))
        self.select_minutos_inicio.setItemText(32, QCoreApplication.translate("MainWindow", u"33", None))
        self.select_minutos_inicio.setItemText(33, QCoreApplication.translate("MainWindow", u"34", None))
        self.select_minutos_inicio.setItemText(34, QCoreApplication.translate("MainWindow", u"35", None))
        self.select_minutos_inicio.setItemText(35, QCoreApplication.translate("MainWindow", u"36", None))
        self.select_minutos_inicio.setItemText(36, QCoreApplication.translate("MainWindow", u"37", None))
        self.select_minutos_inicio.setItemText(37, QCoreApplication.translate("MainWindow", u"38", None))
        self.select_minutos_inicio.setItemText(38, QCoreApplication.translate("MainWindow", u"39", None))
        self.select_minutos_inicio.setItemText(39, QCoreApplication.translate("MainWindow", u"40", None))
        self.select_minutos_inicio.setItemText(40, QCoreApplication.translate("MainWindow", u"41", None))
        self.select_minutos_inicio.setItemText(41, QCoreApplication.translate("MainWindow", u"42", None))
        self.select_minutos_inicio.setItemText(42, QCoreApplication.translate("MainWindow", u"43", None))
        self.select_minutos_inicio.setItemText(43, QCoreApplication.translate("MainWindow", u"44", None))
        self.select_minutos_inicio.setItemText(44, QCoreApplication.translate("MainWindow", u"45", None))
        self.select_minutos_inicio.setItemText(45, QCoreApplication.translate("MainWindow", u"46", None))
        self.select_minutos_inicio.setItemText(46, QCoreApplication.translate("MainWindow", u"47", None))
        self.select_minutos_inicio.setItemText(47, QCoreApplication.translate("MainWindow", u"48", None))
        self.select_minutos_inicio.setItemText(48, QCoreApplication.translate("MainWindow", u"49", None))
        self.select_minutos_inicio.setItemText(49, QCoreApplication.translate("MainWindow", u"50", None))
        self.select_minutos_inicio.setItemText(50, QCoreApplication.translate("MainWindow", u"51", None))
        self.select_minutos_inicio.setItemText(51, QCoreApplication.translate("MainWindow", u"52", None))
        self.select_minutos_inicio.setItemText(52, QCoreApplication.translate("MainWindow", u"53", None))
        self.select_minutos_inicio.setItemText(53, QCoreApplication.translate("MainWindow", u"54", None))
        self.select_minutos_inicio.setItemText(54, QCoreApplication.translate("MainWindow", u"55", None))
        self.select_minutos_inicio.setItemText(55, QCoreApplication.translate("MainWindow", u"56", None))
        self.select_minutos_inicio.setItemText(56, QCoreApplication.translate("MainWindow", u"57", None))
        self.select_minutos_inicio.setItemText(57, QCoreApplication.translate("MainWindow", u"58", None))
        self.select_minutos_inicio.setItemText(58, QCoreApplication.translate("MainWindow", u"59", None))

        self.no_duracion_checkbox.setText(QCoreApplication.translate("MainWindow", u"sin duraci\u00f3n", None))
        self.si_duracion_checkbox.setText(QCoreApplication.translate("MainWindow", u"con duraci\u00f3n", None))
        self.input_descripcion_evento.setText("")
        self.input_ano_inicio.setText(QCoreApplication.translate("MainWindow", u"2020", None))
        self.error_label_capacidad.setText("")
        self.select_minuto_final.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.select_minuto_final.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.select_minuto_final.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.select_minuto_final.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.select_minuto_final.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.select_minuto_final.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_minuto_final.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_minuto_final.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_minuto_final.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_minuto_final.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_minuto_final.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_minuto_final.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_minuto_final.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_minuto_final.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_minuto_final.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_minuto_final.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_minuto_final.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_minuto_final.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_minuto_final.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_minuto_final.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_minuto_final.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_minuto_final.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.select_minuto_final.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.select_minuto_final.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.select_minuto_final.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.select_minuto_final.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.select_minuto_final.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.select_minuto_final.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.select_minuto_final.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.select_minuto_final.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.select_minuto_final.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))
        self.select_minuto_final.setItemText(31, QCoreApplication.translate("MainWindow", u"32", None))
        self.select_minuto_final.setItemText(32, QCoreApplication.translate("MainWindow", u"33", None))
        self.select_minuto_final.setItemText(33, QCoreApplication.translate("MainWindow", u"34", None))
        self.select_minuto_final.setItemText(34, QCoreApplication.translate("MainWindow", u"35", None))
        self.select_minuto_final.setItemText(35, QCoreApplication.translate("MainWindow", u"36", None))
        self.select_minuto_final.setItemText(36, QCoreApplication.translate("MainWindow", u"37", None))
        self.select_minuto_final.setItemText(37, QCoreApplication.translate("MainWindow", u"38", None))
        self.select_minuto_final.setItemText(38, QCoreApplication.translate("MainWindow", u"39", None))
        self.select_minuto_final.setItemText(39, QCoreApplication.translate("MainWindow", u"40", None))
        self.select_minuto_final.setItemText(40, QCoreApplication.translate("MainWindow", u"41", None))
        self.select_minuto_final.setItemText(41, QCoreApplication.translate("MainWindow", u"42", None))
        self.select_minuto_final.setItemText(42, QCoreApplication.translate("MainWindow", u"43", None))
        self.select_minuto_final.setItemText(43, QCoreApplication.translate("MainWindow", u"44", None))
        self.select_minuto_final.setItemText(44, QCoreApplication.translate("MainWindow", u"45", None))
        self.select_minuto_final.setItemText(45, QCoreApplication.translate("MainWindow", u"46", None))
        self.select_minuto_final.setItemText(46, QCoreApplication.translate("MainWindow", u"47", None))
        self.select_minuto_final.setItemText(47, QCoreApplication.translate("MainWindow", u"48", None))
        self.select_minuto_final.setItemText(48, QCoreApplication.translate("MainWindow", u"49", None))
        self.select_minuto_final.setItemText(49, QCoreApplication.translate("MainWindow", u"50", None))
        self.select_minuto_final.setItemText(50, QCoreApplication.translate("MainWindow", u"51", None))
        self.select_minuto_final.setItemText(51, QCoreApplication.translate("MainWindow", u"52", None))
        self.select_minuto_final.setItemText(52, QCoreApplication.translate("MainWindow", u"53", None))
        self.select_minuto_final.setItemText(53, QCoreApplication.translate("MainWindow", u"54", None))
        self.select_minuto_final.setItemText(54, QCoreApplication.translate("MainWindow", u"55", None))
        self.select_minuto_final.setItemText(55, QCoreApplication.translate("MainWindow", u"56", None))
        self.select_minuto_final.setItemText(56, QCoreApplication.translate("MainWindow", u"57", None))
        self.select_minuto_final.setItemText(57, QCoreApplication.translate("MainWindow", u"58", None))
        self.select_minuto_final.setItemText(58, QCoreApplication.translate("MainWindow", u"59", None))

        self.select_dia_final.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.select_dia_final.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.select_dia_final.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.select_dia_final.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.select_dia_final.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.select_dia_final.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.select_dia_final.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.select_dia_final.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.select_dia_final.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.select_dia_final.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))
        self.select_dia_final.setItemText(10, QCoreApplication.translate("MainWindow", u"11", None))
        self.select_dia_final.setItemText(11, QCoreApplication.translate("MainWindow", u"12", None))
        self.select_dia_final.setItemText(12, QCoreApplication.translate("MainWindow", u"13", None))
        self.select_dia_final.setItemText(13, QCoreApplication.translate("MainWindow", u"14", None))
        self.select_dia_final.setItemText(14, QCoreApplication.translate("MainWindow", u"15", None))
        self.select_dia_final.setItemText(15, QCoreApplication.translate("MainWindow", u"16", None))
        self.select_dia_final.setItemText(16, QCoreApplication.translate("MainWindow", u"17", None))
        self.select_dia_final.setItemText(17, QCoreApplication.translate("MainWindow", u"18", None))
        self.select_dia_final.setItemText(18, QCoreApplication.translate("MainWindow", u"19", None))
        self.select_dia_final.setItemText(19, QCoreApplication.translate("MainWindow", u"20", None))
        self.select_dia_final.setItemText(20, QCoreApplication.translate("MainWindow", u"21", None))
        self.select_dia_final.setItemText(21, QCoreApplication.translate("MainWindow", u"22", None))
        self.select_dia_final.setItemText(22, QCoreApplication.translate("MainWindow", u"23", None))
        self.select_dia_final.setItemText(23, QCoreApplication.translate("MainWindow", u"24", None))
        self.select_dia_final.setItemText(24, QCoreApplication.translate("MainWindow", u"25", None))
        self.select_dia_final.setItemText(25, QCoreApplication.translate("MainWindow", u"26", None))
        self.select_dia_final.setItemText(26, QCoreApplication.translate("MainWindow", u"27", None))
        self.select_dia_final.setItemText(27, QCoreApplication.translate("MainWindow", u"28", None))
        self.select_dia_final.setItemText(28, QCoreApplication.translate("MainWindow", u"29", None))
        self.select_dia_final.setItemText(29, QCoreApplication.translate("MainWindow", u"30", None))
        self.select_dia_final.setItemText(30, QCoreApplication.translate("MainWindow", u"31", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n del evento:", None))
        self.select_mes_final.setItemText(0, QCoreApplication.translate("MainWindow", u"enero", None))
        self.select_mes_final.setItemText(1, QCoreApplication.translate("MainWindow", u"febrero", None))
        self.select_mes_final.setItemText(2, QCoreApplication.translate("MainWindow", u"marzo", None))
        self.select_mes_final.setItemText(3, QCoreApplication.translate("MainWindow", u"abril", None))
        self.select_mes_final.setItemText(4, QCoreApplication.translate("MainWindow", u"mayo", None))
        self.select_mes_final.setItemText(5, QCoreApplication.translate("MainWindow", u"junio", None))
        self.select_mes_final.setItemText(6, QCoreApplication.translate("MainWindow", u"julio", None))
        self.select_mes_final.setItemText(7, QCoreApplication.translate("MainWindow", u"agosto", None))
        self.select_mes_final.setItemText(8, QCoreApplication.translate("MainWindow", u"septiembre", None))
        self.select_mes_final.setItemText(9, QCoreApplication.translate("MainWindow", u"octubre", None))
        self.select_mes_final.setItemText(10, QCoreApplication.translate("MainWindow", u"noviembre", None))
        self.select_mes_final.setItemText(11, QCoreApplication.translate("MainWindow", u"diciembre", None))

        self.crear_bt_reserva.setText(QCoreApplication.translate("MainWindow", u"CREAR RESERVA", None))
    # retranslateUi

