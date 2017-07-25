from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    '''为了更加直观地理解信号与槽，我们进一步修改代码，通过创建按钮响应按钮事件来展示信号与槽机制。'''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Signal and Slot")
        #添加布局
        layout = QHBoxLayout()

        #创建按钮
        for i in range(5):
            button = QPushButton(str(i))
            #将按钮按压信号与自定义函数相关联
            button.pressed.connect(lambda x=i: self._my_func(x))
            #将按钮添加到布局中
            layout.addWidget(button)

        #创建部件
        widget = QWidget()
        #将布局添加到部件
        widget.setLayout(layout)
        #将部件添加到主窗口上
        self.setCentralWidget(widget)

    #自定义信号处理函数
    def _my_func(self, n):
        print('click button %s' %n)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()