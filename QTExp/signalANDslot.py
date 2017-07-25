from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    '''这里将 QMainWindow 的信号 windowTitleChanged 与 _my_func 槽函数相绑定，当窗口标题被更改的信号发出的时候便会触发函数 _my_func 进行处理。

其中在自定义函数 _my_func 中允许设置任意多个参数。'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("aaaa")
        self.windowTitleChanged.connect(self._my_func())

    #自定义信号处理函数
    def _my_func(self, s='my_func', a=100):
        dic = {'s': s, 'a': a}
        print(dic)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()