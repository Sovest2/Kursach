# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moreWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_moreWindow(object):
    def setupUi(self, moreWindow):
        moreWindow.setObjectName("moreWindow")
        moreWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(moreWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 591))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.worknameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.worknameLabel.setObjectName("worknameLabel")
        self.verticalLayout.addWidget(self.worknameLabel)
        self.fieldLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fieldLabel.setObjectName("fieldLabel")
        self.verticalLayout.addWidget(self.fieldLabel)
        self.cafedraLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.cafedraLabel.setObjectName("cafedraLabel")
        self.verticalLayout.addWidget(self.cafedraLabel)
        self.consistencyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.consistencyLabel.setObjectName("consistencyLabel")
        self.verticalLayout.addWidget(self.consistencyLabel)
        self.consistencyTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.consistencyTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.consistencyTableWidget.setObjectName("consistencyTableWidget")
        self.consistencyTableWidget.setColumnCount(0)
        self.consistencyTableWidget.setRowCount(0)
        self.consistencyTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.consistencyTableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.consistencyTableWidget)
        self.costLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.costLabel.setObjectName("costLabel")
        self.verticalLayout.addWidget(self.costLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.editButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        moreWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(moreWindow)
        QtCore.QMetaObject.connectSlotsByName(moreWindow)

    def retranslateUi(self, moreWindow):
        _translate = QtCore.QCoreApplication.translate
        moreWindow.setWindowTitle(_translate("moreWindow", "Подробности"))
        self.worknameLabel.setText(_translate("moreWindow", "Название работы:"))
        self.fieldLabel.setText(_translate("moreWindow", "Область знания:"))
        self.cafedraLabel.setText(_translate("moreWindow", "Кафедра:"))
        self.consistencyLabel.setText(_translate("moreWindow", "Состав кафедры:"))
        self.costLabel.setText(_translate("moreWindow", "Затраты:"))
        self.backButton.setText(_translate("moreWindow", "Назад"))
        self.editButton.setText(_translate("moreWindow", "Изменить"))
        self.deleteButton.setText(_translate("moreWindow", "Удалить"))
