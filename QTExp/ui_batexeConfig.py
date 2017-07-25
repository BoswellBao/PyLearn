# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batexe.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BatExeConfig(object):
    def setupUi(self, BatExeConfig):
        BatExeConfig.setObjectName("BatExeConfig")
        BatExeConfig.resize(382, 217)
        self.okButn = QtWidgets.QPushButton(BatExeConfig)
        self.okButn.setEnabled(False)
        self.okButn.setGeometry(QtCore.QRect(80, 150, 75, 23))
        self.okButn.setObjectName("okButn")
        self.widget = QtWidgets.QWidget(BatExeConfig)
        self.widget.setGeometry(QtCore.QRect(33, 11, 71, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.widget1 = QtWidgets.QWidget(BatExeConfig)
        self.widget1.setGeometry(QtCore.QRect(130, 0, 191, 141))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pro_comboBox = QtWidgets.QComboBox(self.widget1)
        self.pro_comboBox.setEnabled(True)
        self.pro_comboBox.setObjectName("pro_comboBox")
        self.verticalLayout_2.addWidget(self.pro_comboBox)
        self.plan_comboBox = QtWidgets.QComboBox(self.widget1)
        self.plan_comboBox.setObjectName("plan_comboBox")
        self.verticalLayout_2.addWidget(self.plan_comboBox)
        self.version_comboBox = QtWidgets.QComboBox(self.widget1)
        self.version_comboBox.setObjectName("version_comboBox")
        self.verticalLayout_2.addWidget(self.version_comboBox)

        self.retranslateUi(BatExeConfig)
        QtCore.QMetaObject.connectSlotsByName(BatExeConfig)

    def retranslateUi(self, BatExeConfig):
        _translate = QtCore.QCoreApplication.translate
        BatExeConfig.setWindowTitle(_translate("BatExeConfig", "BatExeConfig"))
        self.okButn.setText(_translate("BatExeConfig", "OK"))
        self.label.setText(_translate("BatExeConfig", "project"))
        self.label_2.setText(_translate("BatExeConfig", "testPlan"))
        self.label_3.setText(_translate("BatExeConfig", "testVersion"))

