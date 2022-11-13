# Main.py - Handles the functionality to the gui and grabbing the information nessasary to display the gui fully and correctly

import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap, QIcon 
from PyQt5.QtWidgets import QApplication, QMainWindow

from Automation_Functions.Chrono import Chrono
from Automation_Functions.Sky import Sky
from Gui.Main_Gui import Ui_MainWindow

# The Starting window size
WINDOW_SIZE = 0

class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.ui.Pages.setCurrentWidget(self.ui.Home_Page)
        
        #? Grabbing needed data from module to display on gui
        Cron = Chrono()
        
        #* Using seperate functions to grab Datetime so I can make a thread to constantly check time
        Date_Text = Cron.Get_Date()
        Time_Text = Cron.Get_Time()
        Xmas_Countdown_Text = Cron.Days_Till_Xmas()

        S = Sky()
        Weather_Text, Temperature_Text, Feels_Like_Text = S.Fetch_Weather_Data()

        #? getting rid of frame
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        
        #? Grab text from save files
        workouts_data = self.Load_File_Input("Save_Folder/Workouts_Save_File.txt")
        notes_data = self.Load_File_Input("Save_Folder/Notes_Save_File.txt") 

        #? Setting text for different labels 
        self.ui.Workouts_text_edit.setText(workouts_data)
        self.ui.Notes_text_edit.setText(notes_data)

        self.ui.Date_Label.setText(Date_Text)
        self.ui.Time_Label.setText(Time_Text)
        self.ui.Xmas_Countdown_Label.setText(f"{Xmas_Countdown_Text} Days 'Till Christmas!")

        self.ui.Weather_Label.setText(f"Weather: {Weather_Text}")
        self.ui.Temperature_Label.setText(f"Temperature: {Temperature_Text}")
        self.ui.Feels_Like_Label.setText(f"Feels Like: {Feels_Like_Text}")

        if Weather_Text == "Clear":
            self.ui.Weather_Status_Pic.setPixmap(QPixmap('Gui/icons8-clouds-64.png'))

        elif Weather_Text == "Clouds":
            self.ui.Weather_Status_Pic.setPixmap(QPixmap('Gui/icons8-sun-64.png'))
        
        #? Setting buttons functions 
        self.ui.Home_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Home_Page))
        self.ui.Time_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Time_Reminders_Page))
        self.ui.Weather_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Weather_Page))
        self.ui.Close_Button.clicked.connect(lambda: self.close())
        self.ui.Maximize_Button.clicked.connect(lambda: self.Restore_or_Maximized())
        self.ui.Minimize_Button.clicked.connect(lambda: self.showMinimized())
        self.ui.Workout_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Workouts_text_edit,"Save_Folder/Workouts_Save_File.txt"))
        self.ui.Notes_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Notes_text_edit,"Save_Folder/Notes_Save_File.txt"))

        
        
        

    #? Save all text from file to save_data variable
    def Load_File_Input(self,file):
        with open(file,"r") as f:
            save_data = f.read()
        return save_data 

    #? write text from widget to file     
    def Save_Gui_Input(self,widget,file): 
        contents = widget.toPlainText() 
        with open(file,"w") as f:
                f.write(contents)
        
    def Restore_or_Maximized(self):
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
    win.setWindowTitle("D.E.A.T.H - Developer Environment Automation & Task Handler")
    win.setWindowIcon(QIcon('Gui/icons8-headstone-100.png'))
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()




