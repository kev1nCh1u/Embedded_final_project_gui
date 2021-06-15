
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

import joystick
import pyqt_3d


def TimerLoop():
    print(joystick_qwidget.joyPosXY)
    x = joystick_qwidget.joyPosXY[0]/10
    y = joystick_qwidget.joyPosXY[1]/10

    # 3d move
    v3d_qwidget.render.GetActiveCamera().SetPosition(x, y, 0.1)
    v3d_qwidget.render.GetActiveCamera().Azimuth(180)
    v3d_qwidget.render.ResetCamera()

if __name__ == '__main__':
    # Create main application window
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mainWindow = QMainWindow()
    mainWindow.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    window = QWidget()
    # layout = QGridLayout()
    layout = QHBoxLayout()
    layout2 = QVBoxLayout()
    window.setLayout(layout)
    mainWindow.setCentralWidget(window)

    # Create joystick
    joystick_qwidget = joystick.Joystick()

    # Create 3d
    v3d_qwidget = pyqt_3d.Visualization3d()

    # 按鈕
    button1 = QPushButton('button1')
    button2 = QPushButton('button2')
    # button1.clicked.connect()

    
    combobox1 = QComboBox()
    combobox1.addItems

    timer = QTimer()  # 呼叫 QTimer
    timer.timeout.connect(TimerLoop)  # 當時間到時會執行 run
    timer.start(1)  # 啟動 Timer .. 每隔1000ms 會觸發 run

    # layout
    layout.addWidget(v3d_qwidget)
    layout.addLayout(layout2)

    # layout2
    layout2.addWidget(combobox1)
    layout2.addWidget(button1)
    layout2.addWidget(button2)
    layout2.addWidget(joystick_qwidget)
    

    mainWindow.show()

    # Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()
