#! /usr/bin/env python3

from PyQt4 import QtCore
from PyQt4.QtGui import *
import sys


class MainWindow(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QtCore.QSize(500, 400))
        self.setMaximumSize(QtCore.QSize(500, 400))
        self.setWindowTitle("TextOPR")
        self.resize(500, 400)
        
        gridLayout = QGridLayout()
        
        self.filenameEdit = QLineEdit()
        gridLayout.addWidget(QLabel("File:"),  0, 0)
        gridLayout.addWidget(self.filenameEdit,  0,  1)
        
        self.srcEdit = QLineEdit()
        gridLayout.addWidget(QLabel("Source Text:"),  1, 0)
        gridLayout.addWidget(self.srcEdit ,  1,  1)
        
        self.destEdit = QLineEdit()
        gridLayout.addWidget(QLabel("Dest Text:"),  2, 0)
        gridLayout.addWidget(self.destEdit,  2,  1)
        
        self.commitButton = QPushButton("OK")
        gridLayout.addWidget(self.commitButton,  3,  0)
        
        self.setLayout(gridLayout)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
