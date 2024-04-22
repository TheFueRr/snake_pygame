# Form implementation generated from reading ui file 'snake/main_gui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 527)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.start_pushButton.setObjectName("start_pushButton")
        self.verticalLayout.addWidget(self.start_pushButton)
        self.settings_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.settings_pushButton.setObjectName("settings_pushButton")
        self.verticalLayout.addWidget(self.settings_pushButton)
        self.score_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.score_pushButton.setObjectName("score_pushButton")
        self.verticalLayout.addWidget(self.score_pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.page_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.back_pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.back_pushButton.setObjectName("back_pushButton")
        self.verticalLayout_2.addWidget(self.back_pushButton)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.page_3)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_fast = QtWidgets.QRadioButton(parent=self.page_3)
        self.radioButton_fast.setChecked(False)
        self.radioButton_fast.setObjectName("radioButton_fast")
        self.horizontalLayout.addWidget(self.radioButton_fast)
        self.radioButton_medium = QtWidgets.QRadioButton(parent=self.page_3)
        self.radioButton_medium.setObjectName("radioButton_medium")
        self.horizontalLayout.addWidget(self.radioButton_medium)
        self.radioButton_slow = QtWidgets.QRadioButton(parent=self.page_3)
        self.radioButton_slow.setChecked(True)
        self.radioButton_slow.setObjectName("radioButton_slow")
        self.horizontalLayout.addWidget(self.radioButton_slow)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(parent=self.page_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.Amount_of_fruits = QtWidgets.QSpinBox(parent=self.page_3)
        self.Amount_of_fruits.setMinimum(1)
        self.Amount_of_fruits.setMaximum(5)
        self.Amount_of_fruits.setObjectName("Amount_of_fruits")
        self.verticalLayout_3.addWidget(self.Amount_of_fruits)
        self.label_3 = QtWidgets.QLabel(parent=self.page_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Height_size = QtWidgets.QSpinBox(parent=self.page_3)
        self.Height_size.setMinimum(15)
        self.Height_size.setMaximum(40)
        self.Height_size.setObjectName("Height_size")
        self.horizontalLayout_2.addWidget(self.Height_size)
        self.label_4 = QtWidgets.QLabel(parent=self.page_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Width_size = QtWidgets.QSpinBox(parent=self.page_3)
        self.Width_size.setMinimum(15)
        self.Width_size.setMaximum(40)
        self.Width_size.setObjectName("Width_size")
        self.horizontalLayout_3.addWidget(self.Width_size)
        self.label_5 = QtWidgets.QLabel(parent=self.page_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.back_pushButton_1 = QtWidgets.QPushButton(parent=self.page_3)
        self.back_pushButton_1.setObjectName("back_pushButton_1")
        self.verticalLayout_3.addWidget(self.back_pushButton_1)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushButton.setText(_translate("MainWindow", "Start Game"))
        self.settings_pushButton.setText(_translate("MainWindow", "Settings"))
        self.score_pushButton.setText(_translate("MainWindow", "Scoreboard"))
        self.back_pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", "Speed"))
        self.radioButton_fast.setText(_translate("MainWindow", "Fast"))
        self.radioButton_medium.setText(_translate("MainWindow", "Medium"))
        self.radioButton_slow.setText(_translate("MainWindow", "Slow"))
        self.label_2.setText(_translate("MainWindow", "Amount of fruits"))
        self.label_3.setText(_translate("MainWindow", "Fields size"))
        self.label_4.setText(_translate("MainWindow", "Height"))
        self.label_5.setText(_translate("MainWindow", "Width"))
        self.back_pushButton_1.setText(_translate("MainWindow", "back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())