# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(826, 600)
        self.botao_procura_imagem = QPushButton(Dialog)
        self.botao_procura_imagem.setObjectName(u"botao_procura_imagem")
        self.botao_procura_imagem.setGeometry(QRect(40, 60, 141, 29))
        self.botao_reconhecer = QPushButton(Dialog)
        self.botao_reconhecer.setObjectName(u"botao_reconhecer")
        self.botao_reconhecer.setGeometry(QRect(240, 60, 88, 29))
        self.botao_ruido_aleatorio = QPushButton(Dialog)
        self.botao_ruido_aleatorio.setObjectName(u"botao_ruido_aleatorio")
        self.botao_ruido_aleatorio.setGeometry(QRect(367, 60, 121, 29))
        self.botao_pixelar = QPushButton(Dialog)
        self.botao_pixelar.setObjectName(u"botao_pixelar")
        self.botao_pixelar.setGeometry(QRect(367, 20, 121, 29))
        self.slider_horizontal = QSlider(Dialog)
        self.slider_horizontal.setObjectName(u"slider_horizontal")
        self.slider_horizontal.setGeometry(QRect(520, 70, 160, 16))
        self.slider_horizontal.setMaximum(100)
        self.slider_horizontal.setValue(1)
        self.slider_horizontal.setOrientation(Qt.Orientation.Horizontal)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 119, 631, 381))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.botao_procura_imagem.setText(QCoreApplication.translate("Dialog", u"Procurar imagem", None))
        self.botao_reconhecer.setText(QCoreApplication.translate("Dialog", u"Reconhcer", None))
        self.botao_ruido_aleatorio.setText(QCoreApplication.translate("Dialog", u"Ruido aleat\u00f3rio", None))
        self.botao_pixelar.setText(QCoreApplication.translate("Dialog", u"Pixelar", None))
    # retranslateUi

