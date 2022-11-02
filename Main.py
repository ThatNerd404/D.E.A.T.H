# Main file for connecting function to the gui

import PyQt5
from PyQt5 import QtWidgets ,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QPushButton , QFileDialog
from PyQt5.QtGui import QPalette, QColor
import sys
from Gui.Main_Gui import Ui_MainWindow
from Automation_Functions.Inspire import Inspire

WINDOW_SIZE = 0

class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        #? starting widget
        self.ui.Pages.setCurrentWidget(self.ui.Home_Page)
         #? setting start widget page
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)#? getting rid of frame

        workouts_data = self.loadInput("Save_Folder/Workouts_Save_File.txt")
        notes_data = self.loadInput("Save_Folder/Notes_Save_File.txt") #? Grab data from save files
        self.ui.Workouts_text_edit.setText(workouts_data)
        self.ui.Notes_text_edit.setText(notes_data)
        #? Setting buttons functions 

        self.ui.Home_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Home_Page))
        self.ui.Time_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Time_Reminders_Page))
        self.ui.Close_Button.clicked.connect(lambda: self.close()) # dont add () if you dont add stuff in it 
        self.ui.Maximize_Button.clicked.connect(lambda: self.restore_or_maximized())
        self.ui.Minimize_Button.clicked.connect(lambda: self.showMinimized())
        self.ui.Workout_Save_Button.clicked.connect(lambda: self.saveInput(self.ui.Workouts_text_edit,"Save_Folder/Workouts_Save_File.txt"))
        self.ui.Notes_Save_Button.clicked.connect(lambda: self.saveInput(self.ui.Notes_text_edit,"Save_Folder/Notes_Save_File.txt"))

        #inspire = Quote, Author = Inspire.Inspiration(self) #<-- How I will set variable data to labels aka dont forget self
        #self.ui.Thatbutton.setText(Quote)
    def loadInput(self,file):
        with open(file,"r") as f:
            data = f.read()
        return data 
        
    def saveInput(self,widget,file): 
        contents = widget.toPlainText() 
        with open(file,"w") as f:
                f.write(contents)
        
    def restore_or_maximized(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:
            WINDOW_SIZE = 1
            self.showMaximized()
        else:
            WINDOW_SIZE = 0 
            self.showNormal()
    

def app():
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.showMaximized()#show Maxumized to show it full screen
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



