from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow


class ImageBox(QMainWindow):
    def __init__(self):
        super(ImageBox, self).__init__()
        self.setFixedSize(800, 800)
        self.setWindowTitle("查看原图")
        self.setWindowIcon(QtGui.QIcon("images/puzzle.png"))
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 800))
