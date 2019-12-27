# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requestsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Requests(object):
    def setupUi(self, Requests):
        Requests.setObjectName("Requests")
        Requests.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Requests)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.moreButton = QtWidgets.QPushButton(self.centralwidget)
        self.moreButton.setGeometry(QtCore.QRect(260, 550, 75, 23))
        self.moreButton.setObjectName("moreButton")
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setGeometry(QtCore.QRect(350, 550, 75, 23))
        self.editButton.setObjectName("editButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(440, 550, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 761, 501))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        Requests.setCentralWidget(self.centralwidget)

        self.retranslateUi(Requests)
        QtCore.QMetaObject.connectSlotsByName(Requests)

    def retranslateUi(self, Requests):
        _translate = QtCore.QCoreApplication.translate
        Requests.setWindowTitle(_translate("Requests", "Заявки"))
        self.label.setText(_translate("Requests", "Заявки:"))
        self.moreButton.setText(_translate("Requests", "Подробней"))
        self.editButton.setText(_translate("Requests", "Изменить"))
        self.deleteButton.setText(_translate("Requests", "Удалить"))
        self.tableWidget.setSortingEnabled(False)
