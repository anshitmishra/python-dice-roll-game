import random
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtGui
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("dice.ui",self)
        # counter for count who's turn
        self.counter = 0
        self.p1Total = 0
        self.p2Total = 0
        self.setWindowTitle("Dice roll")
        self.setWindowIcon(QtGui.QIcon('image/1.png'))
        # target elements on window 
        self.P1OnCount = self.findChild(QLabel,"label")
        self.P2OnCount = self.findChild(QLabel,"label_2")
        self.DiceImage = self.findChild(QLabel,"label_5")
        self.status = self.findChild(QLabel,"label_6")
        self.diceRoll = self.findChild(QPushButton,"pushButton_3")
        self.Newgame = self.findChild(QPushButton,"pushButton_4")
        self.P1OnTotalCount = self.findChild(QPushButton,"pushButton")
        self.P2OnTotalCount = self.findChild(QPushButton,"pushButton_2")

        # adding events
        self.diceRoll.clicked.connect(lambda: self.diceR())
        self.Newgame.clicked.connect(lambda: self.Restart())



        # show the app
        self.show()



    def diceR(self):
        Image = random.randint(1,6)
        pixmap = QPixmap(f'image/{Image}.png')
        self.DiceImage.setPixmap(pixmap)

        if self.counter % 2 == 0:
            self.status.setText("player 2 turn")
            self.P1OnCount.setText(f'{Image}')
            self.p1Total = self.p1Total + Image
            self.P1OnTotalCount.setText(f'{self.p1Total}')
        else:
            self.status.setText("player 1 turn")
            self.P2OnCount.setText(f'{Image}')
            self.p2Total = self.p2Total + Image
            self.P2OnTotalCount.setText(f'{self.p2Total}')

        if self.counter == 9:
            if self.p1Total > self.p2Total : 
                self.status.setText("player 1 Wins!")
            elif self.p2Total == self.p1Total:
                self.status.setText("Game Tie!")
            else:
                self.status.setText("player 2 Wins!")
            self.diceRoll.setEnabled(False)
            self.Newgame.setText("Restart")
        # counter increment
        self.counter += 1

    def Restart(self):
        pixmap = QPixmap(f'image/1.png')
        self.DiceImage.setPixmap(pixmap)
        self.status.setText("Player 1 turn Only 5 turn to each")
        self.p1Total = 0 
        self.p2Total = 0 
        self.counter = 0 
        self.P1OnCount.setText(f'0')
        self.P2OnCount.setText(f'0')
        self.P1OnTotalCount.setText(f'P1 total')
        self.P1OnTotalCount.setText(f'P1 total')
        self.P2OnTotalCount.setText(f'P2 total')
        self.Newgame.setText("New Game")
        self.diceRoll.setEnabled(True)


        pass


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
