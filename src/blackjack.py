import sys, os
import random

from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6 import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QPropertyAnimation, QPoint
from PyQt6.QtGui import QPixmap






class StartMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()

        


        """
        self.pic = QLabel()
        self.pic.setGeometry(10, 10, 4, 1)
        self.pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/test.png"))
        self.Layout.addWidget(self.pic)
        """

        """
        self.image = QLabel()
        self.image.setGeometry(50, 40, 25, 25)
        pixmap = QPixmap("test.png")
        self.image.setPixmap(pixmap)
        self.Layout.addWidget(self.image)
        """
        



        
        
        self.label = QLabel(self)
        pixmap = QPixmap('logo.png')
        pixmap = pixmap.scaled(700, 200)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.label)
        
        """

        self.label = QWidget(self)
        #pixmap = pixmap.scaled(700, 200)
        self.label.setStyleSheet("background-image: url(logo.png)")
        self.label.resize(100, 100)
        #self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.label)

        """

        
        """
        self.empty_space_01 = QWidget()
        self.empty_space_01.setFixedSize(1,300)
        self.Layout.addWidget(self.empty_space_01,0,0)
        """




        self.start_menu = ["NEW GAME","LEADERBOARD","CREDITS","QUIT"]
        self.start_menu_buttons = []

        for i in range(len(self.start_menu)):
            self.start_menu_button = QPushButton(self.start_menu[i])
            self.Layout.addWidget(self.start_menu_button,i+1,0, Qt.AlignmentFlag.AlignCenter)
            self.start_menu_button.setFixedSize(400, 60)
            self.start_menu_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
            self.start_menu_button.clicked.connect(self.button_clicked)
            self.start_menu_buttons.append(self.start_menu_button)
            
        
        self.empty_space_02 = QWidget()
        self.empty_space_02.setFixedSize(1,20)
        self.Layout.addWidget(self.empty_space_02,len(self.start_menu)+1,0)

        


        self.widget = QWidget()
        self.widget.setLayout(self.Layout)
        self.setCentralWidget(self.widget)




    def button_clicked(self):

        clicked_button = self.sender()
        #print(self.start_menu_buttons.index(clicked_button))

        if(self.start_menu_buttons.index(clicked_button) == 0):
            window.setCurrentWidget(page8)

        if(self.start_menu_buttons.index(clicked_button) == 1):
            window.setCurrentWidget(page3)

        if(self.start_menu_buttons.index(clicked_button) == 2):
            window.setCurrentWidget(page4)

        if(self.start_menu_buttons.index(clicked_button) == 3):
            sys.exit()
        







        




class MoneyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()


        self.token_list = ["t_1", "t_5", "t_10", "t_25", "t_50", "t_100", "t_250", "t_500", "t_1000", "t_5000"]
        self.no_token_list = ["n_1", "n_5", "n_10", "n_25", "n_50", "n_100", "n_250", "n_500", "n_1000", "n_5000"]

        self.chosen_buttons = []

        your_money = 100
        bet_money = 0

        for i in range(10):
            self.chosen_button = QPushButton("")
            if(i < 5):
                self.Layout.addWidget(self.chosen_button,0,i)
            else:
                self.Layout.addWidget(self.chosen_button,1,i-5)
            self.chosen_button.setFixedSize(90, 90)
            self.chosen_button.setIcon(QtGui.QIcon(f"images/tokens/{self.token_list[i]}.png"))
            self.chosen_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            self.chosen_button.setIconSize(QtCore.QSize(90,90))
            #self.chosen_button.clicked.connect(self.button_clicked)
            self.chosen_buttons.append(self.chosen_button)


        self.empty_space_01 = QWidget()
        self.empty_space_01.setFixedSize(1,60)
        self.Layout.addWidget(self.empty_space_01,2,0)




        self.token_buttons = []

        for i in range(10):
            self.token_button = QPushButton("")
            if(i < 5):
                self.Layout.addWidget(self.token_button,4,i)
            else:
                self.Layout.addWidget(self.token_button,5,i-5)
            self.token_button.setFixedSize(105, 105)
            self.token_button.setIcon(QtGui.QIcon(f"images/tokens/{self.token_list[i]}.png"))
            self.token_button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            self.token_button.setIconSize(QtCore.QSize(105,105))
            #self.token_button.clicked.connect(self.button_clicked)
            self.token_buttons.append(self.token_button)


        self.empty_space_02 = QWidget()
        self.empty_space_02.setFixedSize(30,30)
        self.Layout.addWidget(self.empty_space_02,4,5)

        self.empty_space_03 = QWidget()
        self.empty_space_03.setFixedSize(30,30)
        self.Layout.addWidget(self.empty_space_03,4,7)



        
        self.deal_button = QPushButton("DEAL")
        self.Layout.addWidget(self.deal_button,5,6)
        self.deal_button.setFixedSize(300, 120)
        self.deal_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
        self.deal_button.clicked.connect(self.button_clicked)

        self.my_money = QLabel(f"{your_money}$")
        font = self.my_money.font()
        font.setPointSize(30)
        self.my_money.setFont(font)
        self.my_money.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.my_money,3,0)

        self.chosen_money = QLabel(f"{bet_money}$")
        font = self.chosen_money.font()
        font.setPointSize(30)
        self.chosen_money.setFont(font)
        self.chosen_money.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Layout.addWidget(self.chosen_money,1,6)




        

        self.widget = QWidget()
        self.widget.setLayout(self.Layout)
        self.setCentralWidget(self.widget)


    def button_clicked(self):
        window.setCurrentWidget(page5)










class LeaderboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()

        self.empty_space_01 = QWidget()
        self.empty_space_01.setFixedSize(800,600)
        self.Layout.addWidget(self.empty_space_01,0,0)

        self.exit_button = QPushButton("BACK")
        self.Layout.addWidget(self.exit_button,1,1)
        self.exit_button.setFixedSize(100, 40)
        self.exit_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
        self.exit_button.clicked.connect(self.button_clicked)

        self.widget = QWidget()
        self.widget.setLayout(self.Layout)
        self.setCentralWidget(self.widget)


    def button_clicked(self):
        window.setCurrentWidget(page1)





class CreditsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()

        self.empty_space_01 = QWidget()
        self.empty_space_01.setFixedSize(800,600)
        self.Layout.addWidget(self.empty_space_01,0,0)

        self.exit_button = QPushButton("BACK")
        self.Layout.addWidget(self.exit_button,1,1)
        self.exit_button.setFixedSize(100, 40)
        self.exit_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
        self.exit_button.clicked.connect(self.button_clicked)

        self.widget = QWidget()
        self.widget.setLayout(self.Layout)
        self.setCentralWidget(self.widget)


    def button_clicked(self):
        window.setCurrentWidget(page1)








class GameWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()


        self.hit_button = QPushButton("HIT")
        self.Layout.addWidget(self.hit_button,1,0)
        self.hit_button.setFixedSize(100, 40)
        self.hit_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
        self.hit_button.clicked.connect(self.hit_clicked)

        self.stand_button = QPushButton("STAND")
        self.Layout.addWidget(self.stand_button,1,10)
        self.stand_button.setFixedSize(140, 40)
        self.stand_button.setStyleSheet("font: bold;background-color: white;font-size: 36px;")
        self.stand_button.clicked.connect(self.stand_clicked)



        self.player_cards = []
        self.dealer_cards = []
        
        self.dealer_card = QPushButton("")
        self.dealer_card.setIcon(QtGui.QIcon("test.png"))
        self.dealer_card.setIconSize(QtCore.QSize(70,100))
        self.dealer_cards.append(self.dealer_card)

        for i in range(2):
            self.player_card = QPushButton("")
            self.player_card.setIcon(QtGui.QIcon("test.png"))
            self.player_card.setIconSize(QtCore.QSize(70,100))
            self.player_cards.append(self.player_card)
            self.game()

        


    def game(self):

        for i in range(len(self.player_cards)):
            self.Layout.addWidget(self.player_cards[i],2,i)
            self.player_cards[i].setFixedSize(70,100)
            

        for i in range(len(self.dealer_cards)):
            self.Layout.addWidget(self.dealer_cards[i],0,i)
            self.dealer_cards[i].setFixedSize(70,100)

        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)





    def hit_clicked(self):
        self.player_card = QPushButton("")
        self.player_card.setIcon(QtGui.QIcon("test.png"))
        self.player_card.setIconSize(QtCore.QSize(70,100))
        self.player_cards.append(self.player_card)
        self.game()



    def stand_clicked(self):
        self.dealer_card = QPushButton("")
        self.dealer_card.setIcon(QtGui.QIcon("test.png"))
        self.dealer_card.setIconSize(QtCore.QSize(70,100))
        self.dealer_cards.append(self.dealer_card)

        self.game()









