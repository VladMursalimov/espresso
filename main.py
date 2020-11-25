from PyQt5.QtWidgets import *
import sys
import sqlite3
from PyQt5 import uic


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        self.res = cur.execute("""SELECT DISTINCT id, sort, 
        roasting, ground, taste, price, volume FROM coffe""").fetchall()
        print(self.res)
        self.title = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                      'описание вкуса', 'цена', 'объем упаковки']
        self.tableWidget.setColumnCount(len(self.title))
        self.tableWidget.setHorizontalHeaderLabels(self.title)
        self.tableWidget.setRowCount(0)
        n = 0
        for i, j in enumerate(self.res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for x in range(7):
                self.tableWidget.setItem(n, x, QTableWidgetItem(str(j[x])))
            n += 1


if __name__ == '__main__':
    app = QApplication([])
    w = Widget()
    w.show()
    app.exec()