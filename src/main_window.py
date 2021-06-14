
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt

import joystick
import pyqt_3d


if __name__ == '__main__':
    # Create main application window
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mainWindow = QMainWindow()
    mainWindow.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    window = QWidget()
    layout = QGridLayout()
    window.setLayout(layout)
    mainWindow.setCentralWidget(window)

    # Create joystick 
    joystick_qwidget = joystick.Joystick()

    # Create 3d 
    v3d_qwidget = pyqt_3d.Visualization3d()


    # 按鈕
    self.button1 = QPushButton('button1')
    self.button2 = QPushButton('button2')
    # self.button1.clicked.connect()

    # 水平佈局
    layout = QHBoxLayout()
    layout2 = QVBoxLayout()
    layout.addWidget(vll)
    layout2.addWidget(self.button1)
    layout2.addWidget(self.button2)
    layout.addLayout(layout2)
    
    # layout
    # layout.addLayout(joystick.get_joystick_layout(),0,0)
    layout.addWidget(joystick_qwidget,0,1)
    layout.addWidget(v3d_qwidget,0,0)

    mainWindow.show()

    ## Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()