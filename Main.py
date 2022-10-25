# Main file for connecting function to the gui

import PyQt5
from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QPushButton
from PyQt5.QtGui import QPalette, QColor
import sys
from Gui.QT_test import Ui_MainWindow
from Automation_Functions.Inspire import Inspire
class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.ui.Thatbutton.clicked.connect(lambda: self.close()) # dont add () if you dont add stuff in it 
        #inspire = Quote, Author = Inspire.Inspiration(self) #<-- How I will set variable data to labels aka dont forget self
        #self.ui.Thatbutton.setText(Quote)
        
    def clicked(self):
        print("clicked")
    

def app():
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()#show Maxumized to show it full screen
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()
#finished with the classes now I am going to watch tech with tim then turtle code then read  pyqt5 article then read real python articles to work on pyqt5
# don't get stressed you just started and this is your research stage chill out my nigga 
# just learn what you need and return when you need to relearn 
# Finished with title bar and it is fire!!!!
# Nav buttons:
#close: self.close
#minimize: self.ShowMimized



