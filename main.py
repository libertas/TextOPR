#! /usr/bin/env python3

from PyQt4 import QtCore
from PyQt4.QtGui import *
import sys
import glob


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
        QtCore.QObject.connect(self.commitButton,\
            QtCore.SIGNAL("clicked()"),\
            self.textProcess)
        gridLayout.addWidget(self.commitButton,  3,  0)
        
        self.setLayout(gridLayout)
    
    def textProcess(self):
        fn = self.filenameEdit.text()
        src = self.srcEdit.text()
        dest = self.destEdit.text()
        
        gl = glob.glob(fn);

        for i in gl:
            file = open(i, "r")
            st = file.read()
            file.close()
            st = st.replace(src,  dest)
            file = open(i, "w")
            file.write(st)
            file.close()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
