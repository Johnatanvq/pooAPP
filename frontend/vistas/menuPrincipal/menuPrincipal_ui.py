# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuPrincipal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_Menu_Principal(object):
    def setupUi(self, Menu_Principal):
        if not Menu_Principal.objectName():
            Menu_Principal.setObjectName(u"Menu_Principal")
        Menu_Principal.resize(627, 469)
        self.centralwidget = QWidget(Menu_Principal)
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
        self.main_menu.setStyleSheet(u"background-color: \n"
"rgb(255, 255, 255)\n"
"\n"
"")
        self.cabecera_widget = QWidget(self.main_menu)
        self.cabecera_widget.setObjectName(u"cabecera_widget")
        self.cabecera_widget.setGeometry(QRect(10, 50, 41, 41))
        self.label = QLabel(self.main_menu)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 391, 381))
        self.label.setMaximumSize(QSize(16777192, 16777215))
        self.label.setPixmap(QPixmap(u"../../imagenes/image.png"))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-5)
        self.lb_fecha_mm = QLabel(self.main_menu)
        self.lb_fecha_mm.setObjectName(u"lb_fecha_mm")
        self.lb_fecha_mm.setGeometry(QRect(320, 10, 91, 20))
        self.lb_fecha_mm.setStyleSheet(u"QLabel {\n"
"    border-radius: 18px;\n"
"     background-color: qlineargradient(spread:reflect, x1:0, y1:0.562273, x2:0.949, y2:0.545455, \n"
"                                      stop:0 rgb(255,255,255), /* Cian oscuro */\n"
"                                      stop:1 rgb(255,255,255)); /* Cian claro */\n"
"}   \n"
"\n"
"QLabel:hover {\n"
"	  background-color: qlineargradient(spread:reflect, x1:0, y1:0.532273, x2:1, y2:0.5, \n"
"                                      stop:0.362832 rgba(0,128,0,255), /* Verde oscuro */\n"
"                                      stop:0.369469 rgba(0,128,0,255), \n"
"                                      stop:1 rgba(0,255,0,255)); /* Verde claro */\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    font: 12pt \"Arial\";\n"
"}\n"
"")
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
        icon.addFile(u"../../imagenes/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_cerrarlistado_mm.setIcon(icon)
        self.bt_cerrarlistado_mm.setCheckable(True)
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
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_logout_mm.setIcon(icon1)
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

        self.layoutWidget1 = QWidget(self.icon_texto_widget_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 110, 113, 171))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.bt_home_mm = QPushButton(self.layoutWidget1)
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
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_home_mm.setIcon(icon2)
        self.bt_home_mm.setCheckable(True)
        self.bt_home_mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_home_mm)

        self.bt_reservas_mm = QPushButton(self.layoutWidget1)
        self.bt_reservas_mm.setObjectName(u"bt_reservas_mm")
        self.bt_reservas_mm.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_reservas_mm.setIcon(icon3)
        self.bt_reservas_mm.setCheckable(True)
        self.bt_reservas_mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_reservas_mm)

        self.bt_misreservas_mm = QPushButton(self.layoutWidget1)
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
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_misreservas_mm.setIcon(icon4)
        self.bt_misreservas_mm.setCheckable(True)
        self.bt_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.bt_misreservas_mm)

        self.bt_configuraciones_mm = QPushButton(self.layoutWidget1)
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
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_configuraciones_mm.setIcon(icon5)
        self.bt_configuraciones_mm.setCheckable(True)
        self.bt_configuraciones_mm.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.bt_configuraciones_mm)

        self.widget = QWidget(self.layoutWidget1)
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
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_usuarios_mm.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_espacios_mm.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u"../../imagenes/log-out.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_logout_mm.setIcon(icon8)
        self.bt_icono_logout_mm.setCheckable(True)
        self.bt_icono_logout_mm.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.bt_icono_logout_mm)

        self.layoutWidget2 = QWidget(self.icon_solamente_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 111, 34, 171))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bt_icono_home_mm = QPushButton(self.layoutWidget2)
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
        icon9 = QIcon()
        icon9.addFile(u"../../imagenes/home.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_home_mm.setIcon(icon9)
        self.bt_icono_home_mm.setCheckable(True)
        self.bt_icono_home_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_home_mm)

        self.bt_icono_reservas_mm = QPushButton(self.layoutWidget2)
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
        icon10 = QIcon()
        icon10.addFile(u"../../imagenes/bookmark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_reservas_mm.setIcon(icon10)
        self.bt_icono_reservas_mm.setCheckable(True)
        self.bt_icono_reservas_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_reservas_mm)

        self.bt_icono_misreservas_mm = QPushButton(self.layoutWidget2)
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
        icon11 = QIcon()
        icon11.addFile(u"../../imagenes/book-open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_misreservas_mm.setIcon(icon11)
        self.bt_icono_misreservas_mm.setCheckable(True)
        self.bt_icono_misreservas_mm.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bt_icono_misreservas_mm)

        self.bt_icono_configuraciones_mm = QPushButton(self.layoutWidget2)
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
        icon12 = QIcon()
        icon12.addFile(u"../../imagenes/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_configuraciones_mm.setIcon(icon12)
        self.bt_icono_configuraciones_mm.setCheckable(True)
        self.bt_icono_configuraciones_mm.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.bt_icono_configuraciones_mm)

        self.widget_2 = QWidget(self.layoutWidget2)
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
        icon13 = QIcon()
        icon13.addFile(u"../../imagenes/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_usuarios_mm.setIcon(icon13)
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
        icon14 = QIcon()
        icon14.addFile(u"../../imagenes/key.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_icono_espacios_mm.setIcon(icon14)
        self.bt_icono_espacios_mm.setCheckable(True)
        self.bt_icono_espacios_mm.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.bt_icono_espacios_mm)


        self.verticalLayout.addWidget(self.widget_2)

        self.layoutWidget3 = QWidget(self.icon_solamente_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 31, 81))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget3)
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

        Menu_Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu_Principal)
        self.bt_cerrarlistado_mm.toggled.connect(self.icon_texto_widget_2.setVisible)
        self.bt_configuraciones_mm.toggled.connect(self.widget.setVisible)
        self.bt_cerrarlistado_mm.toggled.connect(self.icon_solamente_widget.setHidden)
        self.bt_icono_configuraciones_mm.toggled.connect(self.widget_2.setVisible)

        QMetaObject.connectSlotsByName(Menu_Principal)
    # setupUi

    def retranslateUi(self, Menu_Principal):
        Menu_Principal.setWindowTitle(QCoreApplication.translate("Menu_Principal", u"MainWindow", None))
        self.label.setText("")
        self.lb_fecha_mm.setText(QCoreApplication.translate("Menu_Principal", u"Fecha hoy", None))
        self.bt_cerrarlistado_mm.setText("")
        self.bt_logout_mm.setText(QCoreApplication.translate("Menu_Principal", u"Cerrar Sesi\u00f3n", None))
        self.label_3.setText("")
        self.bt_home_mm.setText(QCoreApplication.translate("Menu_Principal", u"Principal", None))
        self.bt_reservas_mm.setText(QCoreApplication.translate("Menu_Principal", u"Reservas", None))
        self.bt_misreservas_mm.setText(QCoreApplication.translate("Menu_Principal", u"Mis reservas", None))
        self.bt_configuraciones_mm.setText(QCoreApplication.translate("Menu_Principal", u"Configuraciones", None))
        self.bt_usuarios_mm.setText(QCoreApplication.translate("Menu_Principal", u"Usuarios", None))
        self.bt_espacios_mm.setText(QCoreApplication.translate("Menu_Principal", u"Espacios", None))
        self.bt_icono_logout_mm.setText("")
        self.bt_icono_home_mm.setText("")
        self.bt_icono_reservas_mm.setText("")
        self.bt_icono_misreservas_mm.setText("")
        self.bt_icono_configuraciones_mm.setText("")
        self.bt_icono_usuarios_mm.setText("")
        self.bt_icono_espacios_mm.setText("")
        self.label_4.setText("")
    # retranslateUi

