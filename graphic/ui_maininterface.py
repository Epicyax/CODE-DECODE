# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maininterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 368)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 491, 311))
        self.plainTextEdit_normal = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_normal.setObjectName(u"plainTextEdit_normal")
        self.plainTextEdit_normal.setGeometry(QRect(10, 10, 231, 291))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(10)
        self.plainTextEdit_normal.setFont(font)
        self.plainTextEdit_coded = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_coded.setObjectName(u"plainTextEdit_coded")
        self.plainTextEdit_coded.setEnabled(True)
        self.plainTextEdit_coded.setGeometry(QRect(250, 10, 231, 291))
        self.plainTextEdit_coded.setFont(font)
        self.plainTextEdit_coded.setReadOnly(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(510, 10, 120, 91))
        self.radioButton_encode = QRadioButton(self.groupBox_2)
        self.radioButton_encode.setObjectName(u"radioButton_encode")
        self.radioButton_encode.setGeometry(QRect(10, 30, 82, 17))
        self.radioButton_encode.setChecked(True)
        self.radioButton_decode = QRadioButton(self.groupBox_2)
        self.radioButton_decode.setObjectName(u"radioButton_decode")
        self.radioButton_decode.setGeometry(QRect(10, 60, 82, 17))
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(510, 110, 120, 101))
        self.pushButton_encode = QPushButton(self.groupBox_3)
        self.pushButton_encode.setObjectName(u"pushButton_encode")
        self.pushButton_encode.setGeometry(QRect(10, 20, 101, 23))
        self.pushButton_decode = QPushButton(self.groupBox_3)
        self.pushButton_decode.setObjectName(u"pushButton_decode")
        self.pushButton_decode.setEnabled(False)
        self.pushButton_decode.setGeometry(QRect(10, 60, 101, 23))
        self.pushButton_decode.setCheckable(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Programa 04", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir archivo", None))
#if QT_CONFIG(tooltip)
        self.actionAbrir.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Abrir el archivo que se va a encriptar o a desencriptar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar archivo", None))
#if QT_CONFIG(tooltip)
        self.actionGuardar.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Guardar el archivo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle("")
#if QT_CONFIG(accessibility)
        self.plainTextEdit_coded.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Modo", None))
        self.radioButton_encode.setText(QCoreApplication.translate("MainWindow", u"Cifrar", None))
        self.radioButton_decode.setText(QCoreApplication.translate("MainWindow", u"Descifrar", None))
        self.groupBox_3.setTitle("")
        self.pushButton_encode.setText(QCoreApplication.translate("MainWindow", u"Cifrar", None))
        self.pushButton_decode.setText(QCoreApplication.translate("MainWindow", u"Descifrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

