
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import joystick
import pyqt_3d
import kevin_serial

def TimerLoop():
    # print(joystick_qwidget.joyPosXY)
    x = joystick_qwidget.joyPosXY[0]/10
    y = joystick_qwidget.joyPosXY[1]/10

    # 3d move
    v3d_qwidget.render.GetActiveCamera().SetPosition(x, y, 0.1)
    v3d_qwidget.render.GetActiveCamera().Azimuth(180)
    v3d_qwidget.render.ResetCamera()

    input = ser.read()
    label2.setText(str(input[0]))
    label3.setText(str(input[1]))

def Combobox1Changed(text):
    # print(text)
    label1.setText(ser.changePort(text))

def refresh():
    ser.close()
    ports = kevin_serial.serial_ports()
    # print('refresh',ports)
    combobox1.clear()
    combobox1.addItems(ports)
    
def connect():
    label1.setText(ser.open())

def disconnect():
    label1.setText(ser.close())

if __name__ == '__main__':
    # Create main application window
    app = QApplication([])
    app.setStyle(QStyleFactory.create("Cleanlooks"))
    mainWindow = QMainWindow()
    app.setApplicationName("NTUST MAZE by kevin")
    app.setWindowIcon(QIcon("img/ntust.png"))
    # mainWindow.setWindowTitle('Joystick example')

    # Create and set widget layout
    # Main widget container
    window = QWidget()
    # layout = QGridLayout()
    layout = QHBoxLayout()
    layout2 = QVBoxLayout()
    window.setLayout(layout)
    mainWindow.setCentralWidget(window)

    # Create 3d
    v3d_qwidget = pyqt_3d.Visualization3d()

    # serial
    ser = kevin_serial.SerialFuc()

    # label
    label1 = QLabel()
    label1.setText('Disconnect')
    label2 = QLabel()
    label2.setText('0')
    label3 = QLabel()
    label3.setText('1')

    # 下拉選單
    combobox1 = QComboBox()
    # ports = kevin_serial.serial_ports()
    # combobox1.addItems(ports)
    combobox1.activated[str].connect(Combobox1Changed)

    # 按鈕
    button1 = QPushButton('refresh')
    button1.clicked.connect(refresh)
    button2 = QPushButton('connect')
    button2.clicked.connect(connect)
    button3 = QPushButton('disconnect')
    button3.clicked.connect(disconnect)

    # Create joystick
    joystick_qwidget = joystick.Joystick()

    # timer
    timer = QTimer()  # 呼叫 QTimer
    timer.timeout.connect(TimerLoop)  # 當時間到時會執行 run
    timer.start(1)  # 啟動 Timer .. 每隔1000ms 會觸發 run

    # layout
    layout.addWidget(v3d_qwidget)
    layout.addLayout(layout2)

    # layout2
    layout2.addWidget(label1)
    layout2.addWidget(combobox1)
    layout2.addWidget(button1)
    layout2.addWidget(button2)
    layout2.addWidget(button3)
    layout2.addWidget(label2)
    layout2.addWidget(label3)
    layout2.addWidget(joystick_qwidget)
    

    mainWindow.show()

    # Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()
