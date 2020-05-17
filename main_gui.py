# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appliesGrayScale = QtWidgets.QCheckBox(self.centralwidget)
        self.appliesGrayScale.setGeometry(QtCore.QRect(550, 30, 150, 23))
        self.appliesGrayScale.setObjectName("appliesGrayScale")
        self.takeCameraShot = QtWidgets.QPushButton(self.centralwidget)
        self.takeCameraShot.setGeometry(QtCore.QRect(570, 70, 120, 25))
        self.takeCameraShot.setObjectName("takeCameraShot")
        self.histogramView = QtWidgets.QGraphicsView(self.centralwidget)
        self.histogramView.setGeometry(QtCore.QRect(480, 150, 291, 321))
        self.histogramView.setObjectName("histogramView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 130, 81, 17))
        self.label.setObjectName("label")
        self.cameraView = QtWidgets.QGraphicsView(self.centralwidget)
        self.cameraView.setGeometry(QtCore.QRect(0, 0, 461, 551))
        self.cameraView.setObjectName("cameraView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appliesGrayScale.setText(_translate("MainWindow", "Gray Scale"))
        self.takeCameraShot.setText(_translate("MainWindow", "Start Capturing"))
        self.label.setText(_translate("MainWindow", "Histograma"))
