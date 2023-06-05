import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from lab1_ui import *

import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Lab1(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino_sensors")


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
