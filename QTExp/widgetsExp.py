from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("widgets")
        #定义布局
        layout = QVBoxLayout()

        # 展示的部件列表
        widgets = [QCheckBox,
                QComboBox,
                QDateEdit,
                QDateTimeEdit,
                QDial,
                QDoubleSpinBox,
                QFontComboBox,
                QLCDNumber,
                QLineEdit,
                QProgressBar,
                QPushButton,
                QRadioButton,
                QSlider,
                QSpinBox,
                QTimeEdit]
        # 将部件添加大列表中
        for item in widgets:
            layout.addWidget(item())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()