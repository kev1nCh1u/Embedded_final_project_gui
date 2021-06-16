
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
    x = int(joystick_qwidget.joyPosXY[0]) + 50
    y = int(joystick_qwidget.joyPosXY[1]) + 50
    label4.setText('JOY_X:\0' + str(x))
    label5.setText('JOY_Y:\0' + str(y))
    if x != 50 or y != 50:
        if ser.portStatus:
            ser.write('V',x, y)
            label6.setText('Control:\0Virtual') # real virtual
    else:
        if ser.portStatus:
            ser.write('R')
            label6.setText('Control:\0Real') # real virtual

    # 3d move
    # v3d_qwidget.render.GetActiveCamera().SetPosition(x, y, 0.1)
    # v3d_qwidget.render.GetActiveCamera().Azimuth(180)
    # v3d_qwidget.render.ResetCamera()

    if ser.portStatus:
        input = ser.read()
        label2.setText('SERVO_X:\0' + str(input[0]))
        label3.setText('SERVO_Y:\0' + str(input[1]))


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
    label1.setText(ser.open(combobox1.currentText()))


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
    label1.setFont(QFont('Times', 20))
    label2 = QLabel()
    label2.setText('0')
    label2.setFont(QFont('Times', 20))
    label3 = QLabel()
    label3.setText('0')
    label3.setFont(QFont('Times', 20))
    label4 = QLabel()
    label4.setText('0')
    label4.setFont(QFont('Times', 20))
    label5 = QLabel()
    label5.setText('0')
    label5.setFont(QFont('Times', 20))
    label6 = QLabel()
    label6.setText('Control:\0real') # real virtual
    label6.setFont(QFont('Times', 20))

    # 下拉選單
    combobox1 = QComboBox()
    combobox1.setFont(QFont('Times', 20))
    ports = kevin_serial.serial_ports()
    combobox1.addItems(ports)
    # combobox1.activated[str].connect(Combobox1Changed)
    # label1.setText(ser.changePort(combobox1.currentText()))

    # 按鈕
    button1 = QPushButton('Refresh')
    button1.clicked.connect(refresh)
    button1.setFont(QFont('Times', 20))
    button2 = QPushButton('Connect')
    button2.clicked.connect(connect)
    button2.setFont(QFont('Times', 20))
    button3 = QPushButton('Disconnect')
    button3.clicked.connect(disconnect)
    button3.setFont(QFont('Times', 20))

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
    layout2.addWidget(label6)
    layout2.addWidget(label2)
    layout2.addWidget(label3)
    layout2.addWidget(joystick_qwidget)
    layout2.addWidget(label4)
    layout2.addWidget(label5)

    mainWindow.show()

    # Start Qt event loop unless running in interactive mode or using pyside.
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()
