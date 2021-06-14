
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor
from PyQt5.QtCore import Qt


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = vtkMW()
    win.show()
    # win.iren.Initialize()
    sys.exit(app.exec_())