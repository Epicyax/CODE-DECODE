# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyneededdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(325, 86)
        self.lineEdit_key = QLineEdit(Dialog)
        self.lineEdit_key.setObjectName(u"lineEdit_key")
        self.lineEdit_key.setGeometry(QRect(20, 20, 291, 21))
        self.lineEdit_key.setReadOnly(False)
        self.pushButton_ok = QPushButton(Dialog)
        self.pushButton_ok.setObjectName(u"pushButton_ok")
        self.pushButton_ok.setGeometry(QRect(240, 50, 75, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Ingrese la clave", None))
        self.lineEdit_key.setText("")
        self.lineEdit_key.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese la llave necesaria para desencriptar", None))
        self.pushButton_ok.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
    # retranslateUi

