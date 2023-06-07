from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from math import sqrt
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from random import randint
import serial
import time


matplotlib.use("Qt5Agg")


class plotter(QObject):
    finished = pyqtSignal()
    mean = pyqtSignal((float, float))

    def __init__(self, canvas):
        self.canvas = canvas
        QObject.__init__(self)
        self.running = True

    def work(self):
        global queue
        # arduino = serial.Serial("/dev/ttyACM0", 115200, timeout=None)
        # arduino.write("On".encode())
        val = ([], [])
        while (self.running):
            # number_str = arduino.readline().decode("ascii")
            # if (number_str == "\n"):
            #     break
            # print(number_str)
            # coords = mth.sqrt(sum(map(lambda x: x**2,
            #                           map(float, number_str.strip.split('')))))
            coords = randint(0, 3)
            time.sleep(1)
            val[1].append(coords)
            val[0].append(len(val[0]) * 0.5)
            self.canvas.axes.clear()
            self.canvas.axes.plot(
                val[0], val[1], 'r', linewidth=0.5)
            self.canvas.draw()
            mean_num = sum(val[1]) / len(val[1])
            # Standard deviation calculation
            sd_num = sqrt(
                sum(map(lambda x: (x - mean_num)**2, val[1])) /
                (len(val[1]) - 1)) if len(val[1]) > 1 else 0
            self.mean.emit(mean_num, sd_num)
            if (coords == 4):
                break
        self.finished.emit()


class Lab1(QMainWindow):

    thread = QThread()

    def __init__(self, *args):
        QMainWindow.__init__(self)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("arduino_sensors")
        self.ui.pushButton.clicked.connect(self.plot_grav)

    def print_extra(self, mean, sd):
        self.ui.textBrowser.setText(
            "mean:" + format(mean, ".2f") +
            "\nstandard dev.:" + format(sd, ".2f"))

    def plot_grav(self):
        if self.thread.isRunning():
            self.worker.running = False
            self.thread.quit()
            self.thread.wait()
        else:
            self.worker = plotter(self.ui.MplWidget.canvas)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.work)
            self.worker.finished.connect(self.thread.quit)
            self.worker.mean.connect(self.print_extra)
            self.thread.start()


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
