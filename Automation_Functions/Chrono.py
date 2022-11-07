# Chrono.py - module to fetch Date and Time in a pretty, readable format
# aka what time is it? 

from PyQt5.QtCore import QDate , QTime ,Qt

class Chrono:
    def __init__(self):
        pass

    def Get_Date(self):
        
        #? Getting the current date in a nice format
        current_date = QDate.currentDate() 
        Pretty_Date = current_date.toString(Qt.DefaultLocaleLongDate) 
        return Pretty_Date

    def Get_Time(self):
        
        #? Getting the current time in a nice format
        current_time = QTime.currentTime()
        Pretty_Time = current_time.toString("hh:mm AP")
        return Pretty_Time

    def Days_Till_Xmas(self):

        #? Using the current year to see how many days until christmas
        current_date = QDate.currentDate()
        current_year = current_date.year() 
        christmas = QDate(current_year,12,25) 
        Days_Till_Xmas = current_date.daysTo(christmas) 
        return str(Days_Till_Xmas)

if __name__ == "__main__":
    C = Chrono()
    current_date = C.Get_Date()
    current_time = C.Get_Time()
    Days_Till_Xmas = C.Days_till_xmas()
    print(current_date)
    print(current_time)
    print(Days_Till_Xmas)
