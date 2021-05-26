from PySide2.QtWidgets import QDialog
from graphic.ui_keyneededdialog import Ui_Dialog

class KeyNeededDialog(QDialog):
    def __init__(self):
        super(KeyNeededDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_ok.clicked.connect(self.getKey)


    def getKey(self):
        key = self.ui.lineEdit_key.displayText()
        self.close()
        return key
        