# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dock_ver3.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.TEM = QtWidgets.QLineEdit(self.centralwidget)
        self.TEM.setGeometry(QtCore.QRect(430, 290, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.TEM.setFont(font)
        self.TEM.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TEM.setStyleSheet("font: 81 36pt \"Open Sans ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(64, 64, 64);\n"
"background:transparent;")
        self.TEM.setMaxLength(30000)
        self.TEM.setFrame(False)
        self.TEM.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TEM.setObjectName("TEM")
        self.PUL = QtWidgets.QLineEdit(self.centralwidget)
        self.PUL.setGeometry(QtCore.QRect(450, 210, 141, 41))
        self.PUL.setFocusPolicy(QtCore.Qt.NoFocus)
        self.PUL.setStyleSheet("font: 81 36pt \"Open Sans ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(64, 64, 64);\n"
"background:transparent;")
        self.PUL.setFrame(False)
        self.PUL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.PUL.setObjectName("PUL")
        self.DIA = QtWidgets.QLineEdit(self.centralwidget)
        self.DIA.setGeometry(QtCore.QRect(390, 130, 201, 41))
        self.DIA.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DIA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.DIA.setStyleSheet("font: 81 36pt \"Open Sans ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(64, 64, 64);\n"
"background:transparent;")
        self.DIA.setFrame(False)
        self.DIA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.DIA.setObjectName("DIA")
        self.SYS = QtWidgets.QLineEdit(self.centralwidget)
        self.SYS.setGeometry(QtCore.QRect(430, 45, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.SYS.setFont(font)
        self.SYS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.SYS.setStyleSheet("font: 81 36pt \"Open Sans ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(64, 64, 64);\n"
"background:transparent;")
        self.SYS.setFrame(False)
        self.SYS.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SYS.setObjectName("SYS")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(320, 357, 211, 41))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.name.setFont(font)
        self.name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.name.setStyleSheet("font: 20pt \"나눔고딕 ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(118, 113, 113);\n"
"background:transparent;")
        self.name.setFrame(False)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.date_now = QtWidgets.QLineEdit(self.centralwidget)
        self.date_now.setGeometry(QtCore.QRect(33, 351, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.date_now.setFont(font)
        self.date_now.setFocusPolicy(QtCore.Qt.NoFocus)
        self.date_now.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_now.setStyleSheet("color:rgb(64, 64, 64);\n"
"font: 8pt \"Open Sans\";\n"
"background:transparent;\n"
"\n"
"")
        self.date_now.setFrame(False)
        self.date_now.setAlignment(QtCore.Qt.AlignCenter)
        self.date_now.setObjectName("date_now")
        self.number = QtWidgets.QLineEdit(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(76, 397, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.number.setFont(font)
        self.number.setFocusPolicy(QtCore.Qt.NoFocus)
        self.number.setStyleSheet("background:transparent;\n"
"color:rgb(118, 113, 113);")
        self.number.setFrame(False)
        self.number.setAlignment(QtCore.Qt.AlignCenter)
        self.number.setObjectName("number")
        self.function_button = QtWidgets.QPushButton(self.centralwidget)
        self.function_button.setGeometry(QtCore.QRect(63, 48, 31, 31))
        self.function_button.setStyleSheet("border:none; background:transparent;")
        self.function_button.setText("")
        self.function_button.setObjectName("function_button")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(530, 361, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sex.setFont(font)
        self.sex.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sex.setStyleSheet("font: 20pt \"나눔고딕 ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(118, 113, 113);\n"
"background:transparent;")
        self.sex.setFrame(False)
        self.sex.setAlignment(QtCore.Qt.AlignCenter)
        self.sex.setObjectName("sex")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(630, 362, 121, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.age.setFont(font)
        self.age.setFocusPolicy(QtCore.Qt.NoFocus)
        self.age.setStyleSheet("font: 20pt \"나눔고딕 ExtraBold\";\n"
"gridline-color: rgb(0, 0, 0);\n"
"color:rgb(118, 113, 113);\n"
"background:transparent;")
        self.age.setFrame(False)
        self.age.setAlignment(QtCore.Qt.AlignCenter)
        self.age.setObjectName("age")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.graphicsView.setStyleSheet("background-image: url(:/newPrefix/main_released.PNG);")
        self.graphicsView.setObjectName("graphicsView")
        self.message = QtWidgets.QLineEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(320, 412, 421, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.message.setFont(font)
        self.message.setFocusPolicy(QtCore.Qt.NoFocus)
        self.message.setStyleSheet("font: 12pt \"나눔고딕 ExtraBold\";\n"
"color: rgb(225, 126, 66);\n"
"gridline-color: rgb(0, 0, 0);\n"
"background:transparent;")
        self.message.setFrame(False)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setObjectName("message")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(685, 127, 61, 211))
        self.start_button.setStyleSheet("border:none; background:transparent;")
        self.start_button.setText("")
        self.start_button.setObjectName("start_button")
        self.bt_device = QtWidgets.QGraphicsView(self.centralwidget)
        self.bt_device.setGeometry(QtCore.QRect(76, 91, 214, 214))
        self.bt_device.setStyleSheet("background-image: url(:/newPrefix/bt_device.png);\n"
"border:none;")
        self.bt_device.setObjectName("bt_device")
        self.bt_state = QtWidgets.QLineEdit(self.centralwidget)
        self.bt_state.setGeometry(QtCore.QRect(33, 333, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bt_state.setFont(font)
        self.bt_state.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_state.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bt_state.setStyleSheet("color:rgb(64, 64, 64);\n"
"font: 8pt \"Open Sans\";\n"
"background:transparent;\n"
"\n"
"")
        self.bt_state.setFrame(False)
        self.bt_state.setAlignment(QtCore.Qt.AlignCenter)
        self.bt_state.setObjectName("bt_state")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(75, 91, 216, 216))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.45 rgba(255, 90, 90, 187), stop:0.451 rgba(255, 255, 255, 0));\n"
"border-radius: 108px\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.bt_device_not = QtWidgets.QGraphicsView(self.centralwidget)
        self.bt_device_not.setGeometry(QtCore.QRect(85, 100, 196, 198))
        self.bt_device_not.setStyleSheet("background-image: url(:/newPrefix/bt_device_not.png);\n"
"border:none;")
        self.bt_device_not.setObjectName("bt_device_not")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(680, 40, 71, 61))
        self.save_button.setStyleSheet("border:none; background:transparent;")
        self.save_button.setText("")
        self.save_button.setObjectName("save_button")
        self.graphicsView.raise_()
        self.TEM.raise_()
        self.PUL.raise_()
        self.DIA.raise_()
        self.SYS.raise_()
        self.name.raise_()
        self.date_now.raise_()
        self.number.raise_()
        self.function_button.raise_()
        self.sex.raise_()
        self.age.raise_()
        self.message.raise_()
        self.start_button.raise_()
        self.bt_state.raise_()
        self.frame.raise_()
        self.bt_device_not.raise_()
        self.bt_device.raise_()
        self.save_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TEM.setText(_translate("MainWindow", "36.5"))
        self.PUL.setText(_translate("MainWindow", "80"))
        self.DIA.setText(_translate("MainWindow", "70"))
        self.SYS.setText(_translate("MainWindow", "120"))
        self.name.setText(_translate("MainWindow", "장건호"))
        self.date_now.setText(_translate("MainWindow", "yyyy-MM-dd ddd  a hh:mm"))
        self.number.setText(_translate("MainWindow", "33JHK34UD154"))
        self.sex.setText(_translate("MainWindow", "남"))
        self.age.setText(_translate("MainWindow", "25"))
        self.message.setText(_translate("MainWindow", "저장 완료!!"))
        self.bt_state.setText(_translate("MainWindow", "Thermometer is ready "))
import ver3_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
