from PyQt5.QtCore import QDate , QTime ,Qt


class Chrono:
    def __init__(self):
        pass

    def Get_Date(self):
        current_date = QDate.currentDate() #? the current date
        Date = current_date.toString(Qt.DefaultLocaleLongDate) #? Getting the long specfic date
        return Date

    def Get_Time(self):
        current_time = QTime.currentTime()
        Time = current_time.toString("hh:mm AP")#? hours and minutes in am pm format
        return Time

    def Days_till_xmas(self):
        current_date = QDate.currentDate() #? Getting the current date
        current_year = current_date.year() #? Grabbing year
        christmas = QDate(current_year,12,25) #? current year and then christmas
        Days_Till_Xmas = current_date.daysTo(christmas) #? Days to christmas
        return str(Days_Till_Xmas)

if __name__ == "__main__":
    C = Chrono()
    current_date = C.Get_Date()
    current_time = C.Get_Time()
    Days_Till_Xmas = C.Days_till_xmas()
    print(current_date)
    print(current_time)
    print(Days_Till_Xmas)
