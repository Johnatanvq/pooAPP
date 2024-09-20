# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intro.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_intro(object):
    def setupUi(self, intro):
        if not intro.objectName():
            intro.setObjectName(u"intro")
        intro.resize(646, 623)
        self.centralwidget = QWidget(intro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.intro_gif = QLabel(self.centralwidget)
        self.intro_gif.setObjectName(u"intro_gif")
        self.intro_gif.setGeometry(QRect(0, 0, 641, 591))
        self.intro_gif.setMaximumSize(QSize(16777215, 16777215))
        self.intro_gif.setPixmap(QPixmap(u"../../imagenes/intro.gif"))
        self.intro_gif.setScaledContents(False)
        self.intro_gif.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 190, 221, 41))
        self.label.setStyleSheet(u"QLabel{\n"
"	background: #000000;\n"
"	color: #FFFFFF;\n"
"	font-size: 20pt;\n"
"	font-family:\"Courier New\", monospace;\n"
"}")
        self.intro_bt = QPushButton(self.centralwidget)
        self.intro_bt.setObjectName(u"intro_bt")
        self.intro_bt.setGeometry(QRect(180, 280, 271, 51))
        self.intro_bt.setStyleSheet(u"QPushButton{\n"
"	background: #04B338;\n"
"	font-size: 15pt;\n"
"	color: white;\n"
"	font-weight: bold;\n"
"	font-family:\"Courier New\", monospace;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 510, 211, 16))
        self.label_2.setStyleSheet(u"QLabel{\n"
"	background: #000000;\n"
"	color: #FFFFFF;\n"
"	font-size: 8pt;\n"
"	font-style: italic;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 0, 191, 31))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: #000000;\n"
"	color: #FFFFFF;\n"
"	font-size: 10pt;\n"
"	font-style: italic;\n"
"}")
        intro.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(intro)
        self.statusbar.setObjectName(u"statusbar")
        intro.setStatusBar(self.statusbar)

        self.retranslateUi(intro)

        QMetaObject.connectSlotsByName(intro)
    # setupUi

    def retranslateUi(self, intro):
        intro.setWindowTitle(QCoreApplication.translate("intro", u"MainWindow", None))
        self.intro_gif.setText("")
        self.label.setText(QCoreApplication.translate("intro", u"\u00a1BIENVENIDO!", None))
        self.intro_bt.setText(QCoreApplication.translate("intro", u"Presiona para entrar", None))
        self.label_2.setText(QCoreApplication.translate("intro", u"desarrollado por daniela&johnatan", None))
        self.label_3.setText(QCoreApplication.translate("intro", u"dirigido por juan camilo", None))
    # retranslateUi

