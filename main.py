import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

Form, Window = uic.loadUiType("Ui1.ui")


class Ui(QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Поиск по фильмам')
        self.setGeometry(500, 500, 530, 367)
        self.connection = sqlite3.connect("coffee.sqlite")
        res = self.connection.cursor().execute('SELECT * FROM Info').fetchall()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.name = self.connection.execute('SELECT * FROM Info')
        self.names = list(map(lambda x: x[0], self.name.description))
        self.tableWidget.setHorizontalHeaderLabels(self.names)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui()
    ex.show()
    sys.exit(app.exec())