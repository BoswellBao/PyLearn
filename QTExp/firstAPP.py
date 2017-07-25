from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #设置窗口标题
        self.setWindowTitle('My First App')

        #设置标签
        label = QLabel('Welcome to Shiyanlou!')
        #设置标签在中央
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

#Qt 的执行机制: Qt 的程序通过创建 QApplication 类实例来调用 app.exec_ 方法进入事件循环。
# 此时程序一直在循环监听各种事件并把它们放入消息队列中，在适当的时候从队列中取出处理

#创建应用实例，通过 sys.argv 传入命令行参数
app = QApplication(sys.argv)
#创建窗口实例
window = MainWindow()
#显示窗口
window.show()
#执行应用，进入事件循环
app.exec_()
