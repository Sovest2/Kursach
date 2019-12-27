import pymysql
import json

#Dev
#hostname = "localhost"
#username = "root"
#password = "Qwerty123456"
#dbname = "kursach"

#Release
#hostname = "db4free.net"
#username = "sovest2"
#password = "Qwerty123456"
#dbname = "sovest_kursach"

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from requestsWindow import Ui_Requests  # импорт нашего сгенерированного файла
from moreWindow import Ui_moreWindow  # импорт нашего сгенерированного файла
from editWindow import Ui_editWindow
import sys



class requestsWindow(QtWidgets.QMainWindow):

    def update(self):
        con = pymysql.connect(hostname, username, password, dbname)
        with con:
            cur = con.cursor()
            cur.execute("SELECT id,nazvanie_raboti,oblast_znan,status,idkaf,idkonk FROM zayavki_kaf")
            self.requests = cur.fetchall()

            self.requestsWindow.tableWidget.setRowCount(len(self.requests))
            self.requestsWindow.tableWidget.setHorizontalHeaderLabels(("ID", "Название", "Область", "Статус"))
            row = 0
            for request in self.requests:
                col = 0
                for data in request:
                    cellinfo = QTableWidgetItem(str(data))
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.requestsWindow.tableWidget.setItem(row, col, cellinfo)
                    col += 1
                row += 1
        con.close()
        pass

    def showMore(self):
        self.selectedItemID = int(self.requestsWindow.tableWidget.selectedItems()[0].text())-1

        if self.selectedItemID != -1:
            self.moreWindow = moreWindow(self)
            self.moreWindow.setWindowModality(QtCore.Qt.WindowModal)
            #self.close()
            self.moreWindow.show()

    def showEdit(self):
        try:
            self.selectedItemID = int(self.requestsWindow.tableWidget.selectedItems()[0].text())-1
        except:
            self.selectedItemID = -1

        if self.selectedItemID !=-1:
            self.editWindows = editWindow(self)
            self.editWindows.setWindowModality(QtCore.Qt.WindowModal)
            self.editWindows.show()

    def __init__(self):
        self.requests = []
        self.selectedItemID = -1
        super(requestsWindow, self).__init__()
        self.requestsWindow = Ui_Requests()
        self.requestsWindow.setupUi(self)

        self.update()

        self.requestsWindow.moreButton.clicked.connect(self.showMore)
        self.requestsWindow.editButton.clicked.connect(self.showEdit)


class moreWindow(QtWidgets.QMainWindow):

    def update(self):
        self.root.update()
        self.selectedRequest = self.root.requests[self.root.selectedItemID]
        self.moreWindow.worknameLabel.setText("Название работы: " + self.selectedRequest[1])
        self.moreWindow.fieldLabel.setText("Область: " + self.selectedRequest[2])

        kafedraId = self.selectedRequest[4]
        con = pymysql.connect(hostname, username, password, dbname)
        with con:
            cur = con.cursor()
            cur.execute("SELECT kafedra, rukovoditel FROM kafedri WHERE id = " + str(kafedraId))
            kafedra = cur.fetchall()
            self.moreWindow.cafedraLabel.setText("Кафедра: " + kafedra[0][0])

            cur.execute("SELECT idsotr FROM sostav_kaf WHERE idkaf = " + str(kafedraId))
            personal = []
            for data in cur.fetchall():
                personal.append(data[0])


            self.moreWindow.consistencyTableWidget.setRowCount(len(personal))
            self.moreWindow.consistencyTableWidget.setColumnCount(4)
            self.moreWindow.consistencyTableWidget.setHorizontalHeaderLabels(
                ("ID", "ФИО", "Долженость", "Образование"))
            row = 0
            for personalID in personal:
                cur.execute("SELECT id, fio, dolgnost, obrazovanie FROM sotr WHERE id = " + str(personalID))
                personal = cur.fetchall()
                for teacher in personal:
                    col = 0
                    for data in teacher:
                        cellinfo = QTableWidgetItem(str(data))
                        cellinfo.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                        )
                        self.moreWindow.consistencyTableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
        con.close()
        pass

    def showEdit2(self):
        self.editWindows = editWindow(self)
        self.editWindows.setWindowModality(QtCore.Qt.WindowModal)
        self.editWindows.show()

    def __init__(self, root):
        super(moreWindow, self).__init__()
        self.root = root
        self.selectedRequest = self.root.requests[root.selectedItemID]
        self.moreWindow = Ui_moreWindow()
        self.moreWindow.setupUi(self)
        self.update()


        self.moreWindow.editButton.clicked.connect(self.showEdit2)
        self.moreWindow.backButton.clicked.connect(self.close)



