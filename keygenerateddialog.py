from PySide2.QtWidgets import QDialog
from graphic.ui_keygenerateddialog import Ui_Dialog
import pyperclip as clipboard

class KeyGeneratedDialog(QDialog):
    def __init__(self, generatedKey):
        super(KeyGeneratedDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_copy.clicked.connect(self.copy)
        self.ui.lineEdit_key.insert(generatedKey)


    def copy(self):
        key = self.ui.lineEdit_key.displayText()
        clipboard.copy(key)