from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #设置窗口标题
        self.setWindowTitle('dialog')

        #设置标签
        label = QLabel('Welcome to Shiyanlou!')
        #设置标签在中央
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # 添加按钮动作，并加载图标图像
        button_action = QAction('New dialog', self)
        button_action.triggered.connect(self.onButtonClick)

        # 添加菜单栏
        mb = self.menuBar()
        # 禁用原生的菜单栏
        mb.setNativeMenuBar(False)
        # 添加“文件”菜单
        file_menu = mb.addMenu('&File')
        # 为文件菜单添加动作
        file_menu.addAction(button_action)

    def onButtonClick(self, s):
        # 创建对话框
        dlg = CustomDialog()
        print("nm")
        # 运行对话框，这一步非常重要！
        dlg.exec_()

class CustomDialog(QDialog):
    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.setWindowTitle("NEW DIALOG")
        #添加按钮选项
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonBox = QDialogButtonBox(QBtn)
        buttonBox.accepted().connect(self.accept)
        buttonBox.rejected().connect(self.reject)

        layout = QVBoxLayout()
        layout.addWidget(buttonBox)
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
