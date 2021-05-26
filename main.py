from PySide2.QtWidgets import QApplication
from maininterface import MainInterface
import sys

app = QApplication()
window = MainInterface()
window.show()
sys.exit(app.exec_())