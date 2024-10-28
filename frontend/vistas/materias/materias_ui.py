# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'materias.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 590)
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
        icon.addFile(u":/newPrefix/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon1.addFile(u":/newPrefix/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon2.addFile(u":/newPrefix/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon3.addFile(u":/newPrefix/clipboard.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon4.addFile(u":/newPrefix/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon5.addFile(u":/newPrefix/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        icon6.addFile(u":/newPrefix/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_logout_mm.setIcon(icon6)
        self.bt_icono_logout_mm.setIconSize(QSize(40, 40))
        self.bt_icono_logout_mm.setCheckable(True)
        self.bt_icono_logout_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_logout_mm)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.bt_espacios_mm = QPushButton(self.widget_2)
        self.bt_espacios_mm.setObjectName(u"bt_espacios_mm")
        font = QFont()
        font.setPointSize(11)
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

        self.gridLayout_4.addWidget(self.bt_espacios_mm, 4, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.bt_logout_mm, 7, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.bt_misreservas_mm, 2, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.bt_usuarios_mm, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 183, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.bt_home_mm = QPushButton(self.widget_2)
        self.bt_home_mm.setObjectName(u"bt_home_mm")
        self.bt_home_mm.setFont(font)
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
"    font: 18pt \"Arial\";\n"
"}")
        self.bt_home_mm.setIcon(icon)
        self.bt_home_mm.setIconSize(QSize(40, 40))
        self.bt_home_mm.setCheckable(True)
        self.bt_home_mm.setAutoExclusive(True)

        self.gridLayout_4.addWidget(self.bt_home_mm, 0, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.bt_reservas__mm, 1, 0, 1, 1)

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

        self.gridLayout_4.addWidget(self.bt_configuraciones_mm, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 1, 1, 1)

        self.Materias = QWidget(self.centralwidget)
        self.Materias.setObjectName(u"Materias")
        self.Materias.setStyleSheet(u"\n"
"background-color: \n"
"rgb(255, 255, 255)")
        self.gridLayout = QGridLayout(self.Materias)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt_cerrarlistado = QPushButton(self.Materias)
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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lb_indicador_mreservas_3 = QLabel(self.Materias)
        self.lb_indicador_mreservas_3.setObjectName(u"lb_indicador_mreservas_3")
        self.lb_indicador_mreservas_3.setStyleSheet(u"QLabel {\n"
"    color: rgba(0, 128, 0, 255);\n"
"    font: 12pt \"Arial\";\n"
"}")
        self.lb_indicador_mreservas_3.setPixmap(QPixmap(u":/newPrefix/clipboard.svg"))

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_3)

        self.lb_indicador_mreservas_2 = QLabel(self.Materias)
        self.lb_indicador_mreservas_2.setObjectName(u"lb_indicador_mreservas_2")
        self.lb_indicador_mreservas_2.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.horizontalLayout.addWidget(self.lb_indicador_mreservas_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 2)

        self.input_filtro_materias = QLineEdit(self.Materias)
        self.input_filtro_materias.setObjectName(u"input_filtro_materias")
        self.input_filtro_materias.setStyleSheet(u"QLineEdit {\n"
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

        self.gridLayout.addWidget(self.input_filtro_materias, 1, 1, 1, 1)

        self.label = QLabel(self.Materias)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.frame_ingreso = QFrame(self.Materias)
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
        self.gridLayout_6 = QGridLayout(self.frame_ingreso)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.input_programa = QLineEdit(self.frame_ingreso)
        self.input_programa.setObjectName(u"input_programa")
        self.input_programa.setMinimumSize(QSize(0, 30))
        self.input_programa.setMaximumSize(QSize(16777215, 16777215))
        self.input_programa.setStyleSheet(u"QLineEdit {\n"
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
        self.input_programa.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.input_programa, 2, 0, 1, 1)

        self.input_idmateria = QLineEdit(self.frame_ingreso)
        self.input_idmateria.setObjectName(u"input_idmateria")
        self.input_idmateria.setMinimumSize(QSize(0, 30))
        self.input_idmateria.setMaximumSize(QSize(16777215, 16777215))
        self.input_idmateria.setStyleSheet(u"QLineEdit {\n"
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
        self.input_idmateria.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.input_idmateria, 0, 0, 1, 1)

        self.input_intensidadhoraria = QLineEdit(self.frame_ingreso)
        self.input_intensidadhoraria.setObjectName(u"input_intensidadhoraria")
        self.input_intensidadhoraria.setMinimumSize(QSize(0, 30))
        self.input_intensidadhoraria.setMaximumSize(QSize(16777215, 16777215))
        self.input_intensidadhoraria.setStyleSheet(u"QLineEdit {\n"
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
        self.input_intensidadhoraria.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.input_intensidadhoraria, 3, 0, 1, 1)

        self.input_nombremateria = QLineEdit(self.frame_ingreso)
        self.input_nombremateria.setObjectName(u"input_nombremateria")
        self.input_nombremateria.setMinimumSize(QSize(0, 30))
        self.input_nombremateria.setMaximumSize(QSize(16777215, 16777215))
        self.input_nombremateria.setStyleSheet(u"QLineEdit {\n"
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
        self.input_nombremateria.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.input_nombremateria, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 2, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.error_label_correo = QLabel(self.frame_ingreso)
        self.error_label_correo.setObjectName(u"error_label_correo")
        self.error_label_correo.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_5.addWidget(self.error_label_correo, 2, 0, 1, 1)

        self.error_label_contrasena = QLabel(self.frame_ingreso)
        self.error_label_contrasena.setObjectName(u"error_label_contrasena")
        self.error_label_contrasena.setStyleSheet(u"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}")

        self.gridLayout_5.addWidget(self.error_label_contrasena, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.crear_bt_materia = QPushButton(self.frame_ingreso)
        self.crear_bt_materia.setObjectName(u"crear_bt_materia")
        self.crear_bt_materia.setFont(font)
        self.crear_bt_materia.setStyleSheet(u"QPushButton {\n"
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
        self.crear_bt_materia.setIcon(icon4)
        self.crear_bt_materia.setIconSize(QSize(40, 40))
        self.crear_bt_materia.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.crear_bt_materia)

        self.editar_bt_materia = QPushButton(self.frame_ingreso)
        self.editar_bt_materia.setObjectName(u"editar_bt_materia")
        self.editar_bt_materia.setFont(font)
        self.editar_bt_materia.setStyleSheet(u"QPushButton {\n"
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
        self.editar_bt_materia.setIcon(icon8)
        self.editar_bt_materia.setIconSize(QSize(40, 40))
        self.editar_bt_materia.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.editar_bt_materia)

        self.guardar_bt_materia = QPushButton(self.frame_ingreso)
        self.guardar_bt_materia.setObjectName(u"guardar_bt_materia")
        self.guardar_bt_materia.setFont(font)
        self.guardar_bt_materia.setStyleSheet(u"QPushButton {\n"
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
        self.guardar_bt_materia.setIcon(icon9)
        self.guardar_bt_materia.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.guardar_bt_materia)

        self.eliminar_bt_materia = QPushButton(self.frame_ingreso)
        self.eliminar_bt_materia.setObjectName(u"eliminar_bt_materia")
        self.eliminar_bt_materia.setFont(font)
        self.eliminar_bt_materia.setStyleSheet(u"QPushButton {\n"
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
        self.eliminar_bt_materia.setIcon(icon10)
        self.eliminar_bt_materia.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.eliminar_bt_materia)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_ingreso, 2, 0, 1, 3)


        self.gridLayout_2.addWidget(self.Materias, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
        self.bt_espacios_mm.setText(QCoreApplication.translate("MainWindow", u"Espacios", None))
        self.bt_logout_mm.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesi\u00f3n", None))
        self.bt_misreservas_mm.setText(QCoreApplication.translate("MainWindow", u"Mis reservas", None))
        self.bt_usuarios_mm.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.bt_home_mm.setText(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.bt_reservas__mm.setText(QCoreApplication.translate("MainWindow", u"Reservas", None))
        self.bt_configuraciones_mm.setText(QCoreApplication.translate("MainWindow", u"Materias", None))
        self.bt_cerrarlistado.setText("")
        self.lb_indicador_mreservas_3.setText("")
        self.lb_indicador_mreservas_2.setText(QCoreApplication.translate("MainWindow", u"MATERIAS", None))
        self.input_filtro_materias.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Escriba el ID o nombre de la materia", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Buscar Materia", None))
        self.input_programa.setText("")
        self.input_programa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Programa", None))
        self.input_idmateria.setText("")
        self.input_idmateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Materia", None))
        self.input_intensidadhoraria.setText("")
        self.input_intensidadhoraria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Intensidad horaria", None))
        self.input_nombremateria.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de la materia", None))
        self.error_label_correo.setText("")
        self.error_label_contrasena.setText("")
        self.crear_bt_materia.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.editar_bt_materia.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.guardar_bt_materia.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.eliminar_bt_materia.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

