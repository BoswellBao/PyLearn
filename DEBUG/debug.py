dict = {"wo":{'1': "a", '2': "b"}, "ni":{'1': "c", '2': "d"}}
list = []
for ey in dict.values():
    list.append(ey)
print(list)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())