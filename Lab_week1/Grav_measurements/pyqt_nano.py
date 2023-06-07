from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import math as mth
from lab1_ui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QThread, QObject, pyqtSignal
import sys
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from random import randint
import serial
from queue import Queue
import time


matplotlib.use("Qt5Agg")


class receive_input(QObject):
    finished = pyqtSignal()

    def __init__(self, queue):
        self._queue = queue
        QObject.__init__(self)
        self.running = True

    def work(self):
        global queue
        # arduino = serial.Serial("/dev/ttyACM0", 115200, timeout=None)
        # arduino.write("On".encode())
        while (self.running):
            # number_str = arduino.readline().decode("ascii")
            # if (number_str == "\n"):
            #     break
            # print(number_str)
            # coords = mth.sqrt(sum(map(lambda x: x**2,
            #                           map(float, number_str.strip.split('')))))
            coords = randint(0, 4)
            time.sleep(1)
            self._queue.put(coords)
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
        self.timer = QTimer()
        self.timer.timeout.connect(self.write_point)
        self._values = ([], [])
        self._queue = Queue()

    def write_point(self):
        val = self._values
        while not self._queue.empty():
            val[1].append(self._queue.get())
            val[0].append(len(val[0]) * 0.5)
        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.plot(
            val[0], val[1], 'r', linewidth=0.5)
        self.ui.MplWidget.canvas.draw()
        self.timer.start(500)

    def finish_worker(self):
        self.write_point()
        self.timer.stop()
        self.thread.quit()

    def plot_grav(self):
        if self.timer.remainingTime() > 0:
            self.timer.stop()
            self.worker.running = False
            self._queue = Queue()
            self.thread.quit()
            self.thread.wait()
        else:
            self._values = ([], [])
            self.timer.start(500)
            self.worker = receive_input(self._queue)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.work)
            self.worker.finished.connect(self.finish_worker)
            self.thread.start()


if __name__ == "__main__":
    app = QApplication([])
    form = Lab1()
    form.show()
    sys.exit(app.exec_())
