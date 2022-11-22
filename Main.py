# Main.py - Handles the functionality to the gui and grabbing the information nessasary to display the gui fully and correctly

import sys
import random 
import os

from PyQt5 import QtCore , QtMultimedia  
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollBar
from PyQt5.QtCore import QTimer

from Automation_Functions.Chrono import Chrono
from Automation_Functions.Sky import Sky
from Automation_Functions.Inspire import Inspire
from Gui.Main_Gui import Ui_MainWindow

#? The Starting window size
WINDOW_SIZE = 0

class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.ui.Pages.setCurrentWidget(self.ui.Home_Page)
        
        #? Grabbing needed data from module to display on gui
        Cron = Chrono()
        Date_Text = Cron.Get_Date()
        Xmas_Countdown_Text = Cron.Days_Till_Xmas()

        S = Sky()
        Weather_Text, Temperature_Text, Feels_Like_Text = S.Fetch_Weather_Data()
        
        Inspiration = Inspire()
        Quote, Author = Inspiration.Fetch_Inspiration()
       
        #? Putting data in correct data structures
        WeatherInfoDict = { 'Clear': {'img':'Gui/icons8-sun-96.png', 'Consensus': "Where what you want the weather isn't a problem."},
                            'Clouds': {'img':'Gui/icons8-clouds-96.png', 'Consensus': 'Pack a coat just in case the weather might turn for the worse.'}, 
                            'Rain': {'img':'Gui/icons8-rainy-weather-96.png', 'Consensus': 'Wear a coat, the weather is bad.'} }
        
        #! The order of the elif statements matter. 
        # EX: if the <= 60 is first it will always return 60 even if its below 40
        if Temperature_Text >= 95:
            Temp_Consensus = "Wear VERY light clothing, the weathers sweltering."
        
        elif Temperature_Text >= 80:
            Temp_Consensus = "Wear light clothing, It's hot."     
        
        elif Temperature_Text <= 45:
            Temp_Consensus = "Wear VERY heavy clothing, It's freezing."

        elif Temperature_Text <= 60:
            Temp_Consensus = "Wear heavier clothing, It's cold."
        
        else:
            Temp_Consensus = "Wear what you want, The weather's fair."
        
        #? Fetching music and putting it in list
        Music_Path = r'C:/Users/MyCom\Desktop/.vscode/Github_Projects\D_E_A_T_H/Music_Folder'
        Banger_Playlist = []
        for root, dirs, files in os.walk(Music_Path):
            for file in files:
                Banger_Playlist.append(os.path.join(root,file))
        
        #? Grab text from save files
        workouts_text = self.Load_File_Text("Save_Folder/Workouts_Save_File.txt")
        notes_text = self.Load_File_Text("Save_Folder/Notes_Save_File.txt") 

         
        self.ui.Workouts_text_edit.setText(workouts_text)
        self.ui.Notes_text_edit.setText(notes_text)
        
        self.ui.Date_Label.setText(Date_Text)
        #?Works on a different thread to not freeze gui
        Time_timer = QTimer(self)
        #? adding action to timer
        Time_timer.timeout.connect(lambda: self.ui.Time_Label.setText(Cron.Get_Time()))
        #? update the timer every second p.s its in milliseconds
        Time_timer.start(1000)
        self.ui.Xmas_Countdown_Label.setText(f"{Xmas_Countdown_Text} Days 'Till Christmas!")

        self.ui.Weather_Label.setText(f"Weather: {Weather_Text}")
        self.ui.Temperature_Label.setText(f"Temperature: {Temperature_Text}")
        self.ui.Feels_Like_Label.setText(f"Feels Like: {Feels_Like_Text}")

        self.ui.Weather_Status_Pic.setPixmap(QPixmap(WeatherInfoDict[Weather_Text]['img']))
        self.ui.General_Consensus_Desc.setText(f"""Based on the weather you should: 
{WeatherInfoDict[Weather_Text]['Consensus']} \nBased on the temperature you should:
{Temp_Consensus} """)
        
        self.ui.Quote_and_Author_Label.setText(f"{Author}: {Quote}")
        
        #* Setting a scroll bar because you can't use qt designer
        # You have to create a scroll bar widget first to set another widget's scroll bar
        Notes_text_edit_Scroll_Bar = QScrollBar(self)
        Notes_text_edit_Scroll_Bar.setStyleSheet("background : rgb(250,176,5);")
        self.ui.Notes_text_edit.setVerticalScrollBar(Notes_text_edit_Scroll_Bar)
        
        #? Setting buttons functions 
        self.ui.Home_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Home_Page))
        self.ui.Time_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Time_Reminders_Page))
        self.ui.Weather_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Weather_Page))
        self.ui.Inspirations_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Inspirations_Page))
        self.ui.Close_Button.clicked.connect(lambda: self.close())
        self.ui.Maximize_Button.clicked.connect(lambda: self.Restore_or_Maximized())
        self.ui.Minimize_Button.clicked.connect(lambda: self.showMinimized())
        self.ui.Workout_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Workouts_text_edit,"Save_Folder/Workouts_Save_File.txt"))
        self.ui.Notes_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Notes_text_edit,"Save_Folder/Notes_Save_File.txt"))
        self.ui.Play_Pause_Music_Button.clicked.connect(lambda: self.OnPlaybutton(Banger_Playlist))
        
    #? Save all text from file to save_data variable
    def Load_File_Text(self,file):
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
    
    def OnPlaybutton(self,Playlist):
        #? Make song title presentable
        song_title = random.choice(Playlist).rstrip(".wav").lstrip("Music_Folder/")
        self.ui.Song_Title_Label.setText(song_title)
        
        #? Turn title into file and file into content it can read
        url = QtCore.QUrl.fromLocalFile(f"Music_Folder/{song_title}.wav")
        content = QtMultimedia.QMediaContent(url)
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(content)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        
        #? If music is playing stop and change
        if self.ui.Play_Pause_Music_Button.isChecked() == True:
            self.player.stop()
            self.ui.Play_Pause_Music_Button.setIcon(QIcon("Gui/icons8-play-32.png"))
            #self.ui.Play_Pause_Music_Button.se
        else:
            self.player.play()
            self.ui.Play_Pause_Music_Button.setIcon(QIcon("Gui/icons8-pause-32.png"))
           
def app():
    app = QApplication(sys.argv)
    win = Mainwindow()
    
    #? Adjusting window settings
    win.setWindowTitle("D.E.A.T.H - Developer Environment Automation & Task Handler")
    win.setWindowIcon(QIcon('Gui/icons8-headstone-100.png'))
    flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
    win.setWindowFlags(flags)
    
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
   app()




