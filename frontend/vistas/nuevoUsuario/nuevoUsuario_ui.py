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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_10 = QVBoxLayout(self.widget_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.bt_icono_home_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_home_mm_2.setObjectName(u"bt_icono_home_mm_2")
        self.bt_icono_home_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/newPrefix/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_home_mm_2.setIcon(icon)
        self.bt_icono_home_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_home_mm_2.setCheckable(True)
        self.bt_icono_home_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_home_mm_2)

        self.bt_icono_reservas_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_reservas_mm_2.setObjectName(u"bt_icono_reservas_mm_2")
        self.bt_icono_reservas_mm_2.setMaximumSize(QSize(16777, 16777215))
        self.bt_icono_reservas_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/newPrefix/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_reservas_mm_2.setIcon(icon1)
        self.bt_icono_reservas_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_reservas_mm_2.setCheckable(True)
        self.bt_icono_reservas_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_reservas_mm_2)

        self.bt_icono_misreservas_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_misreservas_mm_2.setObjectName(u"bt_icono_misreservas_mm_2")
        self.bt_icono_misreservas_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon2.addFile(u":/newPrefix/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_misreservas_mm_2.setIcon(icon2)
        self.bt_icono_misreservas_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_misreservas_mm_2.setCheckable(True)
        self.bt_icono_misreservas_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_misreservas_mm_2)

        self.bt_icono_configuraciones_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_configuraciones_mm_2.setObjectName(u"bt_icono_configuraciones_mm_2")
        self.bt_icono_configuraciones_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon3.addFile(u":/newPrefix/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_configuraciones_mm_2.setIcon(icon3)
        self.bt_icono_configuraciones_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_configuraciones_mm_2.setCheckable(True)
        self.bt_icono_configuraciones_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_configuraciones_mm_2)

        self.bt_icono_espacios_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_espacios_mm_2.setObjectName(u"bt_icono_espacios_mm_2")
        self.bt_icono_espacios_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon4.addFile(u":/newPrefix/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_espacios_mm_2.setIcon(icon4)
        self.bt_icono_espacios_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_espacios_mm_2.setCheckable(True)
        self.bt_icono_espacios_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_espacios_mm_2)

        self.bt_icono_usuarios_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_usuarios_mm_2.setObjectName(u"bt_icono_usuarios_mm_2")
        self.bt_icono_usuarios_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon5.addFile(u":/newPrefix/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_usuarios_mm_2.setIcon(icon5)
        self.bt_icono_usuarios_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_usuarios_mm_2.setCheckable(True)
        self.bt_icono_usuarios_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_usuarios_mm_2)

        self.verticalSpacer = QSpacerItem(20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.bt_icono_logout_mm_2 = QPushButton(self.widget_3)
        self.bt_icono_logout_mm_2.setObjectName(u"bt_icono_logout_mm_2")
        self.bt_icono_logout_mm_2.setStyleSheet(u"QPushButton{\n"
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
        icon6.addFile(u":/newPrefix/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_logout_mm_2.setIcon(icon6)
        self.bt_icono_logout_mm_2.setIconSize(QSize(40, 40))
        self.bt_icono_logout_mm_2.setCheckable(True)
        self.bt_icono_logout_mm_2.setAutoExclusive(True)

        self.verticalLayout_10.addWidget(self.bt_icono_logout_mm_2)


        self.gridLayout_3.addWidget(self.widget_3, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.bt_home_mm_2 = QPushButton(self.widget_4)
        self.bt_home_mm_2.setObjectName(u"bt_home_mm_2")
        font = QFont()
        font.setPointSize(11)
        self.bt_home_mm_2.setFont(font)
        self.bt_home_mm_2.setStyleSheet(u"QPushButton {\n"
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
        icon7 = QIcon()
        icon7.addFile(u"../../imagenes/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_home_mm_2.setIcon(icon7)
        self.bt_home_mm_2.setIconSize(QSize(40, 40))
        self.bt_home_mm_2.setCheckable(True)
        self.bt_home_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_home_mm_2)

        self.bt_reservas__mm_2 = QPushButton(self.widget_4)
        self.bt_reservas__mm_2.setObjectName(u"bt_reservas__mm_2")
        self.bt_reservas__mm_2.setFont(font)
        self.bt_reservas__mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_reservas__mm_2.setIcon(icon1)
        self.bt_reservas__mm_2.setIconSize(QSize(40, 40))
        self.bt_reservas__mm_2.setCheckable(True)
        self.bt_reservas__mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_reservas__mm_2)

        self.bt_misreservas_mm_2 = QPushButton(self.widget_4)
        self.bt_misreservas_mm_2.setObjectName(u"bt_misreservas_mm_2")
        self.bt_misreservas_mm_2.setFont(font)
        self.bt_misreservas_mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_misreservas_mm_2.setIcon(icon2)
        self.bt_misreservas_mm_2.setIconSize(QSize(40, 40))
        self.bt_misreservas_mm_2.setCheckable(True)
        self.bt_misreservas_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_misreservas_mm_2)

        self.bt_configuraciones_mm_2 = QPushButton(self.widget_4)
        self.bt_configuraciones_mm_2.setObjectName(u"bt_configuraciones_mm_2")
        self.bt_configuraciones_mm_2.setFont(font)
        self.bt_configuraciones_mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_configuraciones_mm_2.setIcon(icon3)
        self.bt_configuraciones_mm_2.setIconSize(QSize(40, 40))
        self.bt_configuraciones_mm_2.setCheckable(True)
        self.bt_configuraciones_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_configuraciones_mm_2)

        self.bt_espacios_mm_2 = QPushButton(self.widget_4)
        self.bt_espacios_mm_2.setObjectName(u"bt_espacios_mm_2")
        self.bt_espacios_mm_2.setFont(font)
        self.bt_espacios_mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_espacios_mm_2.setIcon(icon4)
        self.bt_espacios_mm_2.setIconSize(QSize(40, 40))
        self.bt_espacios_mm_2.setCheckable(True)
        self.bt_espacios_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_espacios_mm_2)

        self.bt_usuarios_mm_2 = QPushButton(self.widget_4)
        self.bt_usuarios_mm_2.setObjectName(u"bt_usuarios_mm_2")
        self.bt_usuarios_mm_2.setFont(font)
        self.bt_usuarios_mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_usuarios_mm_2.setIcon(icon5)
        self.bt_usuarios_mm_2.setIconSize(QSize(40, 40))
        self.bt_usuarios_mm_2.setCheckable(True)
        self.bt_usuarios_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_usuarios_mm_2)

        self.verticalSpacer_6 = QSpacerItem(20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)

        self.bt_logout_mm_2 = QPushButton(self.widget_4)
        self.bt_logout_mm_2.setObjectName(u"bt_logout_mm_2")
        self.bt_logout_mm_2.setFont(font)
        self.bt_logout_mm_2.setStyleSheet(u"QPushButton{\n"
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
        self.bt_logout_mm_2.setIcon(icon6)
        self.bt_logout_mm_2.setIconSize(QSize(40, 40))
        self.bt_logout_mm_2.setCheckable(True)
        self.bt_logout_mm_2.setAutoExclusive(True)

        self.verticalLayout_11.addWidget(self.bt_logout_mm_2)


        self.gridLayout_3.addWidget(self.widget_4, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"\n"
"background-color: \n"
"rgb(255, 255, 255)")
        self.gridLayout_2 = QGridLayout(self.main_menu)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.main_menu)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)

        self.input_filtro_usuarios = QLineEdit(self.main_menu)
        self.input_filtro_usuarios.setObjectName(u"input_filtro_usuarios")
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

        self.gridLayout_2.addWidget(self.input_filtro_usuarios, 1, 2, 1, 1)

        self.frame_ingreso = QFrame(self.main_menu)
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
        self.gridLayout = QGridLayout(self.frame_ingreso)
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_telefono = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_telefono, 7, 0, 1, 1)

        self.input_correo = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_correo, 8, 0, 1, 1)

        self.widget = QWidget(self.frame_ingreso)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.crear_bt_usuario = QPushButton(self.frame_ingreso)
        self.crear_bt_usuario.setObjectName(u"crear_bt_usuario")
        self.crear_bt_usuario.setFont(font)
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
        self.crear_bt_usuario.setIcon(icon4)
        self.crear_bt_usuario.setIconSize(QSize(40, 40))
        self.crear_bt_usuario.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.crear_bt_usuario)

        self.editar_bt_usuario = QPushButton(self.frame_ingreso)
        self.editar_bt_usuario.setObjectName(u"editar_bt_usuario")
        self.editar_bt_usuario.setFont(font)
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
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/smartphone.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.editar_bt_usuario.setIcon(icon8)
        self.editar_bt_usuario.setIconSize(QSize(40, 40))
        self.editar_bt_usuario.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.editar_bt_usuario)

        self.guardar_bt_usuario = QPushButton(self.frame_ingreso)
        self.guardar_bt_usuario.setObjectName(u"guardar_bt_usuario")
        self.guardar_bt_usuario.setFont(font)
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
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.guardar_bt_usuario.setIcon(icon9)
        self.guardar_bt_usuario.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.guardar_bt_usuario)

        self.eliminar_bt_usuario = QPushButton(self.frame_ingreso)
        self.eliminar_bt_usuario.setObjectName(u"eliminar_bt_usuario")
        self.eliminar_bt_usuario.setFont(font)
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
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/trash-2.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eliminar_bt_usuario.setIcon(icon10)
        self.eliminar_bt_usuario.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.eliminar_bt_usuario)


        self.gridLayout.addLayout(self.horizontalLayout_2, 9, 0, 1, 1)

        self.input_contrasena = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_contrasena, 4, 0, 1, 1)

        self.input_usuario = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_usuario, 3, 0, 1, 1)

        self.input_nombre = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_nombre, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.input_rol = QComboBox(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_rol, 5, 0, 1, 1)

        self.input_cedula = QLineEdit(self.frame_ingreso)
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

        self.gridLayout.addWidget(self.input_cedula, 6, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 10, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_ingreso, 2, 0, 1, 3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_indicador_mreservas_3 = QLabel(self.main_menu)
        self.lb_indicador_mreservas_3.setObjectName(u"lb_indicador_mreservas_3")
        self.lb_indicador_mreservas_3.setStyleSheet(u"QLabel {\n"
"    color: rgba(0, 128, 0, 255);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.lb_indicador_mreservas_3.setPixmap(QPixmap(u":/newPrefix/users.svg"))

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_3)

        self.lb_indicador_mreservas_2 = QLabel(self.main_menu)
        self.lb_indicador_mreservas_2.setObjectName(u"lb_indicador_mreservas_2")
        self.lb_indicador_mreservas_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.bt_cerrarlistado_mm = QPushButton(self.main_menu)
        self.bt_cerrarlistado_mm.setObjectName(u"bt_cerrarlistado_mm")
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
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cerrarlistado_mm.setIcon(icon11)
        self.bt_cerrarlistado_mm.setIconSize(QSize(40, 40))
        self.bt_cerrarlistado_mm.setCheckable(True)

        self.gridLayout_2.addWidget(self.bt_cerrarlistado_mm, 0, 0, 1, 2)


        self.gridLayout_3.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.bt_cerrarlistado_mm.toggled.connect(self.widget_3.setHidden)
        self.bt_cerrarlistado_mm.toggled.connect(self.widget_4.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_icono_home_mm_2.setText("")
        self.bt_icono_reservas_mm_2.setText("")
        self.bt_icono_misreservas_mm_2.setText("")
        self.bt_icono_configuraciones_mm_2.setText("")
        self.bt_icono_espacios_mm_2.setText("")
        self.bt_icono_usuarios_mm_2.setText("")
        self.bt_icono_logout_mm_2.setText("")
        self.bt_home_mm_2.setText(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.bt_reservas__mm_2.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.bt_misreservas_mm_2.setText(QCoreApplication.translate("MainWindow", u"Mis reservas", None))
        self.bt_configuraciones_mm_2.setText(QCoreApplication.translate("MainWindow", u"Configuraciones", None))
        self.bt_espacios_mm_2.setText(QCoreApplication.translate("MainWindow", u"Espacios", None))
        self.bt_usuarios_mm_2.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.bt_logout_mm_2.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Buscar Usuario", None))
        self.input_filtro_usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el nombre el usuario", None))
        self.input_telefono.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.input_correo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Correo", None))
        self.crear_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.editar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.guardar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.eliminar_bt_usuario.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.input_contrasena.setText("")
        self.input_contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.input_usuario.setText("")
        self.input_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.input_nombre.setText("")
        self.input_nombre.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.input_rol.setItemText(0, QCoreApplication.translate("MainWindow", u"Estudiante", None))
        self.input_rol.setItemText(1, QCoreApplication.translate("MainWindow", u"Profesor", None))
        self.input_rol.setItemText(2, QCoreApplication.translate("MainWindow", u"Administrativo", None))

        self.input_cedula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"C\u00e9dula", None))
        self.lb_indicador_mreservas_3.setText("")
        self.lb_indicador_mreservas_2.setText(QCoreApplication.translate("MainWindow", u"USUARIOS", None))
        self.bt_cerrarlistado_mm.setText("")
    # retranslateUi

