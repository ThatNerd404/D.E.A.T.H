# Main.py - Handles the functionality to the gui and grabbing the information nessasary to display the gui fully and correctly

import sys
import random 
import os
import pygame
import numpy as np

from pygame import mixer
from mutagen.mp3 import MP3

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollBar, QGridLayout
from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget, plot, ScatterPlotItem, GraphItem, mkBrush

from Automation_Functions.Chrono import Chrono
from Automation_Functions.Sky import Sky
from Automation_Functions.Inspire import Inspire
from Automation_Functions.Stats import Stats
from Gui.Main_Gui import Ui_MainWindow

#? The Starting window state
WINDOW_IS_MAXIMIZED = False


class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.ui.Pages.setCurrentWidget(self.ui.Home_Page)
        
        #? Grabbing needed data from module to display on gui
        Cron = Chrono() # Time data
        Date_Text = Cron.Get_Date()
        Xmas_Countdown_Text = Cron.Days_Till_Xmas()


        S = Sky() # Weather data
        Weather_Text, Temperature_Text, Feels_Like_Text = S.Fetch_Weather_Data()
        WeatherInfoDict = { 'Clear': {'img':'Gui/icons8-sun-96.png', 'Consensus': "Wear what you want the weather isn't a problem."},
                            'Clouds': {'img':'Gui/icons8-clouds-96.png', 'Consensus': 'Pack a coat just in case the weather might turn for the worse.'}, 
                            'Rain': {'img':'Gui/icons8-rainy-weather-96.png', 'Consensus': 'Wear a coat, the weather is bad.'},
                            'Mist':{'img':'Gui/icons8-haze-96.png', 'Consensus': 'Wear whatever but prepare for the humidity.'},
                            'Haze':{'img':'Gui/icons8-haze-96.png', 'Consensus': 'Wear whatever but prepare for the humidity.'},
                            'Snow':{'img':'Gui/icons8-snow-96.png', 'Consensus':'Wear a big coat it is freezing!'}}
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
        
        Inspiration = Inspire() # Quote data
        Quote, Author = Inspiration.Fetch_Inspiration()

        
        #? Fetching music files and putting it in list
        Music_Path = r'Music_Folder'
        self.Banger_Playlist = []
        for root, dirs, files in os.walk(Music_Path):
            for file in files:
                self.Banger_Playlist.append(os.path.join(root,file))
        
        
        Stat = Stats() # System data
        System_Info, Frequency, Battery, Total_Usage, Cpu_Usage = Stat.Check_System_Info()
        
        
        #? Load text from save files
        workouts_text = self.Load_File_Text("Save_Folder/Workouts_Save_File.txt")
        notes_text = self.Load_File_Text("Save_Folder/Notes_Save_File.txt") 

        self.ui.Workouts_text_edit.setText(workouts_text)
        self.ui.Notes_text_edit.setText(notes_text)
        self.ui.Date_Label.setText(Date_Text) #?Works on a different thread to not freeze gui
        Time_Text_Update = QTimer(self)
        Time_Text_Update.timeout.connect(lambda: self.ui.Time_Label.setText(Cron.Get_Time()))
        Time_Text_Update.start(1000)
        self.ui.Xmas_Countdown_Label.setText(f"{Xmas_Countdown_Text} Days 'Till Christmas!")

        self.ui.Weather_Label.setText(f"Weather: {Weather_Text}")
        self.ui.Temperature_Label.setText(f"Temperature: {Temperature_Text}")
        self.ui.Feels_Like_Label.setText(f"Feels Like: {Feels_Like_Text}")

        self.ui.Weather_Status_Pic.setPixmap(QPixmap(WeatherInfoDict[Weather_Text]['img']))
        self.ui.General_Consensus_Desc.setText(f"""Based on the weather you should: 
{WeatherInfoDict[Weather_Text]['Consensus']} \nBased on the temperature you should:
{Temp_Consensus} """)
        
        self.ui.Quote_and_Author_Label.setText(f"{Author}: {Quote}")
        
        #? Manully adding widgets that can't be added with QT designer
        Notes_text_edit_Scroll_Bar = QScrollBar(self)
        Notes_text_edit_Scroll_Bar.setStyleSheet("background : rgb(250,176,5);")
        self.ui.Notes_text_edit.setVerticalScrollBar(Notes_text_edit_Scroll_Bar)
        
        GraphWidget = plot()
        scatter = ScatterPlotItem(
            size=10, brush=mkBrush(30, 255, 35, 255))
        #LineDataItem = GraphItem()
        
        x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        y_data = [5, 4, 6, 4, 3, 5, 6, 6, 7, 8]
        scatter.setData(x_data,y_data)
        GraphWidget.addItem(scatter)
        Grid_Layout = QGridLayout() 
        Grid_Layout.addWidget(GraphWidget)
        self.ui.System_Stats_Content.setLayout(Grid_Layout)
     
         
        #? Setting timer for Song function
        self.Song_Bar_Update = QTimer(self)
        self.Song_Bar_Update.timeout.connect(lambda: self.Play_Time())
        
        #? Setting functions for buttons
        self.ui.Home_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Home_Page))
        self.ui.Time_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Time_Reminders_Page))
        self.ui.Weather_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Weather_Page))
        self.ui.Inspirations_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.Inspirations_Page))
        self.ui.System_Button.clicked.connect(lambda: self.ui.Pages.setCurrentWidget(self.ui.System_Stats_Page))
        self.ui.Close_Button.clicked.connect(lambda: self.close())
        self.ui.Maximize_Button.clicked.connect(lambda: self.Restore_or_Maximized())
        self.ui.Minimize_Button.clicked.connect(lambda: self.showMinimized())
        self.ui.Workout_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Workouts_text_edit,"Save_Folder/Workouts_Save_File.txt"))
        self.ui.Notes_Save_Button.clicked.connect(lambda: self.Save_Gui_Input(self.ui.Notes_text_edit,"Save_Folder/Notes_Save_File.txt"))
        self.ui.Play_Button.clicked.connect(lambda: self.Play_Song())
       
       
        
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
        global WINDOW_IS_MAXIMIZED
        win_status = WINDOW_IS_MAXIMIZED
        if win_status == False:
            WINDOW_IS_MAXIMIZED = True
            self.showMaximized()
        else:
            WINDOW_IS_MAXIMIZED = False
            self.showNormal()
    
    def Play_Song(self):
        if pygame.mixer.get_init():
            if self.ui.Play_Button.isChecked() == False:
                mixer.music.pause()
                self.Song_Bar_Update.stop()
                self.ui.Play_Button.setIcon(QIcon("Gui/icons8-play-32.png"))
                
            elif self.ui.Play_Button.isChecked() == True:
                mixer.music.unpause()
                self.Song_Bar_Update.start(1000)
                self.ui.Play_Button.setIcon(QIcon("Gui/icons8-pause-32.png"))
                
        else:
            pygame.init()
            pygame.mixer.music.set_endevent(pygame.USEREVENT)
            song = random.choice(self.Banger_Playlist)
            song_mutation = MP3(song)
            self.song_length = round(song_mutation.info.length)
            self.ui.Song_Progress_Bar.setMaximum(self.song_length)
            song_title = song.rstrip(".mp3").lstrip("Music_Folder\\")
            self.ui.Song_Title_Label.setText(song_title)
            mixer.init()
            mixer.music.load(song)
            mixer.music.play()
            self.Song_Bar_Update.start(1000)
            self.ui.Play_Button.setIcon(QIcon("Gui/icons8-pause-32.png"))
            
    def Play_Time(self):
        #? grab time in seconds rounded
        current_time = round(mixer.music.get_pos() / 1000)
        self.ui.Song_Progress_Bar.setValue(current_time)
        #? Check for music ending event and queue another song in responce 
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                self.Song_Bar_Update.stop()
                pygame.mixer.quit()
                self.Play_Song()
                self.Song_Bar_Update.start(1000)
    
def app():
    #TODO: Work on the system data page
    #TODO: pump the brakes on numpy and focus on learning to use the plot widget in general numpy and arrays may not be necessary 
    #still learn them tho
    #TODO: Learn numpy (specfically arrays) to help organize sys data to be put on graphs
    os.system('cls')
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




