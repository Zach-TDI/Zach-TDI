#need to change the Version of Python to 3.10
import sys
from socket import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    Width = 1080
    Height = 800
    w.resize(Width,Height)
    w.setWindowTitle('HotWire')
    w.show()
    sys.exit(app.exec_())