class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()



        self.return_button = QPushButton("RETURN")
        self.return_button.clicked.connect(self.exit)
        self.Layout.addWidget(self.return_button,2,0)

        #create OK-button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok)
        self.Layout.addWidget(self.ok_button,2,1)




        #create inputs Name, E-Mail
        self.name = QLineEdit(self)
        self.name.setMaxLength(10)
        self.password = QLineEdit(self)
        self.password.setMaxLength(16)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        counter = 0
        for i in ["name", "password"]:
            lbl = QLabel(i)
            font = lbl.font()
            font.setPointSize(18)
            lbl.setFont(font)
            self.Layout.addWidget(lbl, counter, 0)
            counter = counter + 1
        
        self.Layout.addWidget(self.name,0,1)
        self.Layout.addWidget(self.password,1,1)

        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)


    def exit(self):
        window.setCurrentWidget(page1)


    def ok(self):
        if(self.name.text() == "" or self.password.text() == ""):
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Question)
            message.setWindowTitle("Error-Window")
            message.setText("Alles muss ausgefüllt sein!")
            message.exec()
            return
        
        else:
            window.setCurrentWidget(page2)





class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()



        self.return_button = QPushButton("RETURN")
        self.return_button.clicked.connect(self.exit)
        self.Layout.addWidget(self.return_button,3,0)

        #create OK-button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.ok)
        self.Layout.addWidget(self.ok_button,3,1)




        #create inputs Name, E-Mail
        self.name = QLineEdit(self)
        self.name.setMaxLength(10)
        self.password = QLineEdit(self)
        self.password.setMaxLength(16)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password2 = QLineEdit(self)
        self.password2.setMaxLength(16)
        self.password2.setEchoMode(QLineEdit.EchoMode.Password)

        counter = 0
        for i in ["name", "password", "password 2"]:
            lbl = QLabel(i)
            font = lbl.font()
            font.setPointSize(18)
            lbl.setFont(font)
            self.Layout.addWidget(lbl, counter, 0)
            counter = counter + 1
        
        self.Layout.addWidget(self.name,0,1)
        self.Layout.addWidget(self.password,1,1)
        self.Layout.addWidget(self.password2,2,1)

        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)


    def exit(self):
        window.setCurrentWidget(page1)


    def ok(self):
        if(self.name.text() == "" or self.password.text() == "" or self.password2.text() == ""):
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Question)
            message.setWindowTitle("Error-Window")
            message.setText("Alles muss ausgefüllt sein!")
            message.exec()
            return
        
        elif(self.password.text() != self.password2.text()):
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Critical)
            message.setWindowTitle("Error-Window")
            message.setText("Passwörter müssen gleich sein!")
            message.exec()
            return
        
        else:
            window.setCurrentWidget(page2)










class RegOrLogWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set title
        self.setWindowTitle("Blackjack")

        #set window size
        self.setFixedSize(QSize(1000, 700))

        #create grid
        self.Layout = QGridLayout()


        self.register_button = QPushButton("REGISTER")
        self.register_button.clicked.connect(self.register)
        self.Layout.addWidget(self.register_button,0,0)

        self.login_button = QPushButton("LOGIN")
        self.login_button.clicked.connect(self.login)
        self.Layout.addWidget(self.login_button,0,1)

        self.return_button = QPushButton("RETURN")
        self.return_button.clicked.connect(self.exit)
        self.Layout.addWidget(self.return_button,1,1)



        widget = QWidget()
        widget.setLayout(self.Layout)
        self.setCentralWidget(widget)
    

    def register(self):
        window.setCurrentWidget(page7)

    def login(self):
        window.setCurrentWidget(page6)

    def exit(self):
        window.setCurrentWidget(page1)

























#main
app = QApplication(sys.argv)


window = QStackedWidget()


window.setStyleSheet("""
QMainWindow {
background-image:url(images/other/table.jpg);
background-repeat: no-repeat;
background-position: center;
}
""")


page1 = StartMenuWindow()
window.addWidget(page1) 

page2 = MoneyWindow()
window.addWidget(page2) 

page3 = LeaderboardWindow()
window.addWidget(page3) 

page4 = CreditsWindow()
window.addWidget(page4) 

page5 = GameWindow()
window.addWidget(page5) 

page6 = LoginWindow()
window.addWidget(page6)

page7 = RegisterWindow()
window.addWidget(page7)

page8 = RegOrLogWindow()
window.addWidget(page8)




#create window
#window = StartMenuWindow()
window.setCurrentWidget(page1)

#show window
window.show()

#start the event loop
app.exec()  
















