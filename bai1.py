# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bai1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
import  time
import sqlite3
import random
data = sqlite3.connect("databaseOne.db")

da = data.cursor()
da.execute('''create table if not exists MOITRUONG(nhiet char[10],am char[10])''')
#da.execute("INSERT INTO TAIKHOAN VALUES('37','26')")
data.commit()

class Ui_MainWindow(object):
    temperature=25
    humidity =70
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 306)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tvTemp = QtWidgets.QLabel(self.centralwidget)
        self.tvTemp.setGeometry(QtCore.QRect(120, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tvTemp.setFont(font)
        self.tvTemp.setObjectName("tvTemp")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tvHumid = QtWidgets.QLabel(self.centralwidget)
        self.tvHumid.setGeometry(QtCore.QRect(260, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tvHumid.setFont(font)
        self.tvHumid.setObjectName("tvHumid")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 40, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 130, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tvran1 = QtWidgets.QLabel(self.centralwidget)
        self.tvran1.setGeometry(QtCore.QRect(110, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tvran1.setFont(font)
        self.tvran1.setObjectName("tvran1")
        self.tvran2 = QtWidgets.QLabel(self.centralwidget)
        self.tvran2.setGeometry(QtCore.QRect(300, 130, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tvran2.setFont(font)
        self.tvran2.setObjectName("tvran2")
        self.btnRan = QtWidgets.QPushButton(self.centralwidget)
        self.btnRan.setGeometry(QtCore.QRect(40, 220, 111, 51))
        self.btnRan.setObjectName("btnRan")
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def EventCLickButtonRan(self):
        self.btnRan.clicked.connect(self.FunctionRandom)
    def FunctionRandom(self):
        number = int(random.random()*10)
        self.tvran1.setText(str(number))
        #random2 (0-1000) bo vao thread
    def readFile(self):
        file =open(r'G:\HEDIEUHANHTHOIGIANTHUC_RTOS\Thuctap\Python\RTOS_Week4\readme.txt')
        data = file.readlines()
        temp = data[0].split()
        humid =data[1].split()
        self.temperature=temp[1]
        self.humidity=humid[1]
        self.tvTemp.setText(self.temperature)
        self.tvHumid.setText(self.humidity)
    def showGui(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.readFile)
        self.timer.start()
    def saveToDb(self):
        envi=(
            (self.temperature,self.humidity)
        )
        da.execute("INSERT INTO MOITRUONG VALUES(?,?)",envi)
        data.commit()
    def callSaveDb(self):
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(5000)
        self.timer2.timeout.connect(self.saveToDb)
        self.timer2.start()
    def FunctionRandomAuto(self):
        number2 = int(random.random()*1000)
        self.tvran2.setText(str(number2))
    def FunctionRandomAutoTimer(self):
        self.timer3 = QtCore.QTimer()
        self.timer3.setInterval(500)
        self.timer3.timeout.connect(self.FunctionRandomAuto)
        self.timer3.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tvTemp.setText(_translate("MainWindow", "null"))
        self.label_2.setText(_translate("MainWindow", "T"))
        self.tvHumid.setText(_translate("MainWindow", "null"))
        self.label_4.setText(_translate("MainWindow", "H"))
        self.label_5.setText(_translate("MainWindow", "Ran2"))
        self.label_3.setText(_translate("MainWindow", "Ran1"))
        self.tvran1.setText(_translate("MainWindow", "null"))
        self.tvran2.setText(_translate("MainWindow", "null"))
        self.btnRan.setText(_translate("MainWindow", "random1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #*********************#
    ui.FunctionRandomAutoTimer()
    try:
        threadBtn =Thread(target=ui.EventCLickButtonRan())
        threadUpdateView = Thread(target=ui.showGui())
        threadSaveDatabase=Thread(target=ui.callSaveDb())
        threadBtn.start()
        threadUpdateView.start()
        threadSaveDatabase.start()

    except:
        print("ERROR")

    MainWindow.show()
    sys.exit(app.exec_())