class editWindow(QtWidgets.QMainWindow):
    def doSave(self):
        requestID = self.selectedRequest[0]
        newWorkname = self.editWindow.worknameEdit.text()
        newField = self.editWindow.fieldEdit.text()
        newKafedra = self.editWindow.kafedraComboBox.currentIndex()+1
        con = pymysql.connect(hostname, username, password, dbname)
        with con:
            cur = con.cursor()
            cur.execute("""UPDATE zayavki_kaf SET  idkaf = %s WHERE id = %s""",(str(newKafedra),requestID))
            cur.execute("""UPDATE zayavki_kaf SET  nazvanie_raboti = %s WHERE id = %s""",(newWorkname,requestID))
            cur.execute("""UPDATE zayavki_kaf SET  oblast_znan = %s WHERE id = %s""",(newField,requestID))

        con.commit()
        con.close()
        self.root.update()
        self.close()

    def comboChanged(self):
        self.editWindow.tableWidget.clear()
        con = pymysql.connect(hostname, username, password, dbname)
        with con:
            cur = con.cursor()

            cur.execute("SELECT idsotr FROM sostav_kaf WHERE idkaf = " + str(self.editWindow.kafedraComboBox.currentIndex()+1))
            personal = []
            for data in cur.fetchall():
                personal.append(data[0])

            self.editWindow.tableWidget.setRowCount(len(personal))
            self.editWindow.tableWidget.setColumnCount(4)
            self.editWindow.tableWidget.setHorizontalHeaderLabels(
                ("ID", "ФИО", "Долженость", "Образование"))
            row = 0
            for personalID in personal:
                cur.execute("SELECT id, fio, dolgnost, obrazovanie FROM sotr WHERE id = " + str(personalID))
                personal = cur.fetchall()
                for teacher in personal:
                    col = 0
                    for data in teacher:
                        cellinfo = QTableWidgetItem(str(data))
                        cellinfo.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                        )
                        self.editWindow.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
        con.close()

    def __init__(self, root):
        self.root = root
        try:
            self.selectedRequest = root.requests[root.selectedItemID]
        except:
            self.selectedRequest = root.selectedRequest
        super(editWindow, self).__init__()
        self.editWindow = Ui_editWindow()
        self.editWindow.setupUi(self)

        self.editWindow.worknameEdit.setText(self.selectedRequest[1])
        self.editWindow.fieldEdit.setText(self.selectedRequest[2])
        con = pymysql.connect(hostname, username, password, dbname)
        with con:
            cur = con.cursor()
            cur.execute("SELECT id,kafedra FROM kafedri ")

            kafedrs = cur.fetchall()

            for kafedra in kafedrs:
                self.editWindow.kafedraComboBox.addItem(kafedra[1])
            self.editWindow.kafedraComboBox.setCurrentIndex(self.selectedRequest[4]-1)

            cur.execute("SELECT idsotr FROM sostav_kaf WHERE idkaf = " + str(self.selectedRequest[4]))
            personal = []
            for data in cur.fetchall():
                personal.append(data[0])

            self.editWindow.tableWidget.setRowCount(len(personal))
            self.editWindow.tableWidget.setColumnCount(4)
            self.editWindow.tableWidget.setHorizontalHeaderLabels(
                ("ID", "ФИО", "Долженость", "Образование"))
            row = 0
            for personalID in personal:
                cur.execute("SELECT id, fio, dolgnost, obrazovanie FROM sotr WHERE id = " + str(personalID))
                personal = cur.fetchall()
                for teacher in personal:
                    col = 0
                    for data in teacher:
                        cellinfo = QTableWidgetItem(str(data))
                        cellinfo.setFlags(
                            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                        )
                        self.editWindow.tableWidget.setItem(row, col, cellinfo)
                        col += 1
                    row += 1
        con.close()

        self.editWindow.cancelButton.clicked.connect(self.close)
        self.editWindow.kafedraComboBox.activated[str].connect(self.comboChanged)
        self.editWindow.saveButton.clicked.connect(self.doSave)




with open("dbconfig.json", "r") as read_file:
    data = json.load(read_file)
    hostname = data["hostname"]
    username = data["username"]
    password = data["password"]
    dbname = data["dbname"]

app = QtWidgets.QApplication([])
application = requestsWindow()
application.show()
sys.exit(app.exec())
