# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotter.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plotter(object):
    def setupUi(self, plotter):
        plotter.setObjectName("plotter")
        plotter.resize(500, 437)
        self.centralwidget = QtWidgets.QWidget(plotter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grafico = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.grafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grafico.setTextFormat(QtCore.Qt.AutoText)
        self.grafico.setAlignment(QtCore.Qt.AlignCenter)
        self.grafico.setObjectName("grafico")
        self.verticalLayout.addWidget(self.grafico)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 360, 351, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.iniciar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.iniciar.setObjectName("iniciar")
        self.horizontalLayout.addWidget(self.iniciar)
        self.parar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.parar.setObjectName("parar")
        self.horizontalLayout.addWidget(self.parar)
        #plotter.setCentralWidget(self.centralwidget)

        self.retranslateUi(plotter)
        QtCore.QMetaObject.connectSlotsByName(plotter)

    def retranslateUi(self, plotter):
        _translate = QtCore.QCoreApplication.translate
        plotter.setWindowTitle(_translate("plotter", "Plotter"))
        self.grafico.setText(_translate("plotter", "Grafico"))
        self.iniciar.setText(_translate("plotter", "Iniciar plotagem"))
        self.parar.setText(_translate("plotter", "Parar plotagem"))
