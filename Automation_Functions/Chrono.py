# Chrono.py - module to fetch Date and Time in a pretty, readable format
# aka what time is it? 

from PyQt5.QtCore import QDate , QTime ,Qt

class Chrono:
    def __init__(self):
        pass

    def Fetch_DateTime_Info(self):
        
        #? Getting the current date in a nice format
        current_date = QDate.currentDate() 
        Pretty_Date = current_date.toString(Qt.DefaultLocaleLongDate) 
        
        #? Getting the current time in a nice format
        current_time = QTime.currentTime()
        Pretty_Time = current_time.toString("hh:mm AP")
        
        #? Using the current year to see how many days until christmas
        current_year = current_date.year() 
        christmas = QDate(current_year,12,25) 
        Days_Till_Xmas = str(current_date.daysTo(christmas))

        return Pretty_Date, Pretty_Time, Days_Till_Xmas

if __name__ == "__main__":
    C = Chrono()

    #? Remember has to be in this order to get right info in right variables
    current_date, current_time, Days_Till_Xmas = C.Fetch_DateTime_Info()
    print(current_date)
    print(current_time)
    print(Days_Till_Xmas)
