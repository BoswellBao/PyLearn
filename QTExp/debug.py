from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from QTExp.firstui import Ui_Dialog
import sys


class TestDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(TestDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QApplication(sys.argv)
dialog = TestDialog()
dialog.show()
app.exec_()


