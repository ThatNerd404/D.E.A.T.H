# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui/Main_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        MainWindow.setMaximumSize(QtCore.QSize(5000, 5000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 520))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMinimumSize(QtCore.QSize(0, 73))
        self.Top_Bar.setStyleSheet("QPushButton{background-color: rgb(20,20,20)}\n"
"QFrame{background-color: rgb(20,20,20); \n"
"}\n"
"#Top_Bar{border-color:rgb(250,176,5);\n"
"border-width:1px;\n"
"border-style:solid;}\n"
"\n"
"QPushButton:hover{background-color:rgba(250,176,5,0.05)}")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Title_Bar = QtWidgets.QFrame(self.Top_Bar)
        self.Title_Bar.setStyleSheet("")
        self.Title_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title_Bar.setObjectName("Title_Bar")
        self.Title_icon = QtWidgets.QLabel(self.Title_Bar)
        self.Title_icon.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.Title_icon.setToolTipDuration(-1)
        self.Title_icon.setStyleSheet("font: 28pt \"MS Gothic\";")
        self.Title_icon.setText("")
        self.Title_icon.setPixmap(QtGui.QPixmap("Gui\\icons8-death-64.png"))
        self.Title_icon.setScaledContents(True)
        self.Title_icon.setObjectName("Title_icon")
        self.Title = QtWidgets.QLabel(self.Title_Bar)
        self.Title.setGeometry(QtCore.QRect(80, 10, 231, 51))
        self.Title.setStyleSheet("font: 75 36pt \"Palatino Linotype\"")
        self.Title.setObjectName("Title")
        self.Title_desc = QtWidgets.QLabel(self.Title_Bar)
        self.Title_desc.setGeometry(QtCore.QRect(320, 20, 361, 31))
        self.Title_desc.setStyleSheet("font: 11pt \"Palatino Linotype\"")
        self.Title_desc.setObjectName("Title_desc")
        self.horizontalLayout.addWidget(self.Title_Bar)
        self.Navigation_Button = QtWidgets.QFrame(self.Top_Bar)
        self.Navigation_Button.setMinimumSize(QtCore.QSize(0, 50))
        self.Navigation_Button.setMaximumSize(QtCore.QSize(100, 100))
        self.Navigation_Button.setStyleSheet("")
        self.Navigation_Button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navigation_Button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navigation_Button.setObjectName("Navigation_Button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Navigation_Button)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 37)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Minimize_Button = QtWidgets.QPushButton(self.Navigation_Button)
        self.Minimize_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Gui\\icons8-subtract-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Minimize_Button.setIcon(icon)
        self.Minimize_Button.setIconSize(QtCore.QSize(24, 24))
        self.Minimize_Button.setObjectName("Minimize_Button")
        self.horizontalLayout_2.addWidget(self.Minimize_Button)
        self.Maximize_Button = QtWidgets.QPushButton(self.Navigation_Button)
        self.Maximize_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Gui\\icons8-maximize-button-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Maximize_Button.setIcon(icon1)
        self.Maximize_Button.setIconSize(QtCore.QSize(24, 24))
        self.Maximize_Button.setObjectName("Maximize_Button")
        self.horizontalLayout_2.addWidget(self.Maximize_Button)
        self.Close_Button = QtWidgets.QPushButton(self.Navigation_Button)
        self.Close_Button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Gui\\icons8-close-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Close_Button.setIcon(icon2)
        self.Close_Button.setIconSize(QtCore.QSize(24, 24))
        self.Close_Button.setObjectName("Close_Button")
        self.horizontalLayout_2.addWidget(self.Close_Button)
        self.horizontalLayout.addWidget(self.Navigation_Button)
        self.verticalLayout_5.addWidget(self.Top_Bar)
        self.Main_Content = QtWidgets.QFrame(self.centralwidget)
        self.Main_Content.setMinimumSize(QtCore.QSize(0, 450))
        self.Main_Content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Main_Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Main_Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Main_Content.setObjectName("Main_Content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Main_Content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Side_Bar = QtWidgets.QFrame(self.Main_Content)
        self.Side_Bar.setMinimumSize(QtCore.QSize(120, 0))
        self.Side_Bar.setToolTipDuration(-1)
        self.Side_Bar.setStyleSheet("QFrame{background-color: rgb(27,27,27)}\n"
"\n"
"#Side_Bar{border-color:rgb(250,176,5);\n"
"border-width:1px;\n"
"border-style:solid;}\n"
"\n"
"QPushButton{border-radius:5px; background-color: rgb(27,27,27)}\n"
"\n"
"QPushButton:hover{background-color:rgba(250,176,5,0.05)}")
        self.Side_Bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Side_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Side_Bar.setObjectName("Side_Bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Side_Bar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Page_Buttons = QtWidgets.QFrame(self.Side_Bar)
        self.Page_Buttons.setMaximumSize(QtCore.QSize(40, 1000))
        self.Page_Buttons.setStyleSheet("")
        self.Page_Buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Page_Buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Page_Buttons.setObjectName("Page_Buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Page_Buttons)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Home_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.Home_Button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Gui\\icons8-home-page-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Home_Button.setIcon(icon3)
        self.Home_Button.setIconSize(QtCore.QSize(32, 32))
        self.Home_Button.setDefault(True)
        self.Home_Button.setFlat(True)
        self.Home_Button.setObjectName("Home_Button")
        self.verticalLayout.addWidget(self.Home_Button)
        self.Email_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.Email_Button.setToolTipDuration(-1)
        self.Email_Button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Gui\\icons8-secured-letter-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Email_Button.setIcon(icon4)
        self.Email_Button.setIconSize(QtCore.QSize(32, 32))
        self.Email_Button.setAutoDefault(False)
        self.Email_Button.setDefault(True)
        self.Email_Button.setFlat(True)
        self.Email_Button.setObjectName("Email_Button")
        self.verticalLayout.addWidget(self.Email_Button)
        self.Weather_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.Weather_Button.setToolTipDuration(-1)
        self.Weather_Button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Gui\\icons8-sun-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Weather_Button.setIcon(icon5)
        self.Weather_Button.setIconSize(QtCore.QSize(32, 32))
        self.Weather_Button.setDefault(True)
        self.Weather_Button.setFlat(True)
        self.Weather_Button.setObjectName("Weather_Button")
        self.verticalLayout.addWidget(self.Weather_Button)
        self.System_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.System_Button.setToolTipDuration(-1)
        self.System_Button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Gui\\icons8-tasks-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.System_Button.setIcon(icon6)
        self.System_Button.setIconSize(QtCore.QSize(32, 32))
        self.System_Button.setDefault(True)
        self.System_Button.setFlat(True)
        self.System_Button.setObjectName("System_Button")
        self.verticalLayout.addWidget(self.System_Button)
        self.Time_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.Time_Button.setToolTipDuration(-1)
        self.Time_Button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Gui\\icons8-clock-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Time_Button.setIcon(icon7)
        self.Time_Button.setIconSize(QtCore.QSize(32, 32))
        self.Time_Button.setDefault(True)
        self.Time_Button.setFlat(True)
        self.Time_Button.setObjectName("Time_Button")
        self.verticalLayout.addWidget(self.Time_Button)
        self.Quote_Button = QtWidgets.QPushButton(self.Page_Buttons)
        self.Quote_Button.setToolTipDuration(-1)
        self.Quote_Button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Gui\\icons8-quote-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Quote_Button.setIcon(icon8)
        self.Quote_Button.setIconSize(QtCore.QSize(32, 32))
        self.Quote_Button.setDefault(True)
        self.Quote_Button.setFlat(True)
        self.Quote_Button.setObjectName("Quote_Button")
        self.verticalLayout.addWidget(self.Quote_Button)
        self.verticalLayout_2.addWidget(self.Page_Buttons, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_4.addWidget(self.Side_Bar)
        self.Pages = QtWidgets.QStackedWidget(self.Main_Content)
        self.Pages.setStyleSheet("")
        self.Pages.setObjectName("Pages")
        self.Home_Page = QtWidgets.QWidget()
        self.Home_Page.setStyleSheet("background-color: rgb(15,15,15)")
        self.Home_Page.setObjectName("Home_Page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Home_Page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Home_Title = QtWidgets.QFrame(self.Home_Page)
        self.Home_Title.setMaximumSize(QtCore.QSize(16777215, 75))
        self.Home_Title.setStyleSheet("#Home_Title{border-color:rgb(250,176,5);\n"
"border-width:1px;\n"
"border-style:solid;}")
        self.Home_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_Title.setObjectName("Home_Title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Home_Title)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QLabel(self.Home_Title)
        self.title.setMaximumSize(QtCore.QSize(125, 16777215))
        self.title.setStyleSheet("color:rgb(250,176,5);\n"
"font: 28pt \"Palatino Linotype\";")
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addWidget(self.Home_Title)
        self.Home_Content = QtWidgets.QFrame(self.Home_Page)
        self.Home_Content.setStyleSheet("#Home_Content{border-color:rgb(250,176,5);\n"
"border-width:1px;\n"
"border-style:solid;}")
        self.Home_Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_Content.setObjectName("Home_Content")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Home_Content)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Home_Quote_and_Pic = QtWidgets.QFrame(self.Home_Content)
        self.Home_Quote_and_Pic.setMinimumSize(QtCore.QSize(317, 200))
        self.Home_Quote_and_Pic.setMaximumSize(QtCore.QSize(500, 300))
        self.Home_Quote_and_Pic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Home_Quote_and_Pic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Home_Quote_and_Pic.setObjectName("Home_Quote_and_Pic")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Home_Quote_and_Pic)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Home_PIC = QtWidgets.QLabel(self.Home_Quote_and_Pic)
        self.Home_PIC.setMinimumSize(QtCore.QSize(100, 100))
        self.Home_PIC.setMaximumSize(QtCore.QSize(100, 100))
        self.Home_PIC.setText("")
        self.Home_PIC.setPixmap(QtGui.QPixmap("Gui\\icons8-headstone-100.png"))
        self.Home_PIC.setObjectName("Home_PIC")
        self.verticalLayout_8.addWidget(self.Home_PIC, 0, QtCore.Qt.AlignHCenter)
        self.Home_QUOTE = QtWidgets.QLabel(self.Home_Quote_and_Pic)
        self.Home_QUOTE.setMinimumSize(QtCore.QSize(317, 0))
        self.Home_QUOTE.setMaximumSize(QtCore.QSize(317, 40))
        self.Home_QUOTE.setStyleSheet("color:rgb(250,176,5);\n"
"font: 10pt \"Palatino Linotype\";")
        self.Home_QUOTE.setObjectName("Home_QUOTE")
        self.verticalLayout_8.addWidget(self.Home_QUOTE)
        self.verticalLayout_7.addWidget(self.Home_Quote_and_Pic, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addWidget(self.Home_Content)
        self.Pages.addWidget(self.Home_Page)
        self.Time_Reminders_Page = QtWidgets.QWidget()
        self.Time_Reminders_Page.setStyleSheet("background-color: rgb(15,15,15)")
        self.Time_Reminders_Page.setObjectName("Time_Reminders_Page")
        self.Workouts_section = QtWidgets.QFrame(self.Time_Reminders_Page)
        self.Workouts_section.setGeometry(QtCore.QRect(80, 60, 341, 371))
        self.Workouts_section.setStyleSheet("")
        self.Workouts_section.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Workouts_section.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Workouts_section.setObjectName("Workouts_section")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Workouts_section)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Workouts_Title = QtWidgets.QFrame(self.Workouts_section)
        self.Workouts_Title.setMaximumSize(QtCore.QSize(180, 100))
        self.Workouts_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Workouts_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Workouts_Title.setObjectName("Workouts_Title")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Workouts_Title)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Dumbell_icon = QtWidgets.QLabel(self.Workouts_Title)
        self.Dumbell_icon.setMaximumSize(QtCore.QSize(32, 32))
        self.Dumbell_icon.setText("")
        self.Dumbell_icon.setPixmap(QtGui.QPixmap("Gui\\icons8-dumbbell-32.png"))
        self.Dumbell_icon.setObjectName("Dumbell_icon")
        self.horizontalLayout_3.addWidget(self.Dumbell_icon)
        self.Workout_label = QtWidgets.QLabel(self.Workouts_Title)
        self.Workout_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Workout_label.setStyleSheet("font: 24pt \"Palatino Linotype\";")
        self.Workout_label.setObjectName("Workout_label")
        self.horizontalLayout_3.addWidget(self.Workout_label)
        self.verticalLayout_4.addWidget(self.Workouts_Title, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.Workouts_section)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.Pages.addWidget(self.Time_Reminders_Page)
        self.horizontalLayout_4.addWidget(self.Pages)
        self.verticalLayout_5.addWidget(self.Main_Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "D.E.A.T.H."))
        self.Title_desc.setText(_translate("MainWindow", "Developer Environment Automation & Task Handler"))
        self.Home_Button.setToolTip(_translate("MainWindow", "Home"))
        self.Home_Button.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.Email_Button.setToolTip(_translate("MainWindow", "Emails"))
        self.Email_Button.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.Weather_Button.setToolTip(_translate("MainWindow", "Weather"))
        self.Weather_Button.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.System_Button.setToolTip(_translate("MainWindow", "System Information"))
        self.System_Button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.Time_Button.setToolTip(_translate("MainWindow", "Time & Reminders"))
        self.Time_Button.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.Quote_Button.setToolTip(_translate("MainWindow", "Quotes"))
        self.Quote_Button.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.title.setText(_translate("MainWindow", "Home"))
        self.Home_QUOTE.setText(_translate("MainWindow", "<html><head/><body><p>-Bringing death to mundane tasks, one task at a time!</p></body></html>"))
        self.Workout_label.setText(_translate("MainWindow", "Workouts"))
