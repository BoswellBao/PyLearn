from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("TOOL")
        label = QLabel("USE TOOL")
        label.setAlignment(Qt.AlignCenter)
        #添加到主窗口
        self.setCentralWidget(label)

        #创建工具栏
        tb = QToolBar('Tool Bar')
        #设置工具栏大小
        tb.setIconSize(QSize(16, 16))
        #添加工具栏到主窗口
        self.addToolBar(tb)

        #添加按钮动作，并加载图标图像
        button_action = QAction(QIcon("E:\\图片\\bike.png"), 'Menu button', self)
        #设置状态栏提示
        button_action.setStatusTip('This is menu button')
        button_action.setCheckable(True)
        #添加到工具栏
        tb.addAction(button_action)
        #为主窗口设置状态栏
        self.setStatusBar(QStatusBar(self))

        ## 二级菜单
        # 添加新的菜单选项
        button_action2 = QAction('c++', self)
        button_action3 = QAction('python', self)
        # button_action2.setCheckable(True)
        # button_action3.setCheckable(True)


        #添加菜单栏
        mb = self.menuBar()
        #禁用原生的菜单栏
        mb.setNativeMenuBar(False)
        #添加“文件”菜单
        file_menu = mb.addMenu('&File')
        #为文件菜单添加动作
        file_menu.addAction(button_action)

        #位菜单选项添加分隔符
        file_menu.addSeparator()
        #添加二级菜单
        build_system_menu = file_menu.addMenu('&Build System')
        build_system_menu.addAction(button_action2)
        build_system_menu.addSeparator()
        build_system_menu.addAction(button_action3)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()