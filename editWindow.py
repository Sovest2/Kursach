# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editWindow(object):
    def setupUi(self, editWindow):
        editWindow.setObjectName("editWindow")
        editWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(editWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.worknameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.worknameEdit.setObjectName("worknameEdit")
        self.horizontalLayout.addWidget(self.worknameEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.fieldEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fieldEdit.setObjectName("fieldEdit")
        self.horizontalLayout_6.addWidget(self.fieldEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.kafedraComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.kafedraComboBox.setObjectName("kafedraComboBox")
        self.horizontalLayout_7.addWidget(self.kafedraComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_8.addWidget(self.cancelButton)
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_8.addWidget(self.deleteButton)
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_8.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        editWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(editWindow)
        QtCore.QMetaObject.connectSlotsByName(editWindow)

    def retranslateUi(self, editWindow):
        _translate = QtCore.QCoreApplication.translate
        editWindow.setWindowTitle(_translate("editWindow", "Изменить"))
        self.label.setText(_translate("editWindow", "Название:"))
        self.label_6.setText(_translate("editWindow", "Область:"))
        self.label_7.setText(_translate("editWindow", "Кафедра:"))
        self.cancelButton.setText(_translate("editWindow", "Отмена"))
        self.deleteButton.setText(_translate("editWindow", "Удалить"))
        self.saveButton.setText(_translate("editWindow", "Сохранить"))
