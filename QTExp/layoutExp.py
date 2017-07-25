from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #设置窗口标题
        self.setWindowTitle('Layout')

        colors = ['red', 'green', 'blue', 'yellow']
        #垂直布局    要水平布局，把QVBoxLayout改成QHBoxLayout
        layout = QVBoxLayout()
        for color in colors:
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        #网格布局
        grid_layout = QGridLayout()
        for i, color in enumerate(colors):
            for j in range(10):
                grid_layout.addWidget(Color(color), i, j)

        widget = QWidget()
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
