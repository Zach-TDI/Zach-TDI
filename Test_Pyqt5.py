from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from time import sleep

class Mywindow(QMainWindow):
    def __init__(self):
        super(Mywindow,self).__init__()
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle('HOT_WIRE')
        self.initUI()

    def initUI(self):
        self.labelB1 = QtWidgets.QLabel(self)
        self.labelB1.setText('myfirst Label')
        self.labelB1.move(50,0)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('myfirst Label')
        self.b1.move(25,50)
        self.b1.clicked.connect(self.clicked)

        self.labelB2 = QtWidgets.QLabel(self)
        self.labelB2.setText('myfirst Label')
        self.labelB2.move(200,0)
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText('myfirst Label')
        self.b2.move(175,50)
        self.b2.clicked.connect(self.clicked)

        self.labelB3 = QtWidgets.QLabel(self)
        self.labelB3.setText('myfirst Label')
        self.labelB3.move(350,0)
        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText('myfirst Label')
        self.b3.move(325,50)
        self.b3.clicked.connect(self.clicked)

        self.labelB4 = QtWidgets.QLabel(self)
        self.labelB4.setText('myfirst Label')
        self.labelB4.move(500,0)
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.setText('myfirst Label')
        self.b4.move(475,50)
        self.b4.clicked.connect(self.clicked)

    def clicked(self):
        self.labelB1.setText("You pressed the button")
        self.update()
    def update(self):
        self.label.adjustSize()


def window():
    app =QApplication(sys.argv)
    win = Mywindow()
    win.show()
    sys.exit(app.exec_())

window()