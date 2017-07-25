# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batexe.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatExe(object):
    def setupUi(self, BatExe):
        BatExe.setObjectName("BatExe")
        BatExe.resize(1040, 702)
        self.layoutWidget = QtWidgets.QWidget(BatExe)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 0, 671, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.passButn = QtWidgets.QPushButton(self.layoutWidget)
        self.passButn.setObjectName("passButn")
        self.gridLayout.addWidget(self.passButn, 0, 0, 1, 1)
        self.faildButn = QtWidgets.QPushButton(self.layoutWidget)
        self.faildButn.setObjectName("faildButn")
        self.gridLayout.addWidget(self.faildButn, 0, 1, 1, 1)
        self.blockButn = QtWidgets.QPushButton(self.layoutWidget)
        self.blockButn.setObjectName("blockButn")
        self.gridLayout.addWidget(self.blockButn, 0, 2, 1, 1)
        self.casesTree = QtWidgets.QTreeWidget(BatExe)
        self.casesTree.setGeometry(QtCore.QRect(0, 50, 1041, 651))
        self.casesTree.setObjectName("casesTree")
        item_0 = QtWidgets.QTreeWidgetItem(self.casesTree)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setCheckState(0, QtCore.Qt.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.casesTree)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item_0.setFont(0, font)
        item_0.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setCheckState(0, QtCore.Qt.Unchecked)

        self.retranslateUi(BatExe)
        QtCore.QMetaObject.connectSlotsByName(BatExe)

    def retranslateUi(self, BatExe):
        _translate = QtCore.QCoreApplication.translate
        BatExe.setWindowTitle(_translate("BatExe", "Dialog"))
        self.passButn.setText(_translate("BatExe", "PASS"))
        self.faildButn.setText(_translate("BatExe", "FAILD"))
        self.blockButn.setText(_translate("BatExe", "BLOCK"))
        self.casesTree.headerItem().setText(0, _translate("BatExe", "GoSun"))
        __sortingEnabled = self.casesTree.isSortingEnabled()
        self.casesTree.setSortingEnabled(False)
        self.casesTree.topLevelItem(0).setText(0, _translate("BatExe", "模块1"))
        self.casesTree.topLevelItem(0).child(0).setText(0, _translate("BatExe", "用例集1.1"))
        self.casesTree.topLevelItem(0).child(0).child(0).setText(0, _translate("BatExe", "用例1.1.1"))
        self.casesTree.topLevelItem(0).child(0).child(1).setText(0, _translate("BatExe", "用例1.1.2"))
        self.casesTree.topLevelItem(1).setText(0, _translate("BatExe", "模块2"))
        self.casesTree.topLevelItem(1).child(0).setText(0, _translate("BatExe", "用例2.1"))
        self.casesTree.topLevelItem(1).child(1).setText(0, _translate("BatExe", "用例2.2"))
        self.casesTree.setSortingEnabled(__sortingEnabled)

