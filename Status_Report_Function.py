import PyQt5
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor
import sys
from QT_test import Ui_MainWindow
class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setupUi(self)

def app():
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()
