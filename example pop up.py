import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QApplication, QDialog
from time import sleep


class ExampleWidget(QWidget):

    def __init__(self):
        super().__init__()
        listWidget = QListWidget(self)
        listWidget.itemDoubleClicked.connect(self.buildExamplePopup)
        for n in ["Jack", "Chris", "Joey", "Kim", "Duncan"]:
            QListWidgetItem(n, listWidget)
        self.setGeometry(100, 100, 100, 100)
        self.showMaximized()

    @pyqtSlot(QListWidgetItem)
    def buildExamplePopup(self, item):
        exPopup = ExamplePopup(item.text(), self)
        exPopup.setGeometry(100, 200, 100, 100)
        exPopup.show()


class ExamplePopup(QDialog):

    def __init__(self, name, parent=None):
        super().__init__(parent)
        self.name = name
        self.label = QLabel(self.name, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExampleWidget()
    sys.exit(app.exec_())
